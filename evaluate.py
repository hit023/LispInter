import importlib as il
from parse import atom
import math
import operator as op
import inspect

class Evaluate(object):
    lib=[]
    def __init__(self):
        if inspect.stack()[1][3] != 'Function' :
            string=str(input("enter Python module to be used with LISP(like \'math\' etc)(\'stop\' to proceed further): \n"))
            while string != 'stop' :
                Evaluate.lib.append(string)
                string=str(input("enter Python module to be used with LISP(like \'math\' etc)(\'stop\' to proceed further): \n"))

    @staticmethod
    def modified_eval():
        a=dict()
        a.update({
            'cons': lambda x,y: [x]+[y],
            'car' : lambda x: x[0],
            'cdr' : lambda x: x[1:],
            'iseq' : lambda x,y: x is y,
            'gt' : op.gt,
            'lt' : op.lt,
            'gtet' : op.ge,
            'ltet' : op.le,
            'quote' : lambda x: str(x),
            'add' : op.add,
            'subtract' : op.sub,
            'divide' : op.truediv,
            'multiply' : op.mul,
            'modulus' : op.mod,
            'isatom' : lambda x: not isinstance(x,list)
            })
        for i in Evaluate.lib:
            ownmodule = il.import_module(i)
            a.update(vars(ownmodule))
        return a

    def fund(self,x,ref_dict):
        if isinstance(x,str):
            if not isinstance(ref_dict,Env) and ref_dict.__contains__(x):
                return ref_dict[x]
            elif isinstance(ref_dict,Env) and ref_dict.fetch(x).get(x,None):
                return ref_dict.fetch(x).get(x)
            else:
                return x
        if isinstance(x,str):
            if ref_dict.fetch(x).get(x,None):
                return ref_dict.fetch(x).get(x)
            else:
                return x
        elif not isinstance(x,list):
            return x
        elif x[0] == 'define':
            (*z,variable,value) = x                       #unpacking x into variable and value
            ref_dict[variable] = self.fund(value,ref_dict)
        elif x[0] == 'lambda':
            (*ignore,p,body) = x
            return Function(p,body,ref_dict)        #'Function' in-turn uses 'fund' to Evaluate.
        elif x[0] == 'cond':
            for i in x[1:]:
                if i[0] != 'else':
                    truthvalue = self.fund(i[0],ref_dict)
                    if truthvalue:
                        return self.fund(i[1],ref_dict)
                else:
                    return self.fund(i[1],ref_dict)
        else:
            if not isinstance(ref_dict,Env) and ref_dict.__contains__(x[0]):
                function = ref_dict[x[0]]
                argument_list = [self.fund(i,ref_dict) for i in x[1:]]
                return function(*argument_list)
            elif isinstance(ref_dict,Env) and ref_dict.fetch(x[0]).get(x[0],None):
                function = ref_dict.fetch(x[0]).get(x[0])
                argument_list = [self.fund(i,ref_dict) for i in x[1:]]
                return function(*argument_list)
            else:
                return x

#3 parts of a method: body, arguments and an environment to look up the arguments for resp. parameters.

class Function(object):
    run = Evaluate()
    def __init__(self,para,body,envir):
        self.para,self.body,self.envir = para,body,envir  #unpack the variables

    def __call__(self,*args):         #this method is used to call an object of class 'Function' with arguments
        return Function.run.fund(self.body, Env(args, self.para, self.envir))

class Env(dict):          #a subclass of 'dict' class.
    def __init__(self,args: list,para: list, globalenv: dict = None):
        self.update(dict(zip(para,args)))
        self.globalenv = globalenv

    def fetch(self,k):
        if self.__contains__(k):
            return self
        else:
            return self.globalenv
