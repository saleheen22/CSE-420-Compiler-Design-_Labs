Keywords = ["if", "float", "double", "string", "continue", "char", "else", "else if", "break", "return", "int"]
Identifiers = ["a", "b", "c", "d", "e"]
Math_Operators = ["+", "-", "*", "/", "="]
Logical_operator = [">", "<", "==", ">=", "<="]
Numerical_Values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "2.0", "6.0"]
others = [",", "{", "}", ";", "(", ")"]
Keywords_output = []
Identifiers_output = []
Math_Operators_output = []
Logical_operator_output = []
Numerical_Values_output = []
others_output = []
file = open("input.txt", "r")
for i in file:
    i = i.strip()
    inpt = i.split(" ")
    for j in inpt:
        # print(j[-1])
        if j[-1] == "," or j[-1] == ";":
            others_output.append(j[-1])
            j = j.replace(j[-1], "")
        if j in Keywords:
            Keywords_output.append(j)
        elif j in Identifiers:
            Identifiers_output.append(j)
        elif j in Math_Operators:
            Math_Operators_output.append(j)
        elif j in Logical_operator:
            Logical_operator_output.append(j)
        elif j in Numerical_Values:
            Numerical_Values_output.append(j)
        elif j in others:
            others_output.append(j)

Keywords_output = list(dict.fromkeys(Keywords_output))
Identifiers_output = list(dict.fromkeys(Identifiers_output))
Math_Operators_output = list(dict.fromkeys(Math_Operators_output))
Logical_operator_output = list(dict.fromkeys(Logical_operator_output))
Numerical_Values_output = list(dict.fromkeys(Numerical_Values_output))
others_output = list(dict.fromkeys(others_output))
print("Keywords:", end=" ")
print(*Keywords_output, sep=",")
print("Identifiers:", end=" ")
print(*Identifiers_output, sep=",")
print("Math Operators:", end=" ")
print(*Math_Operators_output, sep=",")
print("Logical Operators:", end=" ")
print(*Logical_operator_output, sep= " ")
print("Numerical Values:", end=" ")
print(*Numerical_Values_output, sep=",")
print("Others:", end=" ")
print(*others_output, sep="")