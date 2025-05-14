import doctest

class teacher:

    def __init__(self, surname: str = None, num_of_les_p_day: int = None):
        """
        Создание объекта класса "teacher":
        :param surname: фамилия преподавателя
        :param num_of_les_p_day: количество пар в день
        Пример:
        >>> teacher0 = teacher("Baranov", 3)
        """
        self.add_data(surname, num_of_les_p_day)

    def add_data(self, surname: str = None, num_of_les_p_day: int = None):
        """
        Добавление данных в объект:
        :param surname: фамилия преподавателя
        :param num_of_les_p_day: количество пар в день
        """
        self.surname = surname
        if num_of_les_p_day >= 0:
            self.num_of_les_p_day = num_of_les_p_day
        else:
            raise ValueError("Количество пар не может быть отрицательным")
        if num_of_les_p_day <= 5:
            self.num_of_les_p_day = num_of_les_p_day
        else:
            raise ValueError("Пощадите преподавателя, пожалуйста")

    def print_data(self):
        print(self.surname, self.num_of_les_p_day)



class student:

    def __init__ (self, surname: str = None, add_ses: int = 0, list_in_unik: bool = False):
        """
        Создание объета класса "student":
        :param surname: фамилия студента
        :param add_ses: количество допсессий у студента
        :param list_in_unik: числится ли в университете
        Пример:
        >>> student0 = student("Glazkov", 2, True)      # Инициализация объекта класса
        """
        self.add_data(surname, add_ses, list_in_unik)

    def add_data (self, surname: str = None, add_ses: int = 0, list_in_unik: bool = None):
        """
        Добавление данных в объект:
        :param surname: фамилия студента
        :param add_ses: количество допсессий у студента
        :param list_in_unik: числится ли в университете
        """
        self.surname = surname
        if add_ses >= 0:        # Студент не может иметь отрицательное количество допсессий
            self.add_ses = add_ses
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.list_in_unik = list_in_unik
        if self.add_ses > 5:        # Студент считается отчисленным, если количество допсесий больше 5
            self.list_in_unik = False

    def print_data(self):
        print(self.surname, self.add_ses, self.list_in_unik)



class dog:

    def __init__(self, name: str = None, age: int = None, breed: str = None):
        """
        Создание объекта класса "dog":
        :param name: имя собаки (str)
        :param age: возраст собаки (int)
        :param breed: порода собаки (str)
        Пример:
        >>> dog0 = dog("Peter", 11, "Husky")
        """
        self.add_data(name, age, breed)

    def add_data(self, name: str = None, age: int = None, breed: str = None):
        """
        Добавление данных в объект:
        :param name: имя собаки (str)
        :param age: возраст собаки (int)
        :param breed: порода собаки (str)
        """
        self.name = name
        if age >= 0:        # Возраст не может быть отрицательным
            self.age = age
        else:
            raise ValueError("Возраст не может быть отрицательным")
        self.breed = breed

    def print_data(self):
        print(self.name, self.age, self.breed)