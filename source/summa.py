from  decimal import Decimal

class Summa:

    def __init__(self, func):
        self.func = func
        self.start = 1
        self.end = 1
        self.skip = 1
        self.var = "x"

    def load(self, text):
        text = text[1:-1]
        formats = text.split(";")

        if len(formats) < 4:
            return text

        formats.reverse()
        index = 0
        for x in formats:
            if x.isalpha():
                break
            index = index + 1

        index = len(formats) - index - 1
        formats.reverse()

        func = ";".join(formats[0:index])
        variables = formats[index:]

        if func == "" or len(variables) < 3:
            return text

        try:
            self.var = variables[0]
            self.start = Decimal(variables[1])
            self.end = Decimal(variables[2])
            if len(variables) == 4:
                self.skip = Decimal(variables[3])

            if self.end < self.start:
                return text

        except Exception:
            return text

        err = self.func.start(func)
        return err

    def calc(self, variables:dict):
        summa = 0
        x = self.start
        while x <= self.end:
            if self.var is not None:
                variables[self.var] = x
            x = x + self.skip
            summa = summa + self.func.f(variables)

        if self.var is not None:
            variables.pop(self.var)

        return summa
