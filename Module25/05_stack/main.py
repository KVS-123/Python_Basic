
class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return len(self.stack) == 0

    def add(self, el):
        self.stack.append(el)

    def delete(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def take(self):
        if self.is_empty():
            return None
        return self.stack[-1]


class TaskManager:
    def __init__(self):
        self.task_list = Stack()

    def new_task(self, task, priority):
        self.task_list.add((task, priority))

    def delete_task(self, task):
        new_stack = Stack()
        removed = False
        while not self.task_list.is_empty():
            cur_task = self.task_list.delete()
            if cur_task[0] != task:
                new_stack.add(cur_task)
            else:
                removed = True

        while not new_stack.is_empty():
            self.task_list.add(new_stack.delete())

        if not removed:
            print('Такого задания нет!')

    def __str__(self):
        priority_dict = dict()
        result = list()
        for task, priority in sorted(self.task_list.stack, key=lambda x: x[1], reverse=True)[::-1]:
            if priority in priority_dict:
                priority_dict[priority].insert(0, task)
            else:
                priority_dict[priority] = [task]

        for p in priority_dict.keys():
            result.append(f'{p} {"; ".join(priority_dict[p])}')
        return "\n".join(result)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

print('\nРезультат после удаления одного из заданий:')
manager.delete_task('помыть посуду')
print(manager)
