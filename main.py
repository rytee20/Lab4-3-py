from Accessories import Accessories
from Clothes import Clothes
from Shoes import Shoes


def add_element():
    print("Ввод объекта с клавиатуры\n")

    # выбор какй именно товар надо добавить
    while True:
        try:
            choise=int(input("Вы хотите добавить одежду (нажмите 1), обувь (нажмите 2) или аксессуар (нажмите 3)? "))
            while choise>3 or choise<1:
                choise = int(input("Вы ввели неверно\nВы хотите добавить одежду (нажмите 1), обувь (нажмите 2) или аксессуар (нажмите 3)? "))
            break
        except:
            ValueError("Вы ввели неверно")
    # ввод названия
    while True:
        try:
            name=str(input("Введите название товара: "))
            break
        except:
            ValueError("Вы ввели неверно")
    # ввод ширины
    while True:
        try:
            width=float(input("Введите ширину товара: "))
            while width <= 0.0:
                width = int(input("Вы ввели неверно\nВведите ширину товара: "))
            break
        except:
            ValueError("Вы ввели неверно")
    # ввод длины
    while True:
        try:
            height=float(input("Введите высоту товара: "))
            while height <= 0.0:
                height = int(input("Вы ввели неверно\nВведите высоту товара: "))
            break
        except:
            ValueError("Вы ввели неверно")
    # ввод глубины
    while True:
        try:
            depth = float(input("Введите глубину товара: "))
            while depth <= 0.0:
                depth = int(input("Вы ввели неверно\nВведите глубину товара: "))
            break
        except:
            ValueError("Вы ввели неверно")
    # ввод цены
    while True:
        try:
            price = float(input("Введите цену товара: "))
            while price <= 0.01:
                price = int(input("Вы ввели неверно\nВведите цену товара: "))
            break
        except:
            ValueError("Вы ввели неверно")
    # ввод количества
    while True:
        try:
            amount = int(input("Введите количество товара: "))
            while amount <= 0:
                amount = int(input("Вы ввели неверно\nВведите количество товара: "))
            break
        except:
            ValueError("Вы ввели неверно")

    if choise==1:  # если выбрана одежда
        # ввод типа
        while True:
            try:
                type_of_clothes = str(input("Введите тип одежды (shirt или dress или skirt ли pants или outerwear): "))
                while type_of_clothes != "shirt" and type_of_clothes != "dress" and \
                        type_of_clothes != "skirt" and type_of_clothes != "pants" and \
                        type_of_clothes != "outerwear":
                    type_of_clothes = str(input("Вы ввели неверно\nВведите тип одежды "
                                                "(shirt или dress или skirt ли pants или outerwear): "))
                break
            except:
                ValueError("Вы ввели неверно")
        # ввод бренда
        while True:
            try:
                brand = str(input("Введите бренд одежды: "))
                break
            except:
                ValueError("Вы ввели неверно")
        # ввод пола
        while True:
            try:
                sex = str(input("Введите пол одежды (man или woman или unisex): "))
                while sex != "man" and sex != "woman" and sex != "unisex":
                    sex = str(input("Вы ввели неверно\nВведите пол одежды (man или woman или unisex): "))
                break
            except:
                ValueError("Вы ввели неверно")
        # ввод размера
        while True:
            try:
                size = int(input("Введите размер одежды: "))
                while 40 > size or size > 58:
                    size = int(input("Вы ввели неверно\nВведите размер одежды: "))
                break
            except:
                ValueError("Вы ввели неверно")

        # возвращаем элемент
        return Clothes(size, type_of_clothes, brand, sex, name, width, height, depth, price, amount)
    elif choise==2:  # если выбрана обувь
        # ввод типа
        while True:
            try:
                type_of_shoes = str(input("Введите тип обуви (high boots или high-heels или sneakers или other): "))
                while type_of_shoes != "high boots" and type_of_shoes != "high-heels" and \
                        type_of_shoes != "sneakers" and type_of_shoes != "other":
                    type_of_shoes = str(input("Вы ввели неверно\nВведите тип обуви "
                                                "(high boots или high-heels или sneakers или other): "))
                break
            except:
                ValueError("Вы ввели неверно")
        # ввод бренда
        while True:
            try:
                brand = str(input("Введите бренд обуви: "))
                break
            except:
                ValueError("Вы ввели неверно")
        # ввод пола
        while True:
            try:
                sex = str(input("Введите пол обуви (man или woman или unisex): "))
                while sex != "man" and sex != "woman" and sex != "unisex":
                    sex = str(input("Вы ввели неверно\nВведите пол обуви (man или woman или unisex): "))
                break
            except:
                ValueError("Вы ввели неверно")
        # ввод размера
        while True:
            try:
                size = int(input("Введите размер обуви: "))
                while 34 > size or size > 45:
                    size = int(input("Вы ввели неверно\nВведите размер обуви: "))
                break
            except:
                ValueError("Вы ввели неверно")

        # возвращаем объект
        return Shoes(size, type_of_shoes, brand, sex, name, width, height, depth, price, amount)

    else:  # если выбран аксессуар
        # ввод типа
        while True:
            try:
                type_of_accessory = str(input("Введите тип аксессуара (hat или bag или belt или other): "))
                while type_of_accessory != "hat" and type_of_accessory != "bag" and \
                        type_of_accessory != "belt" and type_of_accessory != "other":
                    type_of_accessory = str(input("Вы ввели неверно\nВведите тип "
                                                  "аксессуара (hat или bag или belt или other): "))
                break
            except:
                ValueError("Вы ввели неверно")
            # ввод бренда
            while True:
                try:
                    brand = str(input("Введите бренд аксессуара: "))
                    break
                except:
                    ValueError("Вы ввели неверно")
            # ввод пола
            while True:
                try:
                    sex = str(input("Введите пол аксессуара (man или woman или unisex): "))
                    while sex != "man" and sex != "woman" and sex != "unisex":
                        sex = str(input("Вы ввели неверно\nВведите пол аксессуара (man или woman или unisex): "))
                    break
                except:
                    ValueError("Вы ввели неверно")

        # возвращаем объект
        return Accessories(type_of_accessory, brand, sex, name, width, height, depth, price, amount)


