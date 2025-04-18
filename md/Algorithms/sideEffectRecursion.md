# Side Effect Recursion
## Overview: 
Recursion is a distinct topic in programming. It requires thinking in a different way, and that is difficult for many including this Author. So after much trial and error, I came up with the idea of 'side effect recursion', which is easier to understand and apply. Recursion can be conceptually thought of as a iterative refinement of a solution until solved.  In the 'side effect recursion', this iterative solution is passed as a paramenter to the recursive function allowing the function to refine the solution. When the function determines that the solution is reached, it just returns True. This overview will be continued later after the following trivial instance of the eternal example of recursion - the factorial.

Normal Recursion:

def factorial(N):
    if N==1: return 1
    else return factorial(N-1)

Side effect Recursion:

def factorialS(N,soFar):
    soFar = N*soFar
    if N==1: return soFar
    else: return factorialS(N-1,soFar)


Both work:
N=5
print(f'Factorial {N} using Normal recursion = {factorial(N)}')
print(f'Factorial {N} using side effect recursion = {factorialS(N,1)}')
exit(0)

The 'side effect' recursion has more lines of code than the normal recursion. However it is a little clearer in intent. The 'soFar' parameter tracks the work done each time it loops. This also lends itself to 'caching' where we can speed this up by supplying a value to 'soFar' and 'N' as the third and fourth parameters 
