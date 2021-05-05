import math
from .data import Data
from decimal import Decimal


class Operation:

    def __init__(self, package: list, types: list):
        self.package = package
        self.types = types

    def factorial_porcentage(self, index):
        item = self.package[index]
        value = self.package[index - 1]

        if item == Data.FACTORIAL:
            value = self.__case_factorial(value)
        else:
            value = value / Decimal(100)

        self.package[index - 1] = value
        self.__delete(index, [0])

    def operator(self, index):
        item = self.package[index]
        valuea = self.package[index - 1]
        valueb = self.package[index + 1]

        if item == Data.POWER:
            valuea = Decimal.__pow__(valuea, valueb)
        elif item == Data.DIVISION:
            if valueb == Decimal(0):
                valuea = Decimal("Infinity")
            else:
                valuea = valuea / valueb
        elif item == Data.MULTIPLICATION:
            valuea = valuea * valueb
        elif item == Data.PLUS:
            valuea = valuea + valueb
        elif item == Data.MINUS:
            valuea = valuea - valueb

        self.package[index - 1] = valuea
        self.__delete(index, [1, 0])

    def variable_number(self, index):
        item = self.package[index]
        self.__delete(index, [1, -1])
        return item

    def function(self, index):
        item = self.package[index]
        value = self.package[index + 2]
        has_base = True if self.package[index + 3] == Data.SEMICOLON else False

        if item == Data.SIN:
            value = math.sin(value)
        elif item == Data.COS:
            value = math.cos(value)
        elif item == Data.TAN:
            value = math.tan(value)
        elif item == Data.CTG:
            value = 1 / math.tan(value)
        elif item == Data.SEC:
            value = 1 / math.cos(value)
        elif item == Data.CSC:
            value = 1 / math.sin(value)
        elif item == Data.ARC_SIN:
            value = math.asin(value)
        elif item == Data.ARC_COS:
            value = math.acos(value)
        elif item == Data.ARC_TAN:
            value = math.atan(value)
        elif item == Data.ARC_CTG:
            value = 1 / math.atan(value)
        elif item == Data.ARC_SEC:
            value = 1 / math.acos(value)
        elif item == Data.ARC_CSC:
            value = 1 / math.asin(value)
        elif item == Data.SIN_HYPER:
            value = math.sinh(value)
        elif item == Data.COS_HYPER:
            value = math.cosh(value)
        elif item == Data.TAN_HYPER:
            value = math.tanh(value)
        elif item == Data.CTG_HYPER:
            value = 1 / math.tanh(value)
        elif item == Data.SEC_HYPER:
            value = 1 / math.cosh(value)
        elif item == Data.CSC_HYPER:
            value = 1 / math.sinh(value)
        elif item == Data.ARC_SIN_HYPER:
            value = math.asinh(value)
        elif item == Data.ARC_COS_HYPER:
            value = math.acosh(value)
        elif item == Data.ARC_TAN_HYPER:
            value = math.atanh(value)
        elif item == Data.ARC_CTG_HYPER:
            value = 1 / math.atanh(value)
        elif item == Data.ARC_SEC_HYPER:
            value = 1 / math.acosh(value)
        elif item == Data.ARC_CSC_HYPER:
            value = 1 / math.asinh(value)
        elif item in Data.LOGARITHM_NATURAL:
            value = value.ln()
        elif item in Data.LOGARITHM:
            if has_base:
                base = self.package[index + 4]
                value = Decimal(math.log(value, base))
            else:
                value = Decimal.log10(value)
        elif item in Data.ROOT:
            if has_base:
                base = self.package[index + 4]
                value = Decimal.__pow__(value, Decimal(1)/base)
            else:
                value = Decimal.sqrt(value)
        elif item in Data.SUMMA:
            if has_base:
                base = self.package[index + 4]
                value2 = Decimal(0)
                for x in range(1, int(base) + 1, 1):
                    value2 += Decimal.__pow__(value, Decimal(x))
                value = value2
        elif item in Data.ABS:
            value = value.__abs__()
        elif item in Data.MOD:
            value2 = self.package[index + 4]
            value = value.__mod__(value2)

        self.package[index + 2] = Decimal(value)
        if has_base:
            self.__delete(index, [5, 4])
        self.__delete(index, [3, 1, 0])

    def __delete(self, index_base: int, indexes: list):
        for index in indexes:
            index = index_base + index
            self.package.pop(index)
            self.types.pop(index)

    def __case_factorial(self, value):
        if value < 0:
            return Decimal("Infinity")
        elif value == 0:
            return Decimal(1)
        else:
            return self.__case_factorial(value - 1) * value
