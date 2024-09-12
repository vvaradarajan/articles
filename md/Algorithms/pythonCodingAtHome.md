# Coding on Python at Home
<img src="img/ramJam.jpeg" /> 

You are sitting at home working away at your IT job... 
How many more reports can you generate? How many sales figures do you have to tally, how many charts, how many databases, how many sql queries, how many 'design' patterns to follow, how many bugs to fix etc. etc.. because you get paid for it.. Fatigue sets in , purpose of living is being questioned, and just when you are about to yell '.. to hell with all this..', your mortgage comes due, and don't look for that escape vacation because that will put you further in the red..

Well. Python to the rescue! You can do a lot with Python, including having a little recreation!  Let us do some Radix arithmetic.. Why? Because this is the birth week of the elegant mathematician Ramanujan. 'Numbers were his personal friends!'. He played with his friends all life-long, and arranged them in patterns which he thought beautiful. Most of you will think the same, and yet they seem so easy, that you will say 'Why did'nt I think of that?'

There is more.. Once you see the pattern, it will enter your head, and never leave until you find some truth about! Don't worry.. Python to the rescue..

Here is one such pattern:  
<img src="img/ramJam2.jpeg" />

I have no idea what you see in this pattern, but what I see this:

a. All the digits of the radix 10 (or base 10) except 0 are represented. 

b. The second number 8 is 10 - 2 

c. The third number is a digit in the sequence of all digits in base 10, except 0. 

The follow-up question is, is this pattern valid for number system in a different radix? The answer to this question is to use Python. Search google, and here are some useful links:

<a href="https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base">number systems on stackoverflow</a>  

Using the ideas in these links and knowledge of the number base from high school, you can create a python class to answer the question. First, here is the output of my program: 

```
$ python ramjam.py 3
1 x 1 + 1 = 2 => 1 x 1 + 1 = 2
12 x 1 + 2 = 21 => 5 x 1 + 2 = 7
$ python ramjam.py 4
1 x 2 + 1 = 3 => 1 x 2 + 1 = 3
12 x 2 + 2 = 32 => 6 x 2 + 2 = 14
123 x 2 + 3 = 321 => 27 x 2 + 3 = 57
$ python ramjam.py 5
1 x 3 + 1 = 4 => 1 x 3 + 1 = 4
12 x 3 + 2 = 43 => 7 x 3 + 2 = 23
123 x 3 + 3 = 432 => 38 x 3 + 3 = 117
1234 x 3 + 4 = 4321 => 194 x 3 + 4 = 586
$ python ramjam.py 6
1 x 4 + 1 = 5 => 1 x 4 + 1 = 5
12 x 4 + 2 = 54 => 8 x 4 + 2 = 34
123 x 4 + 3 = 543 => 51 x 4 + 3 = 207
1234 x 4 + 4 = 5432 => 310 x 4 + 4 = 1244
12345 x 4 + 5 = 54321 => 1865 x 4 + 5 = 7465
$ python ramjam.py 7
1 x 5 + 1 = 6 => 1 x 5 + 1 = 6
12 x 5 + 2 = 65 => 9 x 5 + 2 = 47
123 x 5 + 3 = 654 => 66 x 5 + 3 = 333
1234 x 5 + 4 = 6543 => 466 x 5 + 4 = 2334
12345 x 5 + 5 = 65432 => 3267 x 5 + 5 = 16340
123456 x 5 + 6 = 654321 => 22875 x 5 + 6 = 114381
$ python ramjam.py 8
1 x 6 + 1 = 7 => 1 x 6 + 1 = 7
12 x 6 + 2 = 76 => 10 x 6 + 2 = 62
123 x 6 + 3 = 765 => 83 x 6 + 3 = 501
1234 x 6 + 4 = 7654 => 668 x 6 + 4 = 4012
12345 x 6 + 5 = 76543 => 5349 x 6 + 5 = 32099
123456 x 6 + 6 = 765432 => 42798 x 6 + 6 = 256794
1234567 x 6 + 7 = 7654321 => 342391 x 6 + 7 = 2054353
$ python ramjam.py 9
1 x 7 + 1 = 8 => 1 x 7 + 1 = 8
12 x 7 + 2 = 87 => 11 x 7 + 2 = 79
123 x 7 + 3 = 876 => 102 x 7 + 3 = 717
1234 x 7 + 4 = 8765 => 922 x 7 + 4 = 6458
12345 x 7 + 5 = 87654 => 8303 x 7 + 5 = 58126
123456 x 7 + 6 = 876543 => 74733 x 7 + 6 = 523137
1234567 x 7 + 7 = 8765432 => 672604 x 7 + 7 = 4708235
12345678 x 7 + 8 = 87654321 => 6053444 x 7 + 8 = 42374116
```

This output shows the pattern for bases 3 thru 9. The pattern is shown on the left followed by => and the familiar base 10 calculation on the right. So yes, it is true for - the pattern is valid for bases other than 10!

Here is the code (written using Python 3.8):

```
#program to generate some patterns in base N

class baseN:
    def __init__(self,N):
        self.b=N

    def tb(self,M): #to base (returns number in that base)
        s = ""
        n=self.b #b=base
        while M>0:
            s = str(M % n) + s
            M = int(M/n)
        return int(s)

    def fb(self,s): #from base (returns number)
        d=0
        s=str(s)
        l=len(s)
        for i,c in enumerate(s):
            #print(f'd={d}; c={int(c)}; l-i: {l-i-1}')
            d += int(c)*self.b**(l-i-1)
        return d

    def printPattern(self):
        for i in range(1,self.b):
            j=self.b**(i-1) #should be a pattern
            p1=1
            for j in range(1,i):
                p1 *=self.b
                p1 +=j+1
            p2=self.tb(self.b-2)
            p3=i
            p4=p1*p2+p3
            print(f'{self.tb(p1)} x {self.tb(p2)} + {self.tb(p3)} = {self.tb(p4)} => {p1} x {p2} + {p3} = {p4}')

def test(b):
    bN=baseN(b)
    bN.printPattern()

import sys
if __name__ == '__main__':
    msg='usage: python ramjam.py <x> where <x> is between 3 and 9';
    err=False
    if len(sys.argv) !=2: err=True
    b=sys.argv[1]
    if not b.isnumeric(): err=True
    b=int(b)
    if not (b>=3 and b<=9): err=True
    if err: print(msg)
    else: test(b)

```

Now take that Pythonication! 
Go find your own pattern! <br/> 
Python at Home to the rescue..

Ramanujan can help: https://en.wikipedia.org/wiki/Srinivasa_Ramanujan

