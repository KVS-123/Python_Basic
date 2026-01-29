from typing import Callable
import functools

def decorator_with_args_for_any_decorator(decorator_func: Callable) -> Callable:
    def wrapped(*args, **kwargs) -> Callable:
        def wrapped_in(func: Callable) -> Callable:
            print('Переданные арги и кварги в декоратор:', args, kwargs)
            return decorator_func(func, *args, **kwargs)
        return wrapped_in
    return wrapped

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrapped(*f_args, **f_kwargs):
        return func(*f_args, **f_kwargs)
    return wrapped

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)