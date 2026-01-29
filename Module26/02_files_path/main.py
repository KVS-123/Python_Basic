import os

def gen_files_path(f):
    for links, dirs, files in list(os.walk(f)):
        for file in files:
            yield links + os.sep + file


folder = os.path.abspath(os.path.join('..'))
print(folder)
path = gen_files_path(folder)
for i in path:
    print(i)
