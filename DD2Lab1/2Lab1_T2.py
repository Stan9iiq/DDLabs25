from task import *

teacher0 = teacher("Baranov", 3)
student0 = student("Glazkov", 2, True)
dog0 = dog("Peter", 11, "Husky")

if __name__ == "__main__":

    try:
        teacher0.add_data(..., 7)
    except:
        print('Ошибка: неправильные данные, некорректное количество пар')

    try:
        student0.add_data(..., ..., -4)
    except:
        print('Ошибка: неправильные данные, на входе только bool')

    try:
        dog0.add_data(1, ..., ...)
    except:
        print('Ошибка: неправильные данные, напишите имя буквами')
