from collections.abc import Callable

app = dict()

def callback(path: str) -> Callable:
    def decorator(func: Callable) -> None:
        app[path] = func
    return decorator

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

