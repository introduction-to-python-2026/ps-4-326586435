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
    digit_index = None

    for i, ch in enumerate(formula):
        if ch.isdigit():
            digit_index = i
            break

    if digit_index is None:
        return formula, 1

    x = formula[:digit_index]
    y = int(formula[digit_index:])
    return x, y

