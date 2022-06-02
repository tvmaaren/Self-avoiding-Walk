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


class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body):
        self.variable = variable
        self.body = body

    def __repr__(self): 
        return "Abstraction("+repr(variable)+","+repr(body)+")"

    def __str__(self):
        return "\u03bb"+str(variable)+"."+str(variable)

    def __call__(self, argument): raise NotImplementedError

    def substitute(self, rules): raise NotImplementedError


class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument): raise NotImplementedError

    def __repr__(self): raise NotImplementedError

    def __str__(self): raise NotImplementedError

    def substitute(self, rules): raise NotImplementedError

    def reduce(self): raise NotImplementedError

print('huts')