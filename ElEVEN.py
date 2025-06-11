from PIL import Image
zad = int(input("Введи задание: "))
if zad == 1:
    from PIL import Image
    from pathlib import Path

    input_dir = Path('cats')
    output_dir = Path('blackcats')
    output_dir.mkdir(exist_ok=True)

    for file_path in input_dir.iterdir():
        if file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            img = Image.open(file_path)
            gray_img = img.convert('L')
            gray_img.save(output_dir / file_path.name)
elif zad == 2:
    from PIL import Image
    from pathlib import Path

    input_dir = Path('cats')

    valid_extensions = ['.jpg']

    filename = input("Введи имя фотки: ")

    file_path = input_dir / filename

    if file_path.exists() and file_path.suffix.lower() in valid_extensions:
        with Image.open(file_path) as img:
            img.show()
    else:
        print("НЕ ТОТ ФАЙЛ ИЛИ РАСШИРЕНИЕ!!!")

elif zad == 3:
    import csv

    filename = 'список.csv'

    total = 0

    print("Мама сказала купить:")

    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            product, quantity, price = row
            quantity = int(quantity)
            price = int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")
            total += quantity * price

    print(f"Итоговая сумма: {total} руб.")

