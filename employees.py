import animals

class Employee:
    """
    Базовый класс для всех работников.
    Содержит общие атрибуты и методы.
    """
    employee_id = 1

    def __init__(self, full_name: str, birth: str, job_title: str):
        self.id = Employee.employee_id
        Employee.employee_id += 1
        self.full_name = full_name
        self.birth = birth
        self.job_title = job_title

    def __str__(self):
        return f'ID: {self.id} | {self.job_title} - {self.full_name}, дата рождения: {self.birth}'


class Manager(Employee):
    def __init__(self, full_name: str, birth: str):
        super().__init__(full_name, birth, job_title='Менеджер')

class Veterinarian(Employee):
    def __init__(self, full_name: str, birth: str):
        super().__init__(full_name, birth, job_title='Ветеринар')

    def treat_animal(self, animal):
        if isinstance(animal, animals.Animal):
            print(f'Ветеринар вылечил животное: {animal.species} по имени {animal.name}.')
        else:
            print('Ошибка аргумента. Объект не является животным.')


def test_employees():
    manager = Manager('Анна', '1991-10-11')
    print(manager.full_name)
    print(manager.job_title)
    print(manager.id)
    employee1 = Employee('Виталий', '2000-01-01', 'Сотрудник')
    print(employee1)
    veterinar = Veterinarian('Петр Сергеевич', '1980-05-15')
    print(veterinar)
    snake = animals.Reptile('Змея', 'Чуча', 2, 'сухопутная',
                    True, 'мышек', 'шшш-шш')
    veterinar.treat_animal(snake)
    veterinar.treat_animal(manager)


if __name__ == '__main__':
    test_employees()

