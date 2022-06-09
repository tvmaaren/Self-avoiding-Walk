#!/usr/bin/env python3


class LambdaTerm:
    """Abstract Base Class for lambda terms."""

    def fromstring(self):
        """Construct a lambda term from a string."""
        raise NotImplementedError

    def substitute(self, rules):
        """Substitute values for keys where they occur."""
        raise NotImplementedError

    def reduce(self):
        """Beta-reduce."""
        raise NotImplementedError


class Variable(LambdaTerm):
    """Represents a variable."""

    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return "Variable("+repr(self.symbol)+")"

    def __str__(self):
        return self.symbol

    def substitute(self, rules):
        try:
            self.symbol = rules[self.symbol]
        except:
            None


class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body):
        self.variable = variable
        self.body = body

    def __repr__(self): 
        return "Abstraction("+repr(self.variable)+","+repr(self.body)+")"

    def __str__(self):
        return "\u03bb"+str(self.variable)+"."+str(self.body)

    def __call__(self, argument): raise NotImplementedError

    def substitute(self, rules):
        self.variable.substitute(rules)
        self.body.substitute(rules)

class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

    def __repr__(self):
        return "Application("+repr(self.function)+", "+repr(self.argument)+")"

    def __str__(self):
        return "("+str(self.function)+")  "+str(self.argument)

    def substitute(self, rules):
        self.function.substitute(rules)
        self.argument(rules)

    def reduce(self):raise NotImplementedError
