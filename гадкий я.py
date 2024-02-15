while True:
    a = input("Ваше ім'я: ")
    if a.isalpha():
        print(a.capitalize())
    else:
        print("Ім'я не коректне")
        break
