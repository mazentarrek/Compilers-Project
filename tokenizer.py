def tokenizer(x):

    oplist = []
    idlist = []
    numlist = []

    program = x

    def remove_Spaces(program):
        scanned_Program = []
        for line in program:
            if (line.strip() != ''):
                scanned_Program.append(line.strip())
        return scanned_Program

    for i in remove_Spaces(program):
        if (i.isalpha()):
            idlist.append(i)
        elif  (i.isnumeric()):
            numlist.append(i)
        elif (i=='+' or i=='*' or i=='-' or i=='/' ):
            oplist.append(i)

    return "There are " + str(len(oplist)) + " Operator(s): " + str(oplist) + '\n' + "There are " + str(len(idlist)) + " Identifier(s): " + str(idlist) + '\n' + "There are " + str(len(numlist)) + " Numeral(s): " + str(numlist)



