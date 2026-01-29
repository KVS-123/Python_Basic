from datetime import datetime
import functools
from collections.abc import Callable

def correct_format(format: str) -> str:
    char = 'bymdYHMSAB'
    cor_for = ''
    for i in format:
        if i in char:
            cor_for += '%' + i
        else:
            cor_for += i
    return cor_for

def log(func: Callable, format: str, class_name: str) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print(f'- Запускается {class_name}.{func.__name__}. Дата и время запуска: {datetime.now().strftime(correct_format(format))}')
        start = datetime.now()
        result = func(*args, **kwargs)
        time = datetime.now() - start
        print(f'- Завершение {class_name}.{func.__name__}, время работы = {round(time.total_seconds(), 3)}s')
        return result
    return wrapped

def log_methods(format: str) -> Callable:
    def decorate(cls):
        for i_methods in dir(cls):
            if i_methods.startswith('__') is False:
                decorate_method = log(getattr(cls, i_methods), format, cls.__name__)
                setattr(cls, i_methods, decorate_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
