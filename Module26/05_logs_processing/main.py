import os


def error_log_generator(path):
    with open(path, 'r', encoding='utf8') as error_log:
        for line in error_log:
            if line.startswith('ERROR'):
                yield line


input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
output_file_path = os.path.abspath(os.path.join('data', 'output.txt'))

with open(output_file_path, 'w') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")
