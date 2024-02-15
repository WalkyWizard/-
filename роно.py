a = input("Введи речення")
char = input("Який символ будете шукати?")
count = 0
for i in a:
    if i == char:
        count += 1
print(f"символ '{char}' з'являється {count} разів у рядку")