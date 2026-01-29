import math

def get_sage_sqrt(num):
    try:
        res = math.sqrt(num)

    except ValueError:
        return 'число не может быть отрицательным'

    except Exception as exc:
        with open('error.txt', 'w', encoding='UTF-8') as exc_list:
            exc_list.write(f'-{exc}')
            return exc
    else:
        return res


numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
