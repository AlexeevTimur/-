zad = int(input("Введи номер задачи: "))

if zad == 1:
    def check_divisible_by_3():
        try:
            A = int(input("Введите число: "))
            if A % 3 == 0:
                print("Число делится на 3")
            else:
                print("Число не делится на 3")
        except ValueError:
            print("Ошибка: введите целое число!")

    check_divisible_by_3()
elif zad == 2:
    def divide_100_by_user_number():
        try:
            number = int(input("Введите число, на которое нужно разделить 100: "))
            result = 100 / number
            print(f"Результат деления: {result}")
        except ValueError:
            print("Ошибка: нужно ввести целое число!")
        except ZeroDivisionError:
            print("Ошибка: на ноль делить нельзя!")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


    divide_100_by_user_number()
elif zad == 3:
    def Magicdata():
        try:
            Data = input("Введите дату в формате ДД.ММ.ГГГГ: ")
            day, month, year = map(int, Data.split('.'))

            konec = year % 100

            if day * month == konec:
                return True
            else:
                return False

        except ValueError:
            print("Ошибка: введите дату в правильном формате (ДД.ММ.ГГГГ).")
            return False

    if Magicdata():
        print("Магическая дата!")
    else:
        print("Это не она.")
elif zad == 4:
    def Dano(ticket_number):
        if len(ticket_number) % 2 != 0:
            print("Ошибка: номер билета должен содержать чётное количество цифр.")
            return False

        half_length = len(ticket_number) // 2
        fhalf = ticket_number[:half_length]
        shalf = ticket_number[half_length:]

        sum_first_half = sum(int(digit) for digit in fhalf)
        sum_second_half = sum(int(digit) for digit in shalf)

        return sum_first_half == sum_second_half

    ticket = input("Введите номер билета: ")

    if Dano(ticket):
        print("Счастливый билет!")
    else:
        print("Не счастливый билет.")