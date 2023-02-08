from abc import ABC, abstractmethod

class ClothesABC(ABC):
    @abstractmethod
    def cloth(self):
        pass

class Clothes(ClothesABC):
    def __init__(self, name):
        self._name = name
        self._cloth = 0

    def __add__(self, other):
        clothes = Clothes(f'{self.name}, {other.name}')
        clothes._cloth = self.cloth() + other.cloth()
        return clothes

    def __radd__(self, other):
        if not isinstance(other, Clothes):
            return self
        return self.__add__(other)

    def cloth(self):
        return self._cloth

    @property
    def name(self):
        return self._name

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size
        self._cloth = self._size / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height
        self._cloth = self._height * 2 + 0.3

coat1 = Coat('Пальто 1', 10)
coat2 = Coat('Пальто 2', 20)
suit1 = Suit('Костюм 1', 10)
suit2 = Suit('Костюм 2', 20)

print(f'Ткань для {coat1.name}: {coat1.cloth()}')
print(f'Ткань для {coat2.name}: {coat2.cloth()}')
print(f'Ткань для {suit1.name}: {suit1.cloth()}')
print(f'Ткань для {suit1.name}: {suit2.cloth()}')

clothes_list = [coat1, coat2, suit1, suit2]
full_calc = sum([item.cloth() for item in clothes_list])

print(f'Всего необходимо ткани: {full_calc}')
sum_clothes = coat2 = suit1
print(f'Всего необходимо ткани: {sum_clothes.name}: {sum_clothes.cloth()}')
sum_clothes = sum(clothes_list)
print(f'Ткань для: {sum_clothes.name}: {sum_clothes.cloth()}')














