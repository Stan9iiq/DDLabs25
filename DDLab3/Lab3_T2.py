def find_common_participants(gr1, gr2, separator=','):
    num1 = set(gr1.split(separator))
    num2 = set(gr2.split(separator))
    identical = sorted(num1.intersection(num2))
    return identical

partgr1 = "Иванов|Петров|Сидоров"
partgr2 = "Петров|Сидоров|Смирнов"

identic = find_common_participants(partgr1, partgr2, separator='|')

print("Общие участники:", identic)