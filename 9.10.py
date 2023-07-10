# Joshua Soto
# 1553869

import csv

file_dict = {}
filename = input()
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for lineArray in reader:
        for key in lineArray:
            if key in file_dict:
                file_dict[key] = file_dict[key] + 1
            else:
                file_dict[key] = 1

for key, count in file_dict.items():
    print(key, count)
