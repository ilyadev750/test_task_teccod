def return_unique_list(my_list):
    new_set = set(my_list)
    new_list = list(new_set)
    return sorted(new_list)


def return_list_of_prime_numbers(start, end):
    prime_list = []
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return 'Введенные значения должны быть числами и не содержать букв'
    if end < start:
        return 'Конечное значение не может быть больше начального'
    for i in range(start, end+1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                prime_list.append(i)
    return prime_list


def sorted_list_by_string(my_list, reverse):
    my_list = sorted(my_list, key=lambda x: len(x), reverse=reverse)
    return my_list
