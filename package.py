from data import Data


class Package:

    VARIABLE = "variable"
    NUMBER = "number"
    OPERATOR = "operator"
    FACTORIAL = "factorial"
    PORCENTAGE = "porcentage"
    FUNCTION = "function"
    SEMICOLON = "semicolon"
    OPENED = "opened"
    CLOSED = "closed"

    def __init__(self):
        self.__function = []
        self.__types = []
        pass

    def add_variable(self, value):
        self.__function.append(value)
        self.__types.append(Package.VARIABLE)

    def add_number(self, value):
        self.__function.append(value)
        self.__types.append(Package.NUMBER)

    def add_operator(self, value):
        self.__function.append(value)
        self.__types.append(Package.OPERATOR)

    def add_factorial(self, value):
        self.__function.append(value)
        self.__types.append(Package.FACTORIAL)

    def add_porcentage(self, value):
        self.__function.append(value)
        self.__types.append(Package.PORCENTAGE)

    def add_function(self, value):
        self.__function.append(value)
        self.__types.append(Package.FUNCTION)

    def add_semicolon(self, value):
        self.__function.append(value)
        self.__types.append(Package.SEMICOLON)

    def add_opened(self, value):
        self.__function.append(value)
        self.__types.append(Package.OPENED)

    def add_closed(self, value):
        self.__function.append(value)
        self.__types.append(Package.CLOSED)

    def get(self) -> list:
        index = 0
        while index < len(self.__function):
            type_value = self.__types[index]
            value = self.__function[index]
            if value in [Data.PLUS, Data.MINUS]:
                self.__case_sign(index)
            elif type_value == Package.VARIABLE:
                self.__case_variable(index)
            elif type_value == Package.FUNCTION:
                self.__case_function(index)
            elif type_value == Package.NUMBER:
                self.__case_number(index)
            elif type_value == Package.OPENED:
                self.__case_opened(index)
            index = index + 1

        return self.__function

    def get_types(self) -> list:
        return self.__types

    def __get(self, index):
        value = None
        if index >= 0:
            value = self.__function[index]
        return value

    def __get_type(self, index):
        value = None
        if index >= 0 and len(self.__types) > index:
            value = self.__types[index]
        return value

    def __case_sign(self, index):
        old_type = self.__get_type(index - 1)
        next_type = self.__get_type(index + 1)
        next_next_type = self.__get_type(index + 2)

        if old_type in [None, Package.OPENED, Package.SEMICOLON]:
            self.__function.insert(index, "0")
            self.__types.insert(index, Package.NUMBER)
        elif old_type in [Package.OPERATOR]:
            if next_type in [Package.NUMBER, Package.VARIABLE]:
                self.__function.insert(index, Data.PARENTHESIS_OPENED)
                self.__types.insert(index, Package.OPENED)

                self.__function.insert(index + 1, "0")
                self.__types.insert(index + 1, Package.NUMBER)

                if next_next_type in [Package.FACTORIAL, Package.PORCENTAGE]:
                    self.__function.insert(index + 5, Data.PARENTHESIS_CLOSED)
                    self.__types.insert(index + 5, Package.CLOSED)
                else:
                    self.__function.insert(index + 4, Data.PARENTHESIS_CLOSED)
                    self.__types.insert(index + 4, Package.CLOSED)
            else:
                self.__function.insert(index, Data.PARENTHESIS_OPENED)
                self.__types.insert(index, Package.OPENED)
                self.__function.insert(index + 1, "0")
                self.__types.insert(index + 1, Package.NUMBER)

                # el siguiente parentesis abierto
                i = index + 1
                if next_type == Package.FUNCTION:
                    i = index + 4
                elif next_type == Package.OPENED:
                    i = index + 3

                parenthesis = 0

                # Ubicar el indice para insertar el parentesis
                while i < len(self.__types):
                    current_type = self.__types[i]
                    if current_type == Package.OPENED:
                        parenthesis = parenthesis + 1
                    elif current_type == Package.CLOSED:
                        parenthesis = parenthesis - 1
                    if parenthesis == 0:
                        break
                    i = i + 1
                    pass
                self.__function.insert(i, Data.PARENTHESIS_CLOSED)
                self.__types.insert(i, Package.CLOSED)
                pass
            pass
        pass

    def __case_variable(self, index):
        old_type = self.__get_type(index - 1)
        if old_type in [Package.CLOSED,
                        Package.VARIABLE,
                        Package.NUMBER,
                        Package.FACTORIAL,
                        Package.PORCENTAGE]:
            self.__function.insert(index, Data.MULTIPLICATION)
            self.__types.insert(index, Package.OPERATOR)

    def __case_function(self, index):
        self.__case_variable(index)

    def __case_number(self, index):
        self.__case_variable(index)

    def __case_opened(self, index):
        self.__case_variable(index)
