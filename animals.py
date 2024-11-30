def validate_age(age):
    try:
        return int(float(age))
    except (TypeError, ValueError):
        print('Некорректное значение: возраст должен быть целым числом. Используется значение по умолчанию: 0.')
        return 0

class Animal:
    """
    Базовый класс для всех животных.
    Содержит общие атрибуты и методы.
    """
    def __init__(self, species: str, name: str, age: int, sound: str=''):
        self.species = species
        self.name = name
        self.age = age
        self.sound = sound

    def display_info(self):
        raise NotImplementedError('Subclasses should implement this method')

    def make_sound(self):
        print(self.sound if self.sound else 'Ничего...')

    def eat(self):
        raise NotImplementedError('Subclasses should implement this method')

class Bird(Animal):
    def __init__(self, species: str, name: str, age: int, wingspan: float, sound: str=''):
        if not isinstance(wingspan, (int, float)):
            try:
                wingspan = float(wingspan)
            except (TypeError, ValueError):
                print('Некорректное значение: размах крыльев должен быть числом. Присвоено значение по умолчанию = 0.')
                wingspan = 0
        age = validate_age(age)
        super().__init__(species, name, age, sound)
        self.wingspan = wingspan

    def display_info(self):
        print(f'Птичка - {self.species} по имени {self.name}.\n'
              f'Возраст: {self.age}. '
              f'Поёт: {self.sound if self.sound else "ничего не поёт"}. Размах крыльев = {self.wingspan} см.')

    def make_sound(self):
        print(self.species, self.name, 'поёт:')
        super().make_sound()

    def eat(self):
        print('Ест зёрна')


class Mammal(Animal):
    def __init__(self, species: str, name: str, age: int, food: str, sound: str='', aquatic: bool=False):
        age = validate_age(age)
        super().__init__(species, name, age, sound)
        self.food = food
        self.aquatic = aquatic

    def display_info(self):
        print(f'Животное - {self.species} по имени {self.name}.'
              f'{"Водное." if self.aquatic else "Не водное."}\n'
              f'Возраст: {self.age}. Ест {self.food}.\n'
              f'Говорит: {self.sound if self.sound else "ничего не говорит"}.')
    def make_sound(self):
        print(self.species, self.name, 'говорит:')
        super().make_sound()

    def eat(self):
        print(self.species, self.name, 'ест', self.food)


class Reptile(Animal):
    def __init__(self, species: str, name: str, age: int, habitat: str,
                 is_venomous: bool, food: str, sound: str=''):
        if not isinstance(is_venomous, bool):
            is_venomous = False
        age = validate_age(age)
        super().__init__(species, name, age, sound)
        self.habitat = habitat
        self.is_venomous = is_venomous
        self.food = food

    def display_info(self):
        print(f'Рептилия - {self.species} по имени {self.name}.\n'
              f'Среда обитания: {self.habitat}\n'
              f'Возраст: {self.age}. Ест {self.food}.\n'
              f'Говорит: {self.sound if self.sound else "ничего не говорит"}.')
    def make_sound(self):
        print(self.species, self.name, 'говорит:')
        super().make_sound()

    def eat(self):
        print(self.species, self.name, 'ест', self.food)

def animal_sound(animals):
    # Звуки животных
    print('Звуки всех животных:')
    for animal in animals:
        animal.make_sound()

def test_animals():
    print('Птички:')
    parrot = Bird('Попугай', 'Mark', 10, 110.5)
    crow = Bird('Ворона', 'Мила', '5.3', 70, 'Кааарррр')
    test_bird1 = Bird('test', 'Test1-age', 'one', '10.13', 'ррр')
    test_bird2 = Bird('test', 'Test2-wings', 13.1, None, 'ррр2')
    print('info:')
    parrot.display_info()
    crow.display_info()
    test_bird1.display_info()
    test_bird2.display_info()
    print('eat:')
    parrot.eat()
    crow.eat()

    print('\nМлекопитающие:')
    horse = Mammal('Лошадь', 'Маша', 7, 'траву', 'Иго-го!')
    dolphin = Mammal('Дельфин', 'Дэн', 3.4, 'рыбу', '', True)
    test_mammal = Mammal('test_mammal', 'Test Mammal', 'one', 'test')
    print('info:')
    horse.display_info()
    dolphin.display_info()
    print('eat:')
    horse.eat()
    dolphin.eat()

    print('\nРептилии:')
    snake = Reptile('Змея', 'Чуча', 2, 'сухопутная',
                    True, 'мышек', 'шшш-шш')
    turtle = Reptile('Черепаха', 'Глаша', 10.111,
                     'полуводная', False, 'овощи')
    print('info:')
    snake.display_info()
    turtle.display_info()
    print('eat:')
    snake.eat()
    turtle.eat()

    all_animals = [parrot, crow, test_bird1, test_bird2, horse, dolphin,
                   test_mammal, snake, turtle]
    animal_sound(all_animals)

if __name__ == '__main__':
    test_animals()
