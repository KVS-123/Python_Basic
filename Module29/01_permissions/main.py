import functools
from  collections.abc import Callable

user_permissions = ['admin']

def check_permission(user: str) -> Callable:
    def permission(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    return func()
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapped
    return permission

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
