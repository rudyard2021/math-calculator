from calculator.function import Function

class Calculator:
    
    def __init__(self):
        self.function = Function()

    def start(self, text:str):
        self.function.start(text)
    
    def f(self, variables=None):
        self.function.f(variables)
