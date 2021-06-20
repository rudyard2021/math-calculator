from .package import Package
from .data import Data


class Simulator:

    def __init__(self, package: list, types: list):
        self.package = package.copy()
        self.types = types.copy()
        self.process = []

    def get_process(self) -> list:
        next = True
        while(next):
            next = self.__simulate()
        return self.process

    def __get_type(self, index):
        value = None
        if index >= 0 and len(self.types) > index:
            value = self.types[index]
        return value

    def __simulate(self) -> bool:
        start_index, end_index = self.__get_parenthesis_indexes()
        operators_indexes = self.__get_operators_indexes(
            self.package[start_index:end_index])
        length = len(operators_indexes)

        for index in range(length):
            operator_index = operators_indexes[index] + start_index
            self.process.append(operator_index)
            type_package = self.__get_type(operator_index)

            if type_package in [Package.FACTORIAL, Package.PERCENTAGE]:
                self.__delete(operator_index, [0])
                self.__index_again(operators_indexes, index, 1)

            elif type_package == Package.OPERATOR:
                self.__delete(operator_index, [1, 0])
                self.__index_again(operators_indexes, index, 2)
                pass
            pass

        type_package = self.__get_type(start_index)
        type_package_old = self.__get_type(start_index - 1)
        if type_package_old == Package.FUNCTION:
            type_package_next_next = self.__get_type(start_index + 2)
            if type_package_next_next == Package.SEMICOLON:
                self.__delete(start_index, [4, 3, 2, 0, -1])
                self.process.append(start_index - 1)
            else:
                self.__delete(start_index, [2, 0, -1])
                self.process.append(start_index - 1)
            pass
        elif type_package == Package.OPENED:
            self.__delete(start_index, [2, 0])
            self.process.append(start_index + 1)
            pass

        next = True
        if len(self.package) == 1:
            next = False
        return next

    def __delete(self, index_base: int, indexes: list):
        for index in indexes:
            index = index_base + index
            self.package.pop(index)
            self.types.pop(index)

    def __index_again(self, operators_indexes: list, index, count_deleted):
        length = len(operators_indexes)
        operator_index = operators_indexes[index]
        while index < length:
            value = operators_indexes[index]
            if value > operator_index:
                operators_indexes[index] = value - count_deleted
            index = index + 1

    def __get_operators_indexes(self, package: list) -> list:
        indexes = self.__get_indexes(
            [Data.FACTORIAL, Data.PERCENTAGE], package)

        temp = self.__get_indexes_back([Data.POWER], package)
        indexes.extend(temp)

        temp = self.__get_indexes([Data.DIVISION], package)
        indexes.extend(temp)

        temp = self.__get_indexes([Data.MULTIPLICATION], package)
        indexes.extend(temp)

        temp = self.__get_indexes([Data.PLUS, Data.MINUS], package)
        indexes.extend(temp)

        return indexes

    def __get_indexes(self, values: list, package: list) -> list:
        length = len(package)
        index = 0
        indexes = []

        while index < length:
            item = package[index]
            for value in values:
                if item == value:
                    indexes.append(index)
                    break
                pass
            index = index + 1
            pass
        return indexes

    def __get_indexes_back(self, values, package: list) -> list:
        index = len(package) - 1
        indexes = []

        while index >= 0:
            item = package[index]
            for value in values:
                if item == value:
                    indexes.append(index)
                    break
                pass
            index = index - 1
            pass
        return indexes

    def __get_parenthesis_indexes(self) -> (int, int):
        opened_index = 0
        closed_index = len(self.package)

        try:
            index = self.types.index(Package.CLOSED)
            closed_index = index + 1
            while index >= 0:
                item = self.types[index]
                if item == Package.OPENED:
                    opened_index = index
                    break
                index = index - 1
        except Exception:
            pass
        return opened_index, closed_index
