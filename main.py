class RangeError(Exception):
    pass


def sorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, us, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if arr[middle] == us:
        return middle + 1
    elif us < arr[middle]:
        return binary_search(arr, us, left, middle - 1)
    else:
        return binary_search(arr, us, middle + 1, right)


try:
    list_ = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
    user = int(input("Введите целое число : "))

    print("Список до сортировки: ", list_)
    array = sorting(list_)
    print("Список после сортировки по возрастанию: ", array)

    if user > array[len(array) - 1] or user < array[0]:
        raise RangeError

    res = binary_search(array, user, 0, len(array) - 1)

    if res:
        print("Индекс введенного числа в списке: ", res - 1)
    else:
        a = 0
        while not res:
            res = binary_search(array, user - a, 0, len(array) - 1)
            a = a + 1
        print("Индекс числа меньше введённого: ", res - 1)

except RangeError:
    print(f"Число {user} не попадает в диапазон списка.")
    print("Программа завершена!")

except ValueError:
    print("Не корректные данные.")
    print("Программа завершена!")
