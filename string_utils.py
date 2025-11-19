def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    if not formula:
        return []
    for i in range(1, len(formula)):
        if formula[i].isupper():
           split_formula.append(formula[start:i])
           start = i
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    x=0
    y=0
    digit_index=None
    for t in range(len(formula)):
        if formula[t].isdigit():
           digit_index = t
           break
        if digit_index == None:
           x=formula
           y=1
        else:
           y = int(formula[digit_index:])
           x = formula[0:digit_index]
        return x, y
