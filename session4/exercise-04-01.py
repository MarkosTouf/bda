import time

def task(name, seconds):
    print(f"Task {name} started")
    time.sleep(seconds)
    print(f"Task {name} finished")


start = time.perf_counter()

task("A", 2)
task("B", 2)

end = time.perf_counter()
print(f"Total time: {end - start:.2f}s")