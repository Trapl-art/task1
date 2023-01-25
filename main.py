class Auto:
    # Автомобиль
    # имеет цвет
    # имеет мощность дивгателя
    # имеет максимальный запас бензина в баке
    # имеет расход (например 9.3 литра на 100 км)
    # можно перекрасить
    # можно заправить N литров
    # можно проехать N киллометров
    # можно узнать цвет
    # мощность
    # сколько осталось литров в баке
    # узнать расход
    color: str = "green"
    power: int = 100
    maxbac: int = 80  # имеет максимальный запас бензина в баке
    expense: float = 9.3  # имеет расход (например 9.3 литра на 100 км)
    now_bac: int = 20

    def __init__(self, color = "red", power = 200, maxbac = 100, expense = 7, now_bac = 20,
                 interval = 50, place = 4, acolor = "grey"):
        self.color = color
        self.power = power
        self.maxbac = maxbac
        self.expense = expense
        self.now_bac = now_bac
        self.interval = interval
        self.place = place
        self.acolor = acolor
    
    
    def set_color(self, acolor): 
        self.color = acolor
        return self.color
        
    def get_color(self): 
        return self.color


    def get_fuel(self, maxbac):
        return self.maxbac

    def set_fuel(self, maxbac):
        self.maxbac = maxbac
        return self.maxbac

    def get_now_bac(self, now_bac):
        return self.now_bac

    def get_expense(self):
        return self.expense

    def get_refuel(self):
        return self.maxbac - self.now_bac

    def refuel(self, maxbac):
        if self.maxbac >= self.now_bac:
            if maxbac > a.get_refuel():
                print("нельзя дозаправить")
            else:
                self.now_bac += maxbac
                return self.now_bac
        else:
            print("дозаправить не нужно")

    def distante(self):
        return self.now_bac / self.expense

    def get_power(self):
        return self.power

    def get_remained(self, expense, interval):
        return self.expense / 100 * self.interval
    def places(self):
        return self.place 
    def print(self):

        print(f"""
        1.машина покрашена в {self.get_color()}
        2.машина перекрашена в {self.set_color(self.acolor)}
        3.бак вмещает литров {self.get_fuel(80)}
        4.бак содержит {self.now_bac}
        5.можно залить {self.get_refuel()}
        6.можно проехать {self.distante()}
        7.мощность двигателя {self.get_power()}
        8.расход двигателя {self.get_expense()}
        9.осталось в баке {self.get_remained(expense=9.3, interval=50)} литров
            """)

a = Auto(color="red", power=250, maxbac=70, expense=9.3, now_bac=70, interval=50, place=4, acolor = "grey")
a.print()

b = Auto(color="бежевый", power=250, maxbac=70, expense=9.3, now_bac=70, interval=50, place=4, acolor = "морской")
b.print()

def test_init_1():
    Auto(color='white',
        power=90,
        maxbac=50,
        expense=9.3,
        now_bac=0)


def test_init_2():
    Auto(color='white')


def test_color_1():
    c = Auto(color='white',
            power=90,
            maxbac=50,
            expense=9.3,
            now_bac=0)
    assert c.get_color() == 'white'


def test_color_2():
    c = Auto(color='white',
            power=90,
            maxbac=50,
            expense=9.3,
            now_bac=0)
    assert c.get_color() == 'white'
    c.set_color('red')


def test_color_3():
    c = Auto(color='white',
            power=90,
            maxbac=50,
            expense=9.3,
            now_bac=0)
    assert c.get_color() == 'white'
    c.set_color('red')

    assert c.get_color() == 'red'
    
test_init_1()
test_init_2()
test_color_1()
test_color_2()
test_color_3()
