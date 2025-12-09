import operator

def basic_op(op, value1, value2):
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    return operators[op](value1, value2)