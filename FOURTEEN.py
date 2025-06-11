zad = int(input("Введи номер в задачи: "))
if zad == 1:
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

    # Подкласс IceCreamStand
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            super().__init__(restaurant_name, cuisine_type, rating)
            self.flavors = ["ваниль", "шоколад", "клубника", "фисташка"]

        def display_flavors(self):
            print(f"Сорта мороженого в '{self.restaurant_name}':")
            for flavor in self.flavors:
                print(f"- {flavor}")
            print()

    # Создание экземпляра IceCreamStand
    ice_cream_cafe = IceCreamStand("Сладкий Рай", "Кафе-мороженое", 4.5)

    # Вызов метода
    ice_cream_cafe.describe_restaurant()
    ice_cream_cafe.display_flavors()


elif zad == 2:
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


    # Подкласс с расширениями
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, location, hours, rating=0):
            super().__init__(restaurant_name, "Кафе-мороженое", rating)
            self.location = location
            self.hours = hours
            self.flavors = []
            self.types = {
                "мороженое на палочке": [],
                "мягкое мороженое": [],
                "фруктовый лёд": []
            }

        def describe_stand(self):
            self.describe_restaurant()
            print(f"Локация: {self.location}")
            print(f"Время работы: {self.hours}\n")

        def add_flavor(self, flavor):
            if flavor not in self.flavors:
                self.flavors.append(flavor)
                print(f"Добавлен сорт: {flavor}")
            else:
                print(f"Сорт уже есть: {flavor}")

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Удалён сорт: {flavor}")
            else:
                print(f"Сорт не найден: {flavor}")

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"Сорт '{flavor}' в наличии.")
                return True
            else:
                print(f"Сорт '{flavor}' отсутствует.")
                return False

        def add_type_flavor(self, ice_type, flavor):
            if ice_type in self.types:
                self.types[ice_type].append(flavor)
                print(f"Добавлен '{flavor}' в '{ice_type}'")
            else:
                print(f"Тип '{ice_type}' не найден.")

        def display_all_flavors(self):
            print("\nОсновные сорта мороженого:")
            for flavor in self.flavors:
                print(f"- {flavor}")
            print("\nСорта по типам:")
            for ice_type, flavors in self.types.items():
                print(f"{ice_type}: {', '.join(flavors) if flavors else 'Нет'}")
            print()


    stand = IceCreamStand("Сладкий Рай", "Парк Горького", "10:00–21:00", 4.7)

    stand.describe_stand()

    stand.add_flavor("ваниль")
    stand.add_flavor("шоколад")
    stand.remove_flavor("клубника")
    stand.check_flavor("ваниль")

    stand.add_type_flavor("мягкое мороженое", "банановое")
    stand.add_type_flavor("мороженое на палочке", "кокосовое")
    stand.display_all_flavors()

elif zad == 3:
    import tkinter as tk
    from tkinter import messagebox


    # Класс IceCreamStand
    class IceCreamStand:
        def __init__(self, name, location, working_hours, flavors=None):
            self.name = name
            self.location = location
            self.working_hours = working_hours
            self.flavors = flavors if flavors else []

        def get_flavors(self):
            return self.flavors

        def add_flavor(self, flavor):
            if flavor and flavor not in self.flavors:
                self.flavors.append(flavor)
                return True
            return False


    # Интерфейс с помощью tkinter
    class IceCreamApp:
        def __init__(self, root, ice_cream_stand):
            self.ice_cream_stand = ice_cream_stand
            self.root = root
            self.root.title("Кафе-мороженое")

            # Название
            self.title_label = tk.Label(root, text=f"{ice_cream_stand.name}", font=("Arial", 18, "bold"))
            self.title_label.pack(pady=10)

            # Кнопка показать вкусы
            self.show_button = tk.Button(root, text="Показать вкусы", command=self.show_flavors)
            self.show_button.pack()

            # Список вкусов
            self.flavor_listbox = tk.Listbox(root, width=40, height=6)
            self.flavor_listbox.pack(pady=5)

            # Поле для добавления нового вкуса
            self.entry_label = tk.Label(root, text="Добавить новый вкус:")
            self.entry_label.pack()
            self.new_flavor_entry = tk.Entry(root)
            self.new_flavor_entry.pack()

            # Кнопка "Добавить"
            self.add_button = tk.Button(root, text="Добавить вкус", command=self.add_flavor)
            self.add_button.pack(pady=5)

        def show_flavors(self):
            self.flavor_listbox.delete(0, tk.END)
            for flavor in self.ice_cream_stand.get_flavors():
                self.flavor_listbox.insert(tk.END, flavor)

        def add_flavor(self):
            new_flavor = self.new_flavor_entry.get().strip()
            if self.ice_cream_stand.add_flavor(new_flavor):
                messagebox.showinfo("Успех", f"Добавлен вкус: {new_flavor}")
                self.show_flavors()
            else:
                messagebox.showwarning("Ошибка", "Пустой или уже существующий вкус.")
            self.new_flavor_entry.delete(0, tk.END)


    # Создаём кафе и запускаем приложение
    if __name__ == "__main__":
        stand = IceCreamStand("Мороженка", "Центр", "10:00–22:00", ["ваниль", "шоколад", "клубника"])

        root = tk.Tk()
        app = IceCreamApp(root, stand)
        root.mainloop()
