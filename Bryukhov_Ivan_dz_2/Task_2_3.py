# ****
def convert_list_in_str(list_in: list) -> str:
    result_str = ''
    for item in list_in:
        if item[-1] not in '0123456789':
            result_str += f'{item} '
        else:
            if len(item) == 1:
                result_str += f'"0{item}" '
            elif item[0] in '-+':
                if len(item[1:]) == 1:
                    result_str += f'"{item[0]}0{item[1:]}" '
                else:
                    result_str += f'"{item}" '
            else:
                result_str += f'"{item}" '
    return result_str


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
