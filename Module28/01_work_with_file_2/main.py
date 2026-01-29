
class File:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        try:
            self.file = open(self.name, 'r')
        except FileNotFoundError:
            self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('file_name') as f:
    if f.mode == 'r':
        print('Открыли')
    elif f.mode == 'w':
        print('Создали')
