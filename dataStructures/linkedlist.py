from hashlib import new


class Node:
    def __init__(self, data, node) -> None:
        self.data = data
        self.next = node

    def __init__(self, data) -> None:
        self.data = data
    
    def __repr__(self) -> str:
        return "Data:  {}".format(self.data)

    def __str__(self) -> str:
        return self.__repr__()

class LinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def __repr__(self) -> str:
        return "Head:  {}".format(self.head)

    def __str__(self) -> str:
        return self.__repr__()


if __name__ == "__main__":
    n = Node(9)
    l = LinkedList(n)
    print(l)