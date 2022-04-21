def tracefinal(x):

    state=1
    states=['1','id1','num1','dead','op1','3','op2','id3','num3']
    path=[1]
    mystring=x
    l=len(mystring)
    for i in mystring:
        if(state==1 and i.isalpha()):
            state='id1'
            path.append(state)
        elif(state==1 and i.isnumeric()):
            state='num1'
            path.append(state)
        elif(state=='id1' and (i=='+' or i=='-' or  i=='*')):
            state='op1'
            path.append(state)
        elif (state == 'id1' and i=='/'):
            state = 'op2'
            path.append(state)
        elif (state == 'num1' and i == '/'):
            state = 'op2'
            path.append(state)
        elif (state == 'num1' and (i=='+' or i=='-' or  i=='*')):
            state = 'op1'
            path.append(state)
        elif (state == 'op1' and i.isalpha()):
            state = 'id3'
            path.append(state)
        elif (state == 'op1' and i.isnumeric()):
            state = 'num3'
            path.append(state)
        elif (state == 'op1' and (i=='+' or i=='-' or  i=='*'or i=='/')):
            state = 'dead'
            path.append(state)
        elif (state == 'op2' and (i=='+' or i=='-' or  i=='*' or i=='0' or i=='/')):
            state = 'dead'
            path.append(state)
        elif (state == 'op2' and i.isnumeric()):
            state = 'num3'
            path.append(state)
        elif (state == 'op2' and i.isalpha()):
            state = 'id3'
            path.append(state)
        elif (state == 'id3' and i=='/'):
            state = 'op2'
            path.append(state)
        elif (state == 'id3' and (i=='+' or i=='-' or  i=='*')):
            state = 'op1'
            path.append(state)
        elif (state == 'num3' and (i=='+' or i=='-' or  i=='*' )):
            state = 'op1'
            path.append(state)

        elif (state == 'num3' and i=='/'):
            state = 'op2'
            path.append(state)
        elif(state==1):
            state='dead'
            path.append(state)
            break
        elif (state == 3 and (i == '+' or i == '-' or i == '*')):
            state = 'op1'
            path.append(state)
        elif (state == 3 and i == '/'):
            state = 'op2'
            path.append(state)
        elif (state == 3 and (i.isalpha() or i.isnumeric())):
            state = 'dead'
            path.append(state)
        elif ((not i=='+' and not i=='-' and not i=='*' and not i=='/') and (i.isalpha()==False and i.isnumeric()==False)):
            state = 'dead'
            path.append(state)
            break

    str4 = "x"

    if(path[-1]=='3' or path[-1]=='id3' or path[-1]=='num3'):
        str4 = "Status: Accepted"
    else:
        str4 = "Status: Rejected"

    return str(path) + '\n' + str4



