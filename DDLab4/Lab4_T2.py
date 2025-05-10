import csv
import json

inputf = "input.csv"
outputf = "output.json"

def task(f = "input.csv") -> None:
    csvf = open(f)
    read = csv.DictReader(csvf, delimiter=",", lineterminator="\n")
    data = list(read)
    with open("result.json", mode="w") as jsonf:
        json.dump(data, jsonf, indent=4)
    return None

if __name__ == '__main__':
    task()
    with open("result.json") as outf:
        for line in outf:
            print(line, end="")