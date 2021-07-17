class Rule:

    def __init__(self):
        self.number = True
        self.pi = True
        self.euler = True
        self.plus_minus = True
        self.parenthesis_open = True
        self.parenthesis_closed = False
        self.multiplication = False
        self.division = False
        self.power = False
        self.factorial = False
        self.percentage = False
        self.semicolon = False
        self.trigonometry = True
        self.logarithm_natural = True
        self.logarithm = True
        self.root = True
        self.abs = True
        self.mod = True
        self.variable = True
        self.summa = True

    def to_assign(self, value):
        self.number = value
        self.pi = value
        self.euler = value
        self.plus_minus = value
        self.parenthesis_open = value
        self.parenthesis_closed = value
        self.multiplication = value
        self.division = value
        self.power = value
        self.factorial = value
        self.percentage = value
        self.trigonometry = value
        self.logarithm_natural = value
        self.logarithm = value
        self.root = value
        self.abs = value
        self.mod = value
        self.variable = value
        self.summa = value
