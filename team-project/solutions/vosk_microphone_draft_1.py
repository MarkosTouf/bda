"""Simple Vosk example.

This records from the microphone, transcribes speech with Vosk, prints the
transcript, and saves it to transcript.txt.
"""

import json
import queue
from datetime import datetime
import sounddevice as sd
from vosk import Model, KaldiRecognizer

import csv #
import time #
import os          # NEW


MODEL_PATH = "solutions/vosk-model-en-us-0.22-lgraph" #m_note - to improve this path
SAMPLE_RATE = 16000
OUTPUT_FILE = "vosk_transcription.csv" ## m_note: would be csv

FIELDNAMES = ["timestamp", "name", "raw_text_vosk", "time_taken_sec"]  # m_note - list with fields

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))


model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

file_exists = os.path.isfile(OUTPUT_FILE)                              # m_note - check if file exists

while True:

    name = input("\nEnter (next) speaker name or 'done' to stop. Thanks: ").strip() #m_note strip() entered to remove a whitespace which was causing run issue
    
    if not name:
        continue
    
    if name.lower() == "done":
        break

    timestamp = datetime.now().isoformat()                       # m_note:moved here
    start_time = time.perf_counter() # m_note: start_time

    print("Recording in progress... Press Ctrl+C to stop.")

    full_text = ""

    with q.mutex:
        q.queue.clear()    

    try:
        with sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=8000,
            dtype="int16",
            channels=1,
            device=2,        # m_note: to select microphone device
            callback=callback,
        ):
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "")
                    if text:
                        print("You said:", text)
                        full_text += text + " "

    except KeyboardInterrupt:
        print("\nStopped recording.")

    # Very important: get the final remaining text.
    final_result = json.loads(recognizer.FinalResult())
    final_text = final_result.get("text", "")

    if final_text:
        print("Final:", final_text)
        full_text += final_text + " "

    # timestamp = datetime.now().isoformat() ## to move to put at start of talking

    end_time = time.perf_counter() # m_note:end_time
    time_taken = round(end_time - start_time,1) #m_note:time duration

    # with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    #     f.write(f"\n--- {timestamp} ---\n")
    #     f.write(full_text.strip() + "\n")

    # print(f"\nSaved to {OUTPUT_FILE}")
    # print("Transcript:", full_text.strip())

    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)              # NEW: DictWriter
        if not file_exists:                                            # NEW: header if new file
            writer.writeheader()                                       # NEW
            file_exists = True                                         # NEW
        writer.writerow({                                              # NEW
            "timestamp": timestamp,                                    # NEW
            "name": name,                                              # NEW
            "raw_text_vosk": full_text.strip(),                        # NEW
            "time_taken_sec": time_taken                               # NEW
        })                                                             # NEW

    print(f"Saved: {name} | {time_taken}s | {full_text.strip()}")     # NEW: 
