import math as m

def math_function1(x, y, a, b):
    try:
        numerator = pow((8 + m.fabs(x - y) ** 3), 1/3) # числитель 
        denominator = m.sqrt(x ** 2 + a * b * y) + 1 # знаменатель
        first_part = numerator / denominator #первая часть выражения

        assert x > 0 # если логарифм меньше нуля 
        assert pow((8 + m.fabs(x - y) ** 3), 1/3) > 0 # если выражение корня меньше 0
        assert (x ** 2 + a * b * y) > 0 # если выражение корня меньше 0 

        second_part = 0.05 * m.log10(x) # вторая часть выражения 
        a = first_part + second_part
        return a
    
    except AssertionError:
        print("Ошибка: Такого числа не существует")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
    except ValueError:
        print("Ошибка: Невозможно вычислить квадратный корень из отрицательного числа.")
    except TypeError: 
        print('Ошибка: Использован не тот тип данных')
    except:
        print ("Неизвестная ошибка")



def math_function2(x, y, k):
    try:
        e = m.exp(-k * x)

        first_part = e*(1 + m.cos(x**3))**2 #первая часть
        second_part = m.tan(y)**2 # вторая часть 
        b = first_part + second_part
        return b
    
    except ValueError:
        print("Ошибка: Невозможно вычислить квадратный корень из отрицательного числа.")
    except TypeError: 
        print('Ошибка: Использован не тот тип данных')
    except:
        print("Неизвестная ошибка.")

print (math_function1(20,2,0,1))

print (math_function1(20,"n",0,1))

print (math_function1(0,0,0,0))

print(math_function2(0,2,-2))