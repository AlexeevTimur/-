zad = int(input("Введи номер в задачи: "))
if zad == 1:
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} сейчас открыт!")


    newRestaurant = Restaurant("Роллы Тимура", "Японская кухня")

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

elif zad == 2:
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}\n")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} сейчас открыт!\n")


    restaurant1 = Restaurant("Бон Ами", "Французская кухня")
    restaurant2 = Restaurant("Чончин", "Корейская кухня")
    restaurant3 = Restaurant("Рулетики", "Мясная кухня")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

elif zad == 3:
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}\n")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} сейчас открыт!\n")

        def update_rating(self, new_rating):
            if 0 <= new_rating <= 5:
                self.rating = new_rating
                print(f"Рейтинг ресторана '{self.restaurant_name}' обновлён до {self.rating}.\n")
            else:
                print("Ошибка: рейтинг должен быть от 0 до 5.\n")


    restaurants = [
        Restaurant("Бон Ами", "Французская кухня", 3.5),
        Restaurant("Чончин", "Корейская кухня", 4.0),
        Restaurant("Рулетики", "Японская кухня", 4.2)
    ]

    for restaurant in restaurants:
        restaurant.describe_restaurant()
        try:
            user_input = float(input(f"Введите новый рейтинг для '{restaurant.restaurant_name}' (от 0 до 5): "))
            restaurant.update_rating(user_input)
        except ValueError:
            print("Ошибка: введите числовое значение рейтинга.\n")

    print("Обновлённая информация о ресторанах:\n")
    fo3r restaurant in restaurants:
        restaurant.describe_restaurant()