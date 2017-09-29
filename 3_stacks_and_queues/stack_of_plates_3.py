import StackModule as SM


class SetOfStacks:

    def __init__(self, limit):
        first_stack = SM.Stack()
        self.stacks = [first_stack]
        self.limit = limit

    def push(self, value):
        if self.stacks[-1].size < self.limit:
            self.stacks[-1].push(value)
        else:
            new_stack = SM.Stack(value)
            self.stacks.append(new_stack)

    def pop(self):
        if self.stacks[-1].isEmpty():
            return None
        return_value = self.stacks[-1].pop()
        if self.stacks[-1].size == 0:
            if len(self.stacks) != 1:
                del self.stacks[-1]
        return return_value

    def popAt(self, index):
        if index >= len(self.stacks):
            return None
        return_value = self.stacks[index].pop()
        if self.stacks[index].size == 0:
            if len(self.stacks) != 1:
                del self.stacks[index]
        return return_value

    def peek(self):
        return self.stacks[-1].pop()
