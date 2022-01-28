# Содаём алгоритм для склонения слова 'Процент' для исел до 100.
def transform_string(number: int) -> str:
    if number in range(10, 21):
        return f'{number} процентов'
    elif number % 10 == 1:
        return f'{number} процент'
    elif number % 10 in range(2, 5):
        return f'{number} процента'
    else:
        return f'{number} процентов'


for n in range(1, 101):
    print(transform_string(n))
