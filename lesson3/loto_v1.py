import random
import sys

class Card():

    def __init__(self, name='Компьютер'):
        if name == 'Компьютер':
            self.__mode = ' Карточка компьютера '
        elif not name.isalpha():
            raise SyntaxError
        else:
            self.__mode = ' Ваша карточка '

        self.__lotto_card = set()
        while len(self.__lotto_card) <= 14:
            self.__lotto_card.add(random.randint(1, 90))

        self.__lotto_list = list(map(str, sorted(self.__lotto_card)))

        for i in range(12):
            self.__lotto_list.insert(random.randrange(0, len(self.__lotto_list)), '__')

    def __str__(self):
        return '{:-^27}\n{:^27}\n{:^27}\n{:^27}\n' \
               '{:-^27}\n'.format(self.__mode,
                                  ' '.join(self.__lotto_list[::3]),
                                  ' '.join(self.__lotto_list[1::3]),
                                  ' '.join(self.__lotto_list[2::3]),
                                  '')

    def pop_item(self, item):
        try:
            self.__lotto_card.remove(int(item))
        except KeyError:
            print('Такого числа нет в вашей карте')
            print('Вы проиграли')
            sys.exit()

        ind = self.__lotto_list.index(item)
        self.__lotto_list[ind] = '--'

        if not self.__lotto_card:
            print('Все числа закрыты')
            if self.__mode == ' Карточка компьютера ':
                print("Компьютер победил!")
            else:
                print('Вы победили!')
            sys.exit()

    @property
    def get_set(self):
        return self.__lotto_card

rand_lst = [i for i in range(1, 91)]
random.shuffle(rand_lst)
numb_generator = iter(rand_lst)

if __name__ == '__main__':
    name = input('Ваше имя?\n>>> ')
    player = Card(name)
    ai = Card()
    counter = 90
    while counter > 0:
        counter -= 1
        print()
        print(player)
        print(ai)
        num = next(numb_generator)
        print('Новый бочонок: {} (осталось {})'.format(num, counter))
        while True:
            us_choice = input('Зачеркнуть цифру? (y/n); q - выход из игры\n>>> ')
            if us_choice.lower().strip() == 'y':
                player.pop_item(str(num))
                if num in ai.get_set:
                    ai.pop_item(str(num))
                break
            elif us_choice.lower().strip() == 'n':
                if num in ai.get_set:
                    ai.pop_item(str(num))
                break
            elif us_choice.lower().strip() == 'q':
                print('Выход из игры')
                sys.exit()
           
    print('Кончились бочонки')
