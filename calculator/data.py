from .rule import Rule


class Data:
    TEXT = "abcdefghijklmnñopqrstuvwxyz"
    NUMBER = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    PI = ["π", "pi"]
    EULER = ["e"]
    PLUS = "+"
    MINUS = "-"
    PARENTHESIS_OPENED = "("
    PARENTHESIS_CLOSED = ")"
    MULTIPLICATION = "*"
    DIVISION = "/"
    POWER = "^"
    FACTORIAL = "!"
    PORCENTAGE = "%"
    SEMICOLON = ";"
    TRIGONOMETRY = [
        "sin", "cos", "tan", "ctg", "sec", "csc",
        "asin", "acos", "atan", "actg", "asec", "acsc",
        "sinh", "cosh", "tanh", "ctgh", "sech", "csch",
        "asinh", "acosh", "atanh", "actgh", "asech", "acsch"]
    LOGARITHM_NATURAL = ["ln"]
    LOGARITHM = ["log"]
    ROOT = ["√", "root", "raiz"]
    ABS = ["abs"]
    MOD = ["mod"]
    SUMMA = ["∑", "summa"]  # sumatoria

    SIN = "sin"
    COS = "cos"
    TAN = "tan"
    CTG = "ctg"
    SEC = "sec"
    CSC = "csc"
    ARC_SIN = "asin"
    ARC_COS = "acos"
    ARC_TAN = "atan"
    ARC_CTG = "actg"
    ARC_SEC = "asec"
    ARC_CSC = "acsc"
    SIN_HYPER = "sinh"
    COS_HYPER = "cosh"
    TAN_HYPER = "tanh"
    CTG_HYPER = "ctgh"
    SEC_HYPER = "sech"
    CSC_HYPER = "csch"
    ARC_SIN_HYPER = "asinh"
    ARC_COS_HYPER = "acosh"
    ARC_TAN_HYPER = "atanh"
    ARC_CTG_HYPER = "actgh"
    ARC_SEC_HYPER = "asech"
    ARC_CSC_HYPER = "acsch"

    def __init__(self, function):
        self.__is_concluded = True  # por default puede terminar en una variable
        self.__function = function
        self.rule = Rule()
        pass

    def is_concluded(self) -> bool:
        return self.__is_concluded

    def to_plus_minus(self, index_start):
        positive_sign, negative_sign = 0, 0
        function = self.__function[index_start:]
        index_end = index_start
        sign = ""

        for item in function:
            index_end = index_end + 1
            if item == Data.PLUS:
                positive_sign = positive_sign + 1
            elif item == Data.MINUS:
                negative_sign = negative_sign + 1
            else:
                index_end = index_end - 1
                sign = Data.MINUS if (negative_sign % 2 == 1) else Data.PLUS
                break

        # Establecer reglas
        self.rule.to_assign(True)
        self.rule.plus_minus = False
        self.rule.parenthesis_closed = False
        self.multiplication = False
        self.division = False
        self.power = False
        self.factorial = False
        self.__is_concluded = False

        return sign, index_end

    def to_number(self, index_start):
        function = self.__function[index_start:]
        index_end = 0
        one_point = True
        length = len(function)

        for i in range(length):
            item = function[i]
            index_end = index_start + i + 1
            ok = item in Data.NUMBER
            if ok:
                continue
            elif item == ".":
                if one_point:
                    one_point = False
                    if i == length - 1:
                        index_end = index_end - 1
                else:
                    index_end = index_end - 1
                    break
            else:
                index_end = index_end - 1
                break

        # Establecer reglas
        self.rule.to_assign(True)
        self.__is_concluded = True

        number = self.__function[index_start:index_end]
        return number, index_end

    def to_pi(self):
        # Establecer reglas
        self.rule.to_assign(True)
        self.rule.number = False
        self.rule.factorial = False
        self.__is_concluded = True

    def to_euler(self):
        # Establecer reglas
        self.rule.to_assign(True)
        self.rule.number = False
        self.rule.factorial = False
        self.__is_concluded = True

    def to_multiplication(self):
        # Establecer reglas
        self.rule.to_assign(True)
        self.rule.parenthesis_closed = False
        self.rule.multiplication = False
        self.rule.division = False
        self.rule.power = False
        self.rule.factorial = False
        self.__is_concluded = False

    def to_division(self):
        self.to_multiplication()
        self.__is_concluded = False

    def to_power(self):
        self.to_multiplication()
        self.__is_concluded = False

    def to_factorial(self):
        # Establecer reglas
        self.rule.to_assign(True)
        # self.rule.number = False
        self.__is_concluded = True

    def to_porcentage(self):
        # Establecer reglas
        self.rule.to_assign(True)
        # self.rule.number = False
        self.__is_concluded = True

    def to_trigonometry(self):
        # Establecer reglas
        self.rule.to_assign(False)
        self.rule.parenthesis_opened = True
        self.__is_concluded = False

    def to_logarithm(self):
        # Establecer reglas
        self.rule.to_assign(False)
        self.rule.parenthesis_opened = True
        self.rule.semicolon = True
        self.__is_concluded = False

    def to_logarithm_natural(self):
        # Establecer reglas
        self.rule.to_assign(False)
        self.rule.parenthesis_opened = True
        self.__is_concluded = False

    def to_root(self):
        # Establecer reglas
        self.rule.to_assign(False)
        self.rule.parenthesis_opened = True
        self.rule.semicolon = True
        self.__is_concluded = False

    def to_abs(self):
        # Establecer reglas
        self.rule.to_assign(False)
        self.rule.parenthesis_opened = True
        self.__is_concluded = False

    def to_mod(self):
        # Establecer reglas
        self.rule.to_assign(False)
        self.rule.parenthesis_opened = True
        self.rule.semicolon = True
        self.__is_concluded = False

    def to_variable(self):
        # Establecer reglas
        self.rule.to_assign(True)
        # self.rule.number = False
        self.__is_concluded = True

    def to_parenthesis_opened(self):
        # Establecer reglas
        self.rule.to_assign(True)
        self.rule.parenthesis_closed = False
        self.rule.multiplication = False
        self.rule.division = False
        self.rule.power = False
        self.rule.factorial = False
        self.rule.porcentage = False
        self.__is_concluded = False

    def to_parenthesis_closed(self):
        # Establecer reglas
        self.rule.to_assign(True)
        self.__is_concluded = True

    def to_semicolon(self):
        # Establecer reglas
        self.rule.to_assign(True)
        self.rule.parenthesis_closed = False
        self.rule.multiplication = False
        self.rule.division = False
        self.rule.power = False
        self.rule.factorial = False
        self.rule.porcentage = False
        self.rule.semicolon = False
        self.__is_concluded = False

    def to_text(self, index_start):
        function = self.__function[index_start:]
        index_end = index_start
        length = len(function)
        for i in range(length):
            index_end = index_end + 1
            item = function[i]
            ok = item in Data.TEXT
            if not ok:
                index_end = index_end - 1
                break
        text = self.__function[index_start:index_end]
        return text, index_end

    def to_summa(self):
        # Establecer reglas
        self.rule.to_assign(False)
        self.rule.parenthesis_opened = True
        self.rule.semicolon = True
        self.__is_concluded = False
