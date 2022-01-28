# Задание 1a: Создаем алгоритм для суммы чисел из списка, состоящего из кубов нечётных чисел от 1 до 1000
# Сумма цифр которох делится на 7 нацело
def sum_list_1(dataset: list) -> int:
    result_sum1 = 0
    for num in dataset:
        my_sum = 0
        while num > 0:
            digit = num % 10
            my_sum += digit
            num = num // 10
        if my_sum % 7 == 0:
            result_sum1 += my_sum
    return result_sum1


# Задание b и с: К каждому элемента списка добавили 17 и заново вычислили сумму чисел из этого списка
# Условие добавлено и задания C* (Не создавая новый список)
def sum_list_2(dataset: list) -> int:
    result_sum2 = 0
    for num in dataset:
        my_sum = 0
        num += 17
        while num > 0:
            digit = num % 10
            my_sum += digit
            num = num // 10
        if my_sum % 7 == 0:
            result_sum2 += my_sum
    return result_sum2


# Создаем список, состоящий из кубов нечётных чисел от 1 до 1000
my_list = [x ** 3 for x in range(1, 1001, 2)]

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
