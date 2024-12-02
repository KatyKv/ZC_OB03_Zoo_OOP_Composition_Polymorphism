import animals
from animals import Bird, Mammal, Reptile
from employees import Employee, Manager, Veterinarian
from zoo import Zoo


def main():
    my_zoo = Zoo()

    print('Птички:')
    parrot = Bird('Попугай', 'Mark', 10, 110.5)
    crow = Bird('Ворона', 'Мила', '5.3', 70, 'Кааарррр')
    parrot.display_info()
    crow.display_info()

    print('\nМлекопитающие:')
    horse = Mammal('Лошадь', 'Маша', 7, 'траву', 'Иго-го!')
    dolphin = Mammal('Дельфин', 'Дэн', 3.4, 'рыбу', '', True)
    horse.display_info()
    dolphin.display_info()

    print('\nРептилии:')
    snake = Reptile('Змея', 'Чуча', 2, 'сухопутная',
                    True, 'мышек', 'шшш-шш')
    turtle = Reptile('Черепаха', 'Глаша', 10.111,
                     'полуводная', False, 'овощи')
    snake.display_info()
    turtle.display_info()

    print()
    manager1 = Manager('Анна', '1991-10-11')
    print(manager1)
    manager2 = Manager('Василиса', '1992-05-14')
    employee1 = Employee('Виталий', '2000-01-01', 'Сотрудник')
    print(employee1)
    employee2 = Employee('Виталий', '1980-03-30', 'Сотрудник')
    print(employee2)
    veterinar = Veterinarian('Петр Сергеевич', '1980-05-15')
    print(veterinar)
    veterinar.treat_animal(snake)

    print('\nДобавляем сотрудников и животных:')
    my_zoo.employee_list.append(manager1) # первого менеджера придется добавить вручную
    print(f'Менеджер {manager1.full_name} добавлен администратором системы')
    my_zoo.add_new_employee(manager1, manager2)
    my_zoo.add_new_employee(manager2, employee1)
    my_zoo.add_new_employee(manager1, employee2)
    my_zoo.add_new_employee(manager1, veterinar)
    my_zoo.add_new_animal(manager1, parrot)
    my_zoo.add_new_animal(manager1, snake)
    my_zoo.add_new_animal(manager2, crow)
    my_zoo.add_new_animal(manager1, horse)
    my_zoo.add_new_animal(manager2, turtle)
    my_zoo.add_new_animal(manager1, dolphin)

    print()
    animals.animal_sound(my_zoo.animals_list)

    print('\nУдаляем сотрудников и животных:')
    my_zoo.del_animal_by_species_and_name('Лошадь', 'Маша')
    my_zoo.del_animal_by_species_and_name('Лошадь', 'Маша')
    my_zoo.del_employee_by_fullname('Виталий')
    my_zoo.del_employee_by_id(4)
    my_zoo.employee_info()




if __name__ == '__main__':
    main()