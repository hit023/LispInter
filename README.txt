LispInter is a an interpreter designed to interpret a fairly large subset of the programming language, Scheme- a dialect of Lisp. It has been written using Python 3.5.2. It is based on the minimalistic design introduced by a famous paper written by John McCarthy in 1960, on LISP(LISt Processor): http://www-formal.stanford.edu/jmc/recursive.html

Every line in LISP is either an atom or a list. Atoms can be 1) numbers: int or float, 2) symbols: typically, strings. A list is usually represented as a collection of atoms surrounded by '(' and ')'. Every expression entered as a part of a LISP program is to be well-parenthesised.

LispInter provides appropriate interpretation for the following primitive functions and built-in operations:
1) define: to declare a variable and assigne a value to it.
2) cons: used to bind 2 atoms together. Implemented as a list.
3) car: first piece of the binding is returned.
4) cdr: rest of the pieces of the binding are returned as a separate list.
5) iseq: returns true if the following arguments are equal to each other.
6) isatom: returns true if the expression entered is an atom.
7) quote: simply spit out what was entered.
8) cond: a series of if/else statements.
9) lambda: creates a user-defined function.
** +,-,*,/,<,>,>=,<= have usual meanings.
** Most of the standard math functions.
