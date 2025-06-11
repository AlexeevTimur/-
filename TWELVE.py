zad = int(input("Введи номер в задачи: "))
if zad == 1:
    import json

    with open('список.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

elif zad == 2:
    import json

    try:
        with open("список.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"products": []}
    user_name = input("Введи название продукта: ")
    user_price = input("Введи цену продукта: ")
    user_weight = input("Введи вес продукта: ")
    user_products = {
        "name": user_name,
        "price": user_price,
        "available": True,
        "weight": user_weight
    }
    data["products"].append(user_products)

    with open("список.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

elif zad == 3:
    from collections import defaultdict

    ru_en_dict = defaultdict(list)

    with open('en-ru.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            if ' - ' in line:
                en_word, ru_translations = line.split(' - ')
                for ru_word in ru_translations.split(', '):
                    ru_en_dict[ru_word].append(en_word)

    with open('ru-eng.txt', 'w', encoding='utf-8') as outfile:
        for ru_word in sorted(ru_en_dict):
            en_words = ', '.join(sorted(ru_en_dict[ru_word]))
            outfile.write(f'{ru_word} – {en_words}\n')
    with open('ru-eng.txt', 'r', encoding='utf-8') as f:
        print(f.read())