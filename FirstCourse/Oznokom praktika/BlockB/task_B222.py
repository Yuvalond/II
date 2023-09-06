# Написать функцию sum_of_fractions, которая получает вещественное число и возвращает строку - сумму слагаемых числа в виде дробей. 
# Между слагаемыми поставить символ +, все отделить пробелами 
#
# Примеры:
# sum_of_fractions(1.24) ==> '1 + 2/10 + 4/100'

import traceback
import decimal as d

def sum_of_fractions(number):
    # Получаем целую часть
    kol_vo_num_fract = d.Decimal(str(number)).as_tuple().exponent*(-1)
    whole_part = int(number)
    # и дробную часть числа
    fractional_part = float(number) - whole_part
    fractional_part = round(fractional_part,kol_vo_num_fract)
    
    # Преобразуем дробную часть в список цифр
    fraction_digits = [int(digit) for digit in str(fractional_part)[2:]]
    
    # Создаем список дробей и вычисляем кусок числа в виде дроби деленной на 10,100...
    fractions = []
    for i in range(1, len(fraction_digits) + 1):
        denominator = 10 ** i #знаменатель
        numerator = fraction_digits[i - 1] #числитель 
        if numerator > 0: # если числитель = 0 игнорируем
            fractions.append(f'{numerator}/{denominator}')
    
    # Соединяем целую часть и дроби в одну строку
    if whole_part == 0:
        return f'{" + ".join(fractions)}'
    else:
        return f'{str(whole_part)+" +"} {" + ".join(fractions)}'
# Тесты
try:
    assert sum_of_fractions(1.24) == '1 + 2/10 + 4/100'
    assert sum_of_fractions(7.304) == '7 + 3/10 + 4/1000'
    assert sum_of_fractions(0.04) == '4/100'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")