class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0

    def go(self, speed=75):
        self.speed = speed
        print(f'Машина модели {self.name} тронулась, скорость {self.speed}.')

    def stop(self):
        self.speed = 0
        print(f'Машина модели {self.name} остановилась.')

    def turn(self, direction):
        if direction == 'лево' or direction == 'право':
            print(f'Машина модели {self.name} повернула на {direction}.')
        else:
            print(f'Машина запрограммирована поворачивать на лево и на право')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 72:
            print(f'Ваша скорость равна {self.speed}, что превышает допустимую скорость в 60 км/ч')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 41:
            print(f'Ваша скорость равна {self.speed}, что превышает допустимую скорость в 41 км/ч')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч.')


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar('красный', 'лада')
auto_1.go(60)
auto_2 = SportCar('синий', 'лада')
auto_2.go(120)
auto_3 = WorkCar('желтый', 'лада')
auto_3.go(80)
auto_3.show_speed()
auto_4 = TownCar('белый', 'лада')
auto_4.go(65)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()