#для примера
products_we_have = [Clothes(46, "shirt", "GloriaJeans", "woman", "Hello Kitty shirt", 20, 15, 1.2, 1499, 100),
                    Clothes(42, "dress", "GloriaJeans", "woman", "Little black dress", 20, 15, 1.5, 2499, 20),
                    Clothes(46, "dress", "O'stin", "woman", "Dress with flowers", 20, 15, 1.5, 2999, 143),
                    Clothes(48, "shirt", "O'stin", "man", "White shirt", 20, 15, 0.7, 1999, 45),
                    Clothes(48, "outerwear", "Mango", "woman", "Coat", 20, 15, 10, 7999, 3),
                    Clothes(50, "shirt", "O'stin", "man", "Hoody", 20, 15, 3, 3499, 80),
                    Shoes(37, "high-heels", "Nike", "woman", "Pink heels with bow", 25, 17, 10, 2499, 98),
                    Shoes(37, "sneakers", "Nike", "man", "Beautiful sneakers", 25, 17, 10, 2699, 100),
                    Accessories("belt", "GloriaJeans", "woman", "Jast a belt", 10, 5, 5, 999, 100),
                    Accessories("hat", "GloriaJeans", "unisex", "Hat with cat", 10, 5, 5, 1299, 23),
                    add_element()]

print("\n Вы ввели товар: ")
products_we_have[10].display_info()

print("\nДемонстрация перегрузки операции сложения как суммы цен товаров:\n Первый товар:")
products_we_have[1].display_info()
print("\n Второй товар:")
products_we_have[8].display_info()
print("\n Результат сложения:", products_we_have[1] + products_we_have[8])

print("\nДемонстрация метода, который возвращает количество данного товара который поместится в заданную коробку\n "
      "Товар:")
products_we_have[6].display_info()
while True:
    try:
        box_width = int(input("\nВведите ширину коробки: "))
        while box_width <= 0:
            box_width = int(input("Вы ввели неверно\n Введите ширину коробки: "))
        box_height = int(input("Введите длину коробки: "))
        while box_height <= 0:
            box_height = int(input("Вы ввели неверно\n Введите длину коробки: "))
        box_depth = int(input("Введите глубину коробки: "))
        while box_depth <= 0:
            box_depth = int(input("Вы ввели неверно\n Введите глубину коробки: "))
        break
    except:
        ValueError("Вы ввели неверно")
print("\nСтолько товара поместится в эту коробку: ",
      products_we_have[6].fit_in_a_box(box_width, box_height, box_depth))

print("Демострация работы метода вычисления цены со скидкой")
while True:
    try:
        discount = int(input("\nВведите скидку в процентах: "))
        while discount <= 0 or discount > 100:
            discount = int(input("Вы ввели неверно\n Введите скидку в процентах: "))
        break
    except:
        ValueError("Вы ввели неверно")
print("\n Обычный метод\n Товар:")
products_we_have[7].display_info()
print("Цена со скидкой: ", products_we_have[7].total_price(discount))

print("\n Переопределенный метод\n Товар:")
products_we_have[9].display_info()
print("Цена со скидкой: ", products_we_have[9].total_price(discount))
