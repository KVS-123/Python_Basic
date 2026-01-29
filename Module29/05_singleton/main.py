import functools
from collections.abc import Callable

def singleton(cls) -> Callable:
    instance = dict()
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapped

@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
