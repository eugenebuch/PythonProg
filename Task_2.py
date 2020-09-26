import time

class Pizza:
    name = "NaN"
    dough = "NaN"
    sauce = "NaN"
    filling = []
    cost = 0
    def __str__(self):
        filling = ", ".join(self.filling)
        return "Пиица: " + self.name + "\nТесто: " + self.dough + "\nСоус: " + self.sauce + "\nНачинка: " + filling + "\nЦена: " + str(self.cost) + "\n"


    def cook(self):
        print("Пиица " + self.name + " готовится...")
        time.sleep(5)
        print("Пицца готова!\n")

    def pack(self):
        print("Пицца " + self.name + " запаковывается...")
        time.sleep(3)
        print("Пицца упакована, забирайте!\n")
        

class PizzaPepperoni(Pizza):
    def __init__(self):
        self.name = "Пепперони"
        self.dough = "Толстое"
        self.sauce = "Сырный"
        self.filling = ["Пепперони", "Моцарелла", "Шампиньоны"]
        self.cost = 450

class PizzaSea(Pizza):
    def __init__(self):
        self.name = "Дары моря"
        self.dough = "Тонкое"
        self.sauce = "Сливочно-имбирный"
        self.filling = ["Кальмар", "Мидии", "Креветки"]
        self.cost = 700

class PizzaBBQ(Pizza):
    def __init__(self):
        self.name = "Барбекю"
        self.dough = "Тонкое"
        self.sauce = "Томатный барбекю"
        self.filling = ["Курица", "Томатная паста", "Огурец"]
        self.cost = 600

class Order:
    order = []

    def add(self, pizza):
        print("\n\tВ заказ добавлено:\n")
        print(pizza)
        print("\n")
        self.order.append(pizza)

    def final_sum(self):
        s = 0
        for elem in self.order:
            s += elem.cost
        return s

    def process(self):
        for elem in self.order:
            elem.cook()
            time.sleep(2)
            elem.pack()

class Terminal:
    menu = [PizzaPepperoni(), PizzaSea(), PizzaBBQ()]
    order = Order()
    def pay(self):
        print("\nЗаказ успешно принят и ожидает оплаты. Сумма: " + str(self.order.final_sum()))
        
    def command(self, inp):
        if inp in range(1, len(self.menu) + 1):
            self.order.add(self.menu[inp-1])
        else:
            print("Такого пункта меню нет")
        
    def show_menu(self):
        print("Меню ресторана: ")
        for i in range(len(self.menu)):
            print(str(i+1) + ". " + self.menu[i].name)
        while True:
            print("\nВыберите пункт меню: ")
            inp = input()
            if inp == '' or inp is None:
                self.pay()
                return
            self.command(int(inp))


def main():
    terminal = Terminal()
    terminal.show_menu()

main()
