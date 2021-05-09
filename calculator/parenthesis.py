class Parenthesis:
    SPECIAL = "special"
    NORMAL_SPECIAL = "normal_special"
    NORMAL = "normal"

    def __init__(self):
        self.__types = []
        self.__checks = []
        self.type = Parenthesis.NORMAL

    def open(self):
        if self.type == Parenthesis.SPECIAL:
            self.__types.append(self.type)
            self.__checks.append(True)
        elif self.type == Parenthesis.NORMAL_SPECIAL:
            self.__checks.append(True)
            self.__types.append(self.type)
        elif self.type == Parenthesis.NORMAL:
            self.__checks.append(False)
            self.__types.append(self.type)

    def close(self):
        exists_error = True
        if len(self.__types) > 0:
            value = self.__types.pop()
            check = self.__checks.pop()
            if not check and value == Parenthesis.SPECIAL:
                exists_error = False
            elif value != Parenthesis.SPECIAL:
                exists_error = False
        return exists_error

    def check_semicolon(self):
        index = len(self.__types)
        exists_error = True

        if index > 0:
            index = index - 1
            value = self.__types[index]
            if value != Parenthesis.NORMAL:
                self.__checks[index] = False
                exists_error = False

        return exists_error

    def is_concluded(self) -> (bool, str):
        concluded = Parenthesis.SPECIAL not in self.__types
        value = 0
        if concluded:
            value = len(self.__types)
        return concluded, value
