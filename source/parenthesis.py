class Input:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.count = 1

    def next(self):
        self.count = self.count + 1
        if self.count > self.max:
            return False
        return True

class Parenthesis:

    def __init__(self):
        self.__inputs = []
        self._input = Input(1, 1)

    def input(self, min=1, max=1):
        self._input = Input(min, max)

    def open(self):
        self.__inputs.append(self._input)

    def close(self):
        exists_error = True
        if len(self.__inputs) > 0:
            input = self.__inputs.pop()
            if input.min <= input.count <= input.max:
                exists_error = False
        return exists_error

    def check_semicolon(self):
        index = len(self.__inputs)
        exists_error = True

        if index > 0:
            index = index - 1
            input = self.__inputs[index]
            if input.next():
                exists_error = False
        return exists_error

    def is_concluded(self) -> (bool, str):
        concluded = True
        for input in self.__inputs:
            if input.count < input.min:
                concluded = False
                break

        value = 0
        if concluded:
            value = len(self.__inputs)
        return concluded, value
