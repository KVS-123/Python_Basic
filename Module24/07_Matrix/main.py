class Matrix:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = [[0 for _ in range(col)] for _ in range(row)]

    def print_matrix(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.data[i][j], end='\t\t')
            print()

    def add(self, matrix):
        data = list()
        for i in range(self.row):
            new_data = list()
            for j in range(self.col):
                try:
                    new_data.append(self.data[i][j] + matrix.data[i][j])
                except IndexError:
                    continue
            data.append(new_data)
        new_matrix = Matrix(len(data), len(data[0]))
        new_matrix.data = data
        new_matrix.print_matrix()

    def subtract(self, matrix):
        data = list()
        for i in range(self.row):
            new_data = list()
            for j in range(self.col):
                try:
                    new_data.append(self.data[i][j] - matrix.data[i][j])
                except IndexError:
                    continue
            data.append(new_data)
        new_matrix = Matrix(len(data), len(data[0]))
        new_matrix.data = data
        new_matrix.print_matrix()

    def multiply(self, matrix):
        if self.col != matrix.row:
            raise ValueError(
                "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения")
        new_matrix = Matrix(self.row, matrix.col)
        for i in range(self.row):
            for j in range(matrix.col):
                for k in range(self.col):
                    new_matrix.data[i][j] += self.data[i][k] * matrix.data[k][j]
        new_matrix.print_matrix()

    def transpose(self):
        resul = list()
        for i in range(self.col):
            list_in = list()
            for j in range(self.row):
                list_in.append(self.data[j][i])
            resul.append(list_in)
        self.row, self.col = self.col, self.row
        self.data = resul
        self.print_matrix()


m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]
#
print("Матрица 1:")
m1.print_matrix()

print("Матрица 2:")
m2.print_matrix()

print("Сложение матриц:")
m1.add(m2)

print("Вычитание матриц:")
m1.subtract(m2)

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
m1.multiply(m3)

print("Транспонирование матрицы 1:")
m1.transpose()
