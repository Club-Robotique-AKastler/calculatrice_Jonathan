

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def pow(a,b):
    return a ** b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return math.inf

def fdiv(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return math.inf

def mod(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return math.inf

class Operation:
    def __init__(self, first: float, operator: str, second: float) -> None:
        self.first_term = first
        self.operator = operator
        self.second_term = second

    def __str__(self) -> str:
        return f"{self.first_term} {self.operator} {self.second_term}"

def get_terms(operation: str, operators: dict) -> Operation:
    index = -1
    first_term = ""
    operator = ""
    second_term = ""

    for char in operation:
        index += 1
        if char == " ":
            continue

        if char == '-' and first_term == "":
            first_term = "-"

        if char == ".":
            if "." not in first_term:
                first_term += "."
            else:
                raise ValueError("mais chef (deux points)")
        
        if char.isdigit():
            first_term += char

        if char in operators.keys():
            operator = char
            break


    for i in range(index, len(operation)):
        char = operation[i]
        if char == " ":
            continue

        if char == '-' and second_term == "":
            second_term = "-"

        if char == ".":
            if "." not in second_term:
                second_term += "."
            else:
                raise ValueError("mais chef (deux points)")
        
        if char.isdigit():
            second_term += char

        if char in operators.keys():
            raise ValueError("chef tu fous quoi (trop d'opératuers ptet)")

        if char == "!":
            break

    return Operation(first_term, operator, second_term)

        

def main():
    OPERATORS = {
        "+": add,
        "-": sub,
        "*": mult,
        "^": pow,
        "/": div,
        ":": fdiv,
        "%": mod
    }
    
    terms = get_terms(input("> ") + "!", OPERATORS)


if __name__ == "__main__":
    main()