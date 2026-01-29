
class Cell:
    def __init__(self, number):
        self.number = number
        self.occupied = number+1


class Board:
    cell_list = list()

    def create_board(self):
        self.cell_list = list()
        for row in range(3):
            self.cell_list.append([Cell(0 + 3*row), Cell(1 + 3*row), Cell(2 + 3*row)])

    def print_board(self):
        for row in range(3):
            print('     |' * 3)
            for line in range(3):
                print(f'  {self.cell_list[row][line].occupied}  |', end='')
            print()
            print('     |' * 3)
            print('-' * 18)


class Player:
    cell_occupied = str()

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    board = Board()
    first_score = 0
    second_score = 0

    def __init__(self, name1, name2):
        self.first = Player(name1, 'X')
        self.second = Player(name2, 'O')

    def toright(self, player):
        for i in range(3):
            if str(self.board.cell_list[i][i].number) not in player.cell_occupied:
                return False
        return True

    def toleft(self, player):
        for i in range(3):
            if str(self.board.cell_list[i][2 - i].number) not in player.cell_occupied:
                return False
        return True

    def row(self, player):
        for row in range(3):
            for line in range(3):
                if str(self.board.cell_list[row][line].number) not in player.cell_occupied:
                    break
            else:
                return True
        return False

    def line(self, player):
        for line in range(3):
            for row in range(3):
                if str(self.board.cell_list[row][line].number) not in player.cell_occupied:
                    break
            else:
                return True
        return False

    def win(self, player):
        if self.toright(player) or self.toleft(player) or self.row(player) or self.line(player):
            self.board.print_board()
            return True
        return False

    def move(self, player):
        self.board.print_board()
        cell_num = int(input(f'{player.name} введите номер клетки: ')) - 1
        player.cell_occupied += str(cell_num)
        for el in self.board.cell_list:
            for cell in el:
                if cell_num == cell.number:
                    self.board.cell_list[self.board.cell_list.index(el)][el.index(cell)].occupied = player.symbol
                    break
        return self.win(player)

    def start_game(self):
        self.board.create_board()
        count = 1
        while count != 10:
            if count % 2 != 0:
                count += 1
                if self.move(self.first):
                    return 1
            else:
                count += 1
                if self.move(self.second):
                    return 2
        else:
            self.board.print_board()
            return 3

    def play(self):
        result = self.start_game()
        if result == 1:
            print(f'{self.first.name} победил')
            self.first_score += 1
        elif result == 2:
            print(f'{self.second.name} победил')
            self.second_score += 1
        else:
            print('Ничья!')
        print(f'Ваш счет: {self.first_score}:{self.second_score}')
        answer = int(input('Вы хотите продолжить? 1-да, 2-нет '))
        if answer == 1:
            self.first.cell_occupied = str()
            self.second.cell_occupied = str()
            self.play()


name_1 = input('Введите имя первого игрока: ')
name_2 = input('Введите имя второго игрока: ')
Game(name_1, name_2).play()


# нет ничьей