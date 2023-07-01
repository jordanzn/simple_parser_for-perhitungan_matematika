import re
# re = regular expression

print('Input format:')
print('     Example #1 : 123 + 234 - 1.234 x -576')
print('     Example #2 : 7.5 : -2.14 ^ 789\n')
print('Operan     := bil bulat, bil riil')
print('Operator   := +, -, :, x, ^, |')
print('Grouping   := (, )\n')
print('Input Formula:')


lex_dictionary = {
    r"-?\d+\.\d+":  ("Operan", 2),          # bil riil
    r"-?\d+":       ("Operan", 1),          # bil bulat
    
# bil riil diletakkan sebelum bil bulat agar terbaca lebih dulu oleh program,
# dan program tidak akan salah mengira bahwa operan bil riil adalah bil bulat
    
    r"\+":          ("Operator", 3),        # +
    r"-":           ("Operator", 4),        # -
    r"x":           ("Operator", 5),        # x
    r":":           ("Operator", 6),        # :
    r"\^":          ("Operator", 7),        # ^
    r"\|":          ("Operator", 8),        # |
    r"\(":          ("Grouping", 9),        # (
    r"\)":          ("Grouping", 10),       # )
}

#TUGAS PROGRAM TAHAP 1
def lexical(x):
    t = []
    lexs = re.findall(r"-?\d+\.\d+|-?\d+|\S", x)
    
    for lex in lexs:
        match = False
        for formula, (kind, token) in lex_dictionary.items():
            if re.match(formula, lex):
                t.append(token)
                match = True
                break
        if not match:
            t.append("error")    
    return t

#TUGAS PROGRAM TAHAP 2
class Parser:
    def __init__(j, t):
        j.t = t
        j.current_token = None
        j.index = -1
        j.error = False

    def parse(j):
        j.advance()
        j.expression()

        if not j.error and j.current_token is None:
            print("Valid Formula.")
        else:
            print("Invalid Formula.")

    def advance(j):
        j.index += 1
        if j.index < len(j.t):
            j.current_token = j.t[j.index]
        else:
            j.current_token = None

    def expression(j):
        j.term()
        while j.current_token in [3, 4]:
            j.advance()
            j.term()

    def term(j):
        j.factor()
        while j.current_token in [5, 6, 7, 8]:
            j.advance()
            j.factor()

    def factor(j):
        if j.current_token in [1, 2]:
            j.advance()
        elif j.current_token == 9:
            j.advance()
            j.expression()
            if j.current_token == 10:
                j.advance()
            else:
                j.error = True
        else:
            j.error = True


#CONCLUSION
input_formula = input()

output_t = lexical(input_formula)
print("\nInput: ", input_formula)
print("\nOUTPUT TAHAP 1")
print("Lexical:", " ".join(str(token) for token in output_t))
print("\nOUTPUT TAHAP 2")

parser = Parser(output_t)
parser.parse()
