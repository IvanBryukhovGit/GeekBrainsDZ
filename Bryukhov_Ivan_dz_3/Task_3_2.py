# *(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv(): реализовать корректную
# работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.


def num_translate_adv(num: str) -> str:
    dictionary = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if num.lower() in dictionary.keys():
        value = dictionary[num.lower()]
        if num == num.capitalize():
            return value.capitalize()
        return value


print(num_translate_adv("One"))
print(num_translate_adv("two"))
print(num_translate_adv("One"))
print(num_translate_adv("two"))
