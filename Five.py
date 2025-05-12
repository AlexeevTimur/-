zad = input("Введи номер задачи: ")

if zad == "1":
    out = ""

    while True:
        word = input('Вводи слова, чтобы завершить — напиши "stop": ')
        if word.lower() == "stop":
            break
        if out == "":
            out = word
        else:
            out += " " + word

    print("Ваша строка:", out)

elif zad == "2":
    a = input("Введи редкое слово: ")

    if "ф" in a.lower():
        print(f"{a} ... Ого! Это слово реально редкое!")
    else:
        print(f"{a} Эх, это не такое редкое слово")
elif zad == "3":
    import random
    miss = 0
    right = 0

    while miss < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = input(f"{a} + {b} = ")

        if not answer.isdigit():
            print(" Нужны цифры ")
            continue

        if int(answer) == a + b:
            print(" Правильно ")
            right += 1
        else:
            print(" неверный ответ ")
            miss += 1

    print(f"Правильных ответов: {right}. game over.. ")