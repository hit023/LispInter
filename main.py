import parse
import evaluate

def main():
    h = ''
    while(h != '-h'):
        h = input('enter -h for usage\n')
    with open('README.txt','r') as f:
        for lines in f:
            print(lines)
    x = int(input("Enter option number to see usage and -1 to exit: \n"))
    while x != -1 :
        with open(str(x)+'.txt','r') as f:
           for lines in f:
               print(lines)
        x = int(input("Enter option number to see usage and -1 to exit: \n"))
    execute = evaluate.Evaluate()
    parser = parse.parse
    mydict = execute.modified_eval()
    while(True):
        try:
            prog = input('interactive@LispInter>>> ')
            retvalue = execute.fund(parser(prog),mydict)
            if retvalue is not None:
                print(PyToLisp(retvalue))
        except Exception as e:
            print('Not valid!','reason: '+str(e))
            pass

def PyToLisp(x):
    if isinstance(x, list):
        print('printing a list!')
        return '('+','.join(list(map(PyToLisp,x))) + ')'  #lists start with '[' and end with ']'.
    else:
        return str(x)

if __name__ == '__main__':
    main()
