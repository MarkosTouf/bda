def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line


count_lines = 0

for line in non_empty_lines("les_miserables.txt"):
    
    if "Jean" in line:
        print(line)
        count_lines += 1

print(count_lines)