import employees
import animals


class Zoo:
    def __init__(self):
        self.animals_list = []
        self.employee_list = []

    def employee_info(self, job_title: str = None):
        if job_title:
            for employee in self.employee_list:
                if employee.job_title == job_title:
                    print(employee.__str__())
        else:
            print('Список сотрудников:')
            for employee in self.employee_list:
                print(employee.__str__())

    def animal_info(self, animal_species: str = None):
        if animal_species:
            for animal in self.animals_list:
                if animal.species == animal_species:
                    print(animal.name, '\n')
        else:
            for animal in self.animals_list:
                print(animal.name, '\n')

    def add_new_animal(self, manager, animal):
        if not isinstance(manager, employees.Manager) or manager not in self.employee_list:
            print('Ошибка: добавлять животных может только менеджер зоопарка')
        elif not isinstance(animal, animals.Animal):
            print('Ошибка аргумента: добавляемый объект не является животным')
        elif animal in self.animals_list:
            print(f'Животное: {animal.species} {animal.name} ранее уже было добавлено в зоопарк.')
        else:
            self.animals_list.append(animal)
            print(f'Животное: {animal.species} {animal.name} - добавлено в список животных зоопарка')

    def add_new_employee(self, manager, employee):
        if not isinstance(manager, employees.Manager) or manager not in self.employee_list:
            print('Ошибка: добавлять сотрудников может только менеджер зоопарка')
        elif not isinstance(employee, employees.Employee):
            print('Ошибка аргумента: добавляемый объект не является сотрудником')
        else:
            self.employee_list.append(employee)
            print(f'Сотрудник: {employee.job_title} {employee.full_name} - добавлен в список сотрудников зоопарка')

    def del_animal_by_id(self, animal_id):
        deleted = False
        for animal in self.animals_list:
            if animal.id == animal_id:
                self.animals_list.remove(animal)
                deleted = True
                print(f'Из списка удалено животное вида {animal.species} '
                      f'по имени {animal.name} с идентификатором {animal.id}')
                break
        if not deleted:
            print(f'В списке не найдено животное с идентификатором {animal_id}')

    def del_animal_by_species_and_name(self, species, name):
        id_list = []
        for animal in self.animals_list:
            if animal.species == species and animal.name == name:
                id_list.append(animal.id)
        if len(id_list) == 0:
            print(f'В списке отсутствует животное вида {species} по имени {name}')
        elif len(id_list) == 1:
            self.del_animal_by_id(id_list[0])
        else:
            print(f'В списке несколько животных вида {species} по имени {name}. Удалите животное по ID.')
            print(f'ID животных: {id_list}')

    def del_employee_by_id(self, employee_id):
        deleted = False
        for employee in self.employee_list:
            if employee.id == employee_id:
                self.employee_list.remove(employee)
                deleted = True
                print(f'Из списка удален сотрудник {employee.full_name} '
                      f'с идентификатором {employee.id}')
                break
        if not deleted:
            print(f'В списке не найден сотрудник с идентификатором {employee_id}')

    def del_employee_by_fullname(self, fullname):
        id_list = []
        for employee in self.employee_list:
            if employee.full_name == fullname:
                id_list.append(employee.id)
        if len(id_list) == 0:
            print(f'В списке отсутствует сотрудник по имени {fullname}')
        elif len(id_list) == 1:
            self.del_employee_by_id(id_list[0])
        else:
            print(f'В списке несколько сотрудников с именами: {fullname}. Удалите сотрудника по ID.')
            print(f'ID сотрудников с именем {fullname}: {id_list}')







