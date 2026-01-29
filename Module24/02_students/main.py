class Student:
    def __init__(self, surname, name, group_number, grades):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.grades = grades

    def get_gpa(self):
        gpa = 0
        for el in self.grades:
            gpa += int(el)
        gpa /= 5
        return gpa


stud_count = int(input('Введите количество студентов: '))
stud_list = dict()
for _ in range(stud_count):
    inf = input('\nВведите фамилию, имя и номер группы: ').split()
    gr = input('Введите ваши оценки через пробел: ').split()
    stud = Student(inf[0], inf[1], inf[2], gr)
    stud_list[f'{stud.surname} {stud.name} {stud.group_number}'] = stud.get_gpa()

for i in sorted(stud_list.items(), key=lambda para: para[1], reverse=True):
    print(i[0], i[1])
