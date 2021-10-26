cars_mas = [["А123БВ", "Toyota", "Spacio", "Серебристый"], ["Г456ДЕ", "Toyota", "MarkII", "Чёрный"], ["Ё789ЖЗ",
                                                                                                      "Москвич", "412",
                                                                                                      "Оранжевый"]]
#Привет
class Cars:
    number, brand, model, color = "", "", "", ""

    def __init__(self, n, b, m, c):
        self.number = n
        self.brand = b
        self.model = m
        self.color = c

    def add_to_list(self):
        cars_mas.append([self.number, self.brand, self.model, self.color])

    def delete(self):
        cars_mas.pop(cars_mas.index([self.number, self.brand, self.model, self.color]))
        print("Успешно удалено")

    def print_car(self):
        print(cars_mas.index([self.number, self.brand, self.model, self.color]), self.number, self.brand, self.model, self.color)

    def change(self, feature_n, new_feature):
        cars_mas[cars_mas.index([self.number, self.brand, self.model, self.color])][feature_n] = new_feature


def print_cars():
    for i in cars_mas:
        pcar = Cars(i[0], i[1], i[2], i[3])
        pcar.print_car()


def get_num(s):
    if s == "Номер" or s == "номер":
        return 0
    elif s == "Бренд" or s == "бренд":
        return 1
    elif s == "Модель" or s == "Модель":
        return 2
    elif s == "Цвет" or s == "Цвет":
        return 3
    else:
        return 4


def search(s):
    q = input("Введите характеристику: ")
    found = False
    for i in cars_mas:
        if i[s] == q:
            found_car = Cars(i[0], i[1], i[2], i[3])
            found_car.print_car()
            found = True
    if not found:
        print("Не найдено")


while True:
    command = input("Команды: выход, добавить, удалить, поиск, вывести, изменить: ")
    if command == "Выход" or command == "выход":
        print("До свидания")
        break
    elif command == "Добавить" or command == "добавить":
        data = input("Введите характеристики через пробел: Номер, Бренд, Модель, Цвет: ")
        try:
            number, brand, model, color = data.split()
            car = Cars(number, brand, model, color)
            car.add_to_list()
        except:
            print("Введите все характеристики")
    elif command == "удалить" or command == "Удалить":
        car_id = int(input("Введите id машины: "))
        if car_id < len(cars_mas):
            car = Cars(cars_mas[car_id][0], cars_mas[car_id][1], cars_mas[car_id][2], cars_mas[car_id][3])
            car.delete()
        else:
            print("Машины с таким id не существует!")
    elif command == "поиск" or command == "Поиск":
        search_by = input("По какой характеристике искать(Номер, Бренд, Модель, Цвет): ")
        search_by = get_num(search_by)
        if search_by == 4:
            print("Такой характеристики нет")
            continue
        else:
            search(search_by)
    elif command == "Вывести" or command == "вывести":
        print_cars()
    elif command == "Изменить" or command == "изменить":
        car_id = int(input("Введите id машины: "))
        if car_id < len(cars_mas):
            car = Cars(cars_mas[car_id][0], cars_mas[car_id][1], cars_mas[car_id][2], cars_mas[car_id][3])
            f = get_num(input("Что хотите изменить: "))
            if f != 4:
                n = input("На что поменять: ")
                car.change(f, n)
            else:
                print("Нет такой характеристики")
        else:
            print("Нет такой машины")
    else:
        print("Такой команды нет")
