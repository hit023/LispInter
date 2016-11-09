res=[]
def parse(prog):
    global res
    if len(prog)==0:
        print()
    elif prog[0] != '(':
        print("All expressions begin with '(' in LISP!\n")
    else:
        res=[]
        prog1 = prog.replace('(',' ( ')
        prog2 = prog1.replace(')',' ) ')
        allkeywords = prog2.split()
        res=helper(allkeywords)
        return res

def helper(l):
    if len(l) == 0:
        return
    top = l.pop(0)
    if top == '(':
        ret=[]
        #print('list so far: '+str(l))
        while l[0] != ')':
            ret.append(helper(l))
        l.pop(0)  #removes ')'
        return ret
    elif top == ')':
        print('why \')\' ?')
    else:
        return atom(top)

def atom(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return str(x)

if __name__=="__main__":
    parse(str(input('Enter command: \n')))
    print(res)
