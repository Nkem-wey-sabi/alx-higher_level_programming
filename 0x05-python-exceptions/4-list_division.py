#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''
    Divides the elements of 2 lists with the same index

    Parameters:
    my_list_1 (list): The first list
    my_list_2 (list): The second list
    list_length (int): The length of the items to divide

    Returns:
    A new list containing the result of the divisions
    '''
    my_list_res = []
    for i in range(list_length):
        res = 0
        try:
            a, b = (my_list_1[i], my_list_2[i])
            res = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_list_res.append(res)
    return my_list_res
