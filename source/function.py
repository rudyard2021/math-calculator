from .data import Data
from .parenthesis import Parenthesis
from .package import Package
from .simulator import Simulator
from .variable import Variable
from .operation import Operation
from .summa import Summa

class Function:

    def __init__(self):
        self.process = []
        self.types = []
        self.__error = None

    def start(self, function):
        function = self.__trim(str(function))

        data = Data(function)
        parenthesis = Parenthesis()
        package = Package()

        index, length = 0, len(function)
        error = False
        while index < length:
            item = function[index]
            variable, _ = data.to_text(index)

            if variable != "":
                item = variable

            item_length = len(item)

            if item in Data.NUMBER:
                if data.rule.number:
                    item, index = data.to_number(index)
                    package.add_number(item)
                else:
                    error = True
            elif item in Data.PI:
                if data.rule.pi:
                    data.to_pi()
                    package.add_variable(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.EULER:
                if data.rule.euler:
                    data.to_euler()
                    package.add_variable(item)
                    index = index + item_length
                else:
                    error = True
            elif item in [Data.PLUS, Data.MINUS]:
                if data.rule.plus_minus:
                    item, index = data.to_plus_minus(index)
                    package.add_operator(item)
                else:
                    error = True
            elif item in Data.PARENTHESIS_OPENED:
                if data.rule.parenthesis_opened:
                    data.to_parenthesis_opened()
                    package.add_opened(item)
                    parenthesis.open()
                    parenthesis.input()
                    index = index + item_length
                else:
                    error = True
            elif item in Data.PARENTHESIS_CLOSED:
                if data.rule.parenthesis_closed:
                    data.to_parenthesis_closed()
                    package.add_closed(item)
                    error = parenthesis.close()
                    if not error:
                        index = index + item_length
                else:
                    error = True
            elif item in Data.MULTIPLICATION:
                if data.rule.multiplication:
                    data.to_multiplication()
                    package.add_operator(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.DIVISION:
                if data.rule.division:
                    data.to_division()
                    package.add_operator(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.POWER:
                if data.rule.power:
                    data.to_power()
                    package.add_operator(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.FACTORIAL:
                if data.rule.factorial:
                    data.to_factorial()
                    package.add_factorial(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.PERCENTAGE:
                if data.rule.percentage:
                    data.to_percentage()
                    package.add_percentage(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.SEMICOLON:
                if data.rule.semicolon:
                    data.to_semicolon()
                    package.add_semicolon(item)
                    error = parenthesis.check_semicolon()
                    if not error:
                        index = index + item_length
                else:
                    error = True
            elif item in Data.TRIGONOMETRY:
                if data.rule.trigonometry:
                    data.to_trigonometry()
                    package.add_function(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.LOGARITHM_NATURAL:
                if data.rule.logarithm_natural:
                    data.to_logarithm_natural()
                    package.add_function(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.LOGARITHM:
                if data.rule.logarithm:
                    data.to_logarithm()
                    package.add_function(item)
                    parenthesis.input(1, 2)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.ROOT:
                if data.rule.root:
                    data.to_root()
                    package.add_function(item)
                    parenthesis.input(1, 2)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.SUMMA:
                if data.rule.summa:
                    new_text, new_index = data.to_summa(index + item_length)
                    if new_text == "":
                        error = True
                    else:
                        summa = Summa(Function())
                        err = summa.load(new_text)
                        if err is None:
                            package.add_func_summa(summa)
                        else:
                            new_index = index + item_length + len(err)
                            error = True
                    index = new_index
                else:
                    error = True
            elif item in Data.ABS:
                if data.rule.abs:
                    data.to_abs()
                    package.add_function(item)
                    index = index + item_length
                else:
                    error = True
            elif item in Data.MOD:
                if data.rule.mod:
                    data.to_mod()
                    package.add_function(item)
                    parenthesis.input(2, 2)
                    index = index + item_length
                else:
                    error = True
            elif item == variable:
                if data.rule.variable:
                    data.to_variable()
                    package.add_variable(item)
                    index = index + item_length
                else:
                    error = True
            else:
                error = True

            if error:
                break
            pass

        text = function
        concluded_parenth, number = parenthesis.is_concluded()

        if error or not concluded_parenth or not data.is_concluded():
            self.__error = function[0:index]
        else:
            self.__error = None

            for item in range(number):
                package.add_closed(Data.PARENTHESIS_CLOSED)
            text = text + Data.PARENTHESIS_CLOSED * number

            package_list = package.get()
            package_types = package.get_types()

            simulator = Simulator(package_list, package_types)
            process = simulator.get_process()

            self.types = package_types
            self.process = process
            self.variable = Variable(package_list, package_types)

        return self.__error

    def __trim(self, function):
        function = str.replace(function, " ", "")
        function = str.lower(function)
        return function

    def f(self, variables=None):
        if self.__error is not None:
            return None

        package, var_items = self.variable.set(variables)
        types = self.types.copy()
        length = len(self.process)

        operation = Operation(package, types, var_items)
        for index in range(length):
            index_process = self.process[index]
            item_type = types[index_process]

            if item_type in [Package.FACTORIAL, Package.PERCENTAGE]:
                operation.factorial_percentage(index_process)
            elif item_type in [Package.VARIABLE, Package.NUMBER]:
                operation.variable_number(index_process)
            elif item_type == Package.OPERATOR:
                operation.operator(index_process)
            elif item_type == Package.FUNCTION:
                operation.function(index_process)
            elif item_type == Package.FUNC_SUMMA:
                operation.func_suma(index_process)

        value = package[0]
        if type(value) is Summa:
            return value.calc(var_items)
        return value
