
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.__head = Node(data)
        self.__tail = self.__head

    def __iter__(self):
        node = self.__head
        while node is not None:
            yield node.data
            node = node.next

    def __str__(self):
        return f'[{", ".join(str(i) for i in self)}]'

    def append(self, elem):
        node = Node(elem)
        self.__tail.next = node
        self.__tail = node

    def get(self, index):
        node = self.__head
        i = 0
        while node is not None:
            if i == index:
                return node.data
            node = node.next
            i += 1

    def remove(self, index):
        node = self.__head
        left = self.__head
        right = self.__head
        i = 0
        while node is not None:
            if i == index - 1:
                left = node
                right = left.next.next
                break
            node = node.next
            i += 1
        left.next = right


my_list = LinkedList(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
