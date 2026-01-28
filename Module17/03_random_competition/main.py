import random

team_1 = [random.randint(500, 1000) / 100 for _ in range(20)]
team_2 = [random.randint(500, 1000) / 100 for _ in range(20)]
winners = [(team_1[i] if team_1[i] > team_2[i] else team_2[i]) for i in range(20)]
print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', winners)


