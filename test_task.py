def return_unique_list(my_list):
    new_set = set(my_list)
    new_list = list(new_set)
    return sorted(new_list)


def return_list_of_prime_numbers(start, end):
    prime_list = []
    if end < start:
        return 'Конечное значение не может быть больше начального'
    for i in range(start, end+1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                prime_list.append(i)
    return prime_list


def sorted_list_by_string(my_list):
    my_list = sorted(my_list, key=lambda x: len(x), reverse=True)
    return my_list




# d = ['1', '32434ww', '233', '2222', '45345435656456', '4432asd', '36546awd', '23', '333', '666']
# f = sorted_list_by_string(d)
# print(f)