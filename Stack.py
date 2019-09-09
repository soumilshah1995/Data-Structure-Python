
""""
FIFO
"""

class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, item = ''):

        """

        :param item: Accepts item as Parameter
        :return: None
        """
        self.item.append(item)
        pass

    def pop(self):
        """
        This will remove Last item
        :return: None
        """
        self.item.pop()
        pass

    def peek(self):
        """
        Allows us to see the Last elements
        :return: Last item
        """
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):

        """
        tells Whether the stack is Empty or not
        :return: Bool Value
        """
        if self.item == []:
            return True
        else:
            return False

if __name__ == "__main__":
    stack = Stack()

    stack.push("1")
    stack.push('2')
    print(stack.size())
    print(stack.peek())


    stack.pop()
    print(stack.size())
    print(stack.peek())

    print(stack.isempty())










