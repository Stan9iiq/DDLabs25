import json
def goal() -> float:
    summ = 0
    with open("input.json", "r") as f:
        data = json.load(f)
        for item in data:
            summ += item["score"] * item["weight"]
    return round(summ, 3)
print(goal())