zad = int(input("Введи задание: "))
if zad == 1:
    countries = {
        "Россия": "Москва",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Италия": "Рим",
        "Япония": "Токио"
    }

    for country, capital in countries.items():
        print(f"{country} — {capital}")

    print()

    print("Столица Германии:", countries.get("Германия"))

    print()

    for country in sorted(countries):
        print(f"{country} — {countries[country]}")

elif zad == 2:
    points = {
        1: "АВЕИНОРСТ",
        2: "ДКЛМПУ",
        3: "БГЁЬЯ",
        4: "ЙЫ",
        5: "ЖЗХЦЧ",
        8: "ШЭЮ",
        10: "ФЩЪ"
    }

    letter_values = {letter: score for score, letters in points.items() for letter in letters}

    word = input("Введите слово: ").upper()

    total = sum(letter_values.get(letter, 0) for letter in word)

    print(f"Стоимость слова '{word}' составляет {total} очков.")
