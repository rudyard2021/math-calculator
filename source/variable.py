import math
from decimal import Decimal

from .package import Package
from .data import Data


class Variable:

    def __init__(self, package: list, types: list):
        self.package = package.copy()
        self.types = types.copy()
        self.variables = {}
        self.__set_pi()
        self.__set_euler()

    def __set_pi(self):
        for pi in Data.PI:
            self.variables[pi] = Decimal(math.pi)

    def __set_euler(self):
        for euler in Data.EULER:
            self.variables[euler] = Decimal(math.e)

    def __clean_variables(self, values) -> dict:
        variables = {}
        type_name = type(values).__name__

        if type_name == "list":
            for item in values:
                items = str.split(item, "=")
                variable = items[0].strip()
                value = Decimal(0) if len(items) == 1 else items[1].strip()
                variables[variable] = value
        elif type_name == "dict":
            for variable in values.keys():
                value = values[variable]
                variables[variable] = value

        return variables

    def __load(self, values):
        variables = self.variables.copy()
        package = self.package.copy()
        values = self.__clean_variables(values)

        for variable in values.keys():
            value = values[variable]
            variables[variable] = value

        length = len(package)
        for index in range(length):
            item_type = self.types[index]
            if item_type == Package.NUMBER:
                item = package[index]
                package[index] = Decimal(item)
            elif item_type == Package.VARIABLE:
                item = package[index]
                package[index] = self.__get(variables, item)
                pass
            pass
        return package

    def __get(self, variables: dict, item: str):
        value = Decimal(0)
        ok = item in variables.keys()

        if ok:
            items = []
            while(True):
                try:
                    value = variables[item]
                    ok = value in items
                    if not ok:
                        value = Decimal(value)
                    else:
                        value = Decimal(0)
                    break
                except Exception:
                    items.append(item)
                    item = value
                    if len(items) > len(variables):
                        value = Decimal(0)
                        break
                    pass
        return value

    def set(self, variables) -> list:
        """
        variables = {"x":10, "a" = 1}
        variables = ["x=10","a=1"]
        """
        package = self.__load(variables)
        return package
        pass
    pass
