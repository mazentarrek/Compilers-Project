import nltk
import re


def tokenizer(x):

    oplist = []
    idlist = []
    numlist = []

    count = 0
    program = x

    def remove_Spaces(program):
        scanned_Program = []
        for line in program:
            if (line.strip() != ''):
                scanned_Program.append(line.strip())
        return scanned_Program

    def remove_Comments(program):
        program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
        program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
        program_Comments_removed = program_Single_Comments_Removed
        return program_Comments_removed

    RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
    RE_Numerals = "^(\d+)$"
    RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

    program_Comments_removed = remove_Comments(program)
    prog = program_Comments_removed.split('\n')

    scanned_Prog = remove_Spaces(prog)

    scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])

    scanned_Program_lines = scanned_Program.split('\n')
    match_counter = 0

    Source_Code = []
    for line in scanned_Program_lines:
        Source_Code.append(line)

    for line in Source_Code:
        count = count + 1

        tokens = nltk.wordpunct_tokenize(line)

        for token in tokens:
            if (re.findall(RE_Operators, token)):
                oplist.append(token)
            elif (re.findall(RE_Numerals, token)):
                numlist.append(token)
            elif (re.findall(RE_Identifiers, token)):
                idlist.append(token)


    return "There are " + str(len(oplist)) + " Operator(s): " + str(oplist) + '\n' + "There are " + str(len(idlist)) + " Identifier(s): " + str(idlist) + '\n' + "There are " + str(len(numlist)) + " Numeral(s): " + str(numlist)



