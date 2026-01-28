skate_sizes = []
foot_sizes = []
couples = 0

skate_count = int(input('Кол-во коньков: '))
for i_num in range(skate_count):
    print('Размер', str(i_num + 1) + '-й пары:', end=' ')
    skate = int(input())
    skate_sizes.append(skate)
print()

people_count =int(input('Кол-во людей: '))
for i_num in range(people_count):
    print('Размер ноги', str(i_num + 1) + '-го человека:', end=' ')
    foot = int(input())
    foot_sizes.append(foot)
print()

for i_el in foot_sizes:
    if skate_sizes.count(i_el) != 0:
        couples += 1
        skate_sizes.remove(i_el)

print('Наибольшее кол-во людей, которые могут взять ролики:', couples)
