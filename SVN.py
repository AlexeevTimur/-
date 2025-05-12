zad = int(input("Введи задание: "))

if zad == 1:
    numbers = [5, 6, 12, 25, 31]
    user_input = int(input("Введите число: "))
    print("Список чисел:", numbers)
    print("Вы ввели число:", user_input)
    if user_input in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")

elif zad == 2:
    chislo = input("Введи числа через пробел: ")
    my_list = list(map(int, chislo.split()))
    duplicates = set()

    for item in my_list:
        if my_list.count(item) > 1:
            duplicates.add(item)

    if duplicates:
        print("Повторяющиеся элементы:", duplicates)
    else:
        print("Повторяющихся элементов нет.")

elif zad == 3:
    days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    n = int(input("Сколько выходных на неделе вы хотите? "))

    weekends = list(days[-n:]) if n <= len(days) else list(days)
    workdays = list(days[:-n]) if n <= len(days) else []

    print("Ваши выходные дни:", weekends)
    print("Ваши рабочие дни:", workdays)

elif zad == 4:
    group1 = ["Алексеев", "Шакиров", "Барченков", "Фараджева", "Мухамадиев", "Ившина", "Пищикова", "Шумакова", "Попова",
              "Шевченко"]
    group2 = ["Смирнов", "Иванов", "Сальвина", "Васильева", "Гомодрилов", "Пупок", "Винокуров", "Белокуров", "Боп",
              "Томтосов"]

    team = tuple(group1[:5] + group2[:5])

    print("Группа 1:", group1)
    print("Группа 2:", group2)
    print("Спортивная команда:", team)

    print("Длина команды:", len(team))

    sorted_team = tuple(sorted(team))
    print("Отсортированная команда:", sorted_team)

    searchname= input("Введи фамилию студента: ")

    namecount = team.count(searchname)
    if searchname in team:
        print(f"{searchname} входит в команду.")
    else:
        print(f"{searchname} не входит в команду.")
    print(f"Фамилия '{searchname}' встречается {namecount} раз.")

