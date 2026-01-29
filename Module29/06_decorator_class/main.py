import time
from collections.abc import Callable

def LoggerDecorator(func: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print('Аргументы:', args, kwargs)
        print('Результат:', result)
        print('Время выполнения:', execution_time, 'секунд')
        return result
    return wrapped

@LoggerDecorator
def complex_algorithm(arg1, arg2):
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


result = complex_algorithm(10, 50)