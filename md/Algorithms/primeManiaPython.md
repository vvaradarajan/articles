# The Python slithers among numbers..

The mind keeps ticking. Anything to explore..One of them is numbers. Everyone who has memorized multiplication tables, has and will take on mental calculation challenges, become sudoku champs, try to outdo cash registers at the shops, and come up with patterns in numbers all connected in some way. Numbers, though claimed as human creations, have a beauty that is divine. Movies have been made (a beautiful mind is just one of them), Human calculators have fascinated the world for as long as there has been history with their lightning fast calculations and observences of patterns in numbers.

While our minds keep ticking, most of us are feeble in numeric skills. But now we have weapons, and a powerful one is Python.  Think of some numeric pattern, and watch it grow as you code! Explore the patterns as if you are a great mathematician and feel the joy! We owe all this to Python and let us begin..

Now onto a design of using Python to explore one fascinating example:

Prime numbers of course come to mind..and along with that our long lost anscestor Erasmus and his sieve! Given that the first prime is 2, using the sieve, Erasmus eliminated 1/2 of all numbers from the distinction of being primes! And 'eureka', if 2 eliminates 1/2 all number from being primes, then 3 should eliminate 1/3 and 5 should eliminate 1/5 and 7 .. 1/7 ..  Strong Mathematicians will soon start putting in weird greek symbols and 'prove' this for all time! The not so strong will start coding to 'see' if this is really true or not!

Let us do some design. Concieve of some pattern to code..
Start with prime set having its first member - the number 2. Put all the remaining numbers into another set called Candidate Primes. This appears impossible as it is an infinite set. But they follow a pattern, which is:
a. Represent this set as a set of 'gaps' (difference between a number and the one prior to it.) So the set of numbers [3,4,5,6,7,..] becomes [1,1,1,1,1..]. In this set the first number is the difference between the last prime and itself, which is 3-2 = 1, the second is 4-3=1 and so on.first member as 2, and the remaing numbers ready to be sieved are [1,1,1,1,1,..] i.e. a pattern of numbers that differ by 1. Now we apply the sieve to this set i.e. remove all numbers divisible by the new prime (2). That gives the new pattern [1,2,2,2,2,..] which are 1+2,1+2+2..(i.e. 3,5,7,9..). Now thinking a little bit, the first number in this sequence must be a prime, which is 1+2 = 3. The next numbers may or may not be primes (i.e. 4,5,6,7,8..). We have to check if these are divisible (sieved out..) by the new prime 3, and eliminate them if so. Going back to coding, our prime set at this point is {2}, and our pattern is [1,2,2,2,2,2..] or [1,(2)*]. The first number in the pattern is separated out as it is the next prime, and the (2)* is '2' repeated ad-infinitum..

Now repeat the process: 
a. Add the 1st element as the new prime to the prime set.
b. Apply the Sieve and remove all numbers divisible by the new prime

After a couple of repeats, we start seeing a pattern! The pattern repeats itself every 'prime factorial' intervals. We define the prime factorial as the product of all primes in our prime set. Ex: If our prime set contains 2,3 the prime factorial is 2*3 = 6. For a prime set containing 2,3,5 the prime factorial is 2*3*5 = 30

Such a pattern can be represented as a python array: [p,(cpattern)*]. The first element p is the next prime, and cpattern is the set of 'candidate primes'

Rather than worrying about whether the above is a correct design or not (leave that to the real mathematicians!), it is cogent enough for us to explore with code..

## Design so far:

To keep it organied and neat, object orientation paradigm is used. The code is contained in the class 'CandPrimes', a short form for 'Candidate Primes'. This class contains methods to sieve the numbers and extract primes, and create the candidate prime set as a finite array of numbers. The diagram below describes this class:


The code is:
```python
class CandPrimes:
    def __init__(self):
        self.primes=[2] #first prime
        self.pattern = [1,2] # the pattern 1,(1)* is stored in an array 

    
    def getNextPattern(self):
        #now the new pattern
        #algorithm: New pattern is first element and a repeating group (rg). The sum of the rg = primeFactorial
        #ex: For 2, the pattern is [1,2]
        #To get the next pattern
        # 1. Add the first element to the prime list. 
        # 2. get the repeating group (everthing except the first element)
        # 3. expand the rg  * new Prime (i.e. goes up to the prime factorial)
        # 4. Process the rg to remove candPrimes divisible by the new prime and this forms the new pattern
        nP=self.primes[-1]+self.pattern[0]
        self.primes.append(nP) # 1
        rg=self.pattern[1:] #2
        tempRg=[]
        for i in range(nP): #3
            tempRg.extend(rg)
        tempRg.append(tempRg[0])
        #print(f'tempRg = {tempRg}')
        #4. eliminate the non-primes
        cp=nP
        npmPrimeIdx=[]
        for idx,cpg in enumerate(tempRg):
            cp +=cpg
            #print(f'cp={cp}')
            if cp%nP==0:
                npmPrimeIdx.append(idx)
                #print(f'cp={cp}, nP={nP}, idx={idx}')
        print(f'npmPrimeIdx:len: {len(npmPrimeIdx)} for prime {nP} with primeFactorial: {self.getPrimeFactorial()}')
        for i in reversed(npmPrimeIdx): #delete in reverse direction
            tempRg[i+1] += tempRg[i]
            del tempRg[i]
        self.pattern=tempRg
        print(f'nextPattern = {self.patternStr()}')
        #print(f'patternStr={tempRg}')

    def getPrimeFactorial(self):
        #returns product of all primes (in self.primes)
        pf=1
        for p in self.primes: pf *=p
        return pf
    
    def patternStr(self):
        #get a printable representation of the pattern
        pat=self.pattern
        p=self.primes[-1]
        if len(pat)<2: msg= f'Prime: {p} has Invalid Pattern: {pat}'
        msg = f'Prime: {p} has ({pat[0]},({pat[1:]})*)'
        return msg
    
    @staticmethod
    def test(args):
        #usage python3 candPrimes.py
        # This one prints the candidate prime patters for 3 primes beyond 2 (3,5,7)

        CP=CandPrimes()
        for i in range(3):
            CP.getNextPattern()

if __name__=='__main__':
    import sys
    args = sys.argv
    CandPrimes.test(args)
```

A static test method is created in the class to check on our patterns. Running this program produces the candidate prime patterns as shown below:

```
Pattern (1,([2])*) 
for Prime: 2 has Length = 2 that repeats every 2
 
Pattern (2,([2, 4])*) 
for Prime: 3 has Length = 3 that repeats every 6
 
Pattern (2,([4, 2, 4, 2, 4, 6, 2, 6])*) 
for Prime: 5 has Length = 9 that repeats every 30
 
Pattern (4,([2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2, 10])*) 
for Prime: 7 has Length = 49 that repeats every 210

```

Now we have gotten thru this code, we can continue our experiments..

## Experiment #1: Validate this pattern by printing all primes below 100.
To do this, observe that the first number eliminated from the candidate prime list by a prime is that prime\*prime. Ex: 3 elminates candidate primes from 9 onwards: i.e. 9,15..
Therefore if we find the pattern for primes < 10\*10 we should be able to find all primes below 100. 
The design is to add a member function getPrimesUptoN as shown below:


```python

## Experiment #1:

    def getPrimesUptoN(self,N):
        #gets all prime number upto N
        maxP = int(math.sqrt(N))
        while self.primes[-1] < maxP:
            self.getNextPattern()
        self.printPrimesUptoN(N)

    def printPrimesUptoN(self,N):
        print(f'Primes: {self.primes}')
        sCP=self.primes[-1]
        primeArr = self.primes[:]
        for cpg in self.pattern:
            sCP +=cpg
            if sCP > N: break
            primeArr.append(sCP)
        print(f'NoOfPrimes = {len(primeArr)} \n primes: {",".join(map(str,primeArr))}')
```
Output of this is:
```
Primes: [2, 3, 5, 7, 11]
NoOfPrimes = 25 
 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
```
Which turns out to be correct!

## Experiment 2: Let us use this to calculate the primes upto 1000.
When we try this with the above code, the machine hangs - i.e. keeps computing. A quick review indicates that it is computing the pattern and the pattern is of length on the order of prime factorial.  The output line:
```
for Prime: 22 has Length = 1658881 that sums to 9699694
```
shows a pattern length of 1658881!  The 'sums to 9699694' indicates that we have been computing the pattern to almost 10 million, when calculating primes upto only 1000!
Experiment 2 failed! We will leave this as is now, and proceed to further experiments..

## Experiment 3: How many candidate primes does the new prime eliminate? 
To explain: The sieving process is an elimination game. Each prime eliminates all its multiples from becoming primes. The first prime number 2 eliminates half the numbers. Does the inclusion of the next prime number (3) result in the elimination of 1/3 of the remaining numbers?
So we want to know if including the next prime p results in the elimination of 1/p of the remaining numbers? Intuitively this seems plausible and let us verify by experiment.
We code a couple of methods and add a member as below:

Method modified:

```python
def getNextPattern(self):
    ...
    self.noOfcandPrimesEliminated= len(npmPrimeIdx)

#member added
    def getFraction(self,noOfPrimes):
        #Gets fraction of cprimes divisible by the first one (i.e. the first real prime)or 
        for i in range(noOfPrimes):
            self.getNextPattern()
            np=self.primes[-1] #new prime
            lrg = len(self.pattern) -1 #length of regular pattern (1st element is a prime and not part of regular patter of candidate primes)
            elimF = self.noOfcandPrimesEliminated*100 / (lrg+self.noOfcandPrimesEliminated)
            print(f'Prime Elimination Fraction for {np} = {elimF}, expected = 100/{np}, '
                f'%diff = {elimF - 100/np} %')

```

Running this code results in:

```
nextPattern = for Prime: 3 pattern has Length = 3 that sums to 8
 
Prime Elimination Fraction for 3 = 33.333333333333336, expected = 100/3, %diff = 0.0 %
for Prime: 3 pattern has Length = 3 that sums to 8
 
nextPattern = for Prime: 5 pattern has Length = 9 that sums to 32
 
Prime Elimination Fraction for 5 = 20.0, expected = 100/5, %diff = 0.0 %
for Prime: 5 pattern has Length = 9 that sums to 32
 
nextPattern = for Prime: 7 pattern has Length = 49 that sums to 214
 
Prime Elimination Fraction for 7 = 14.285714285714286, expected = 100/7, %diff = 0.0 %
for Prime: 7 pattern has Length = 49 that sums to 214
 
nextPattern = for Prime: 11 pattern has Length = 481 that sums to 2312
 
Prime Elimination Fraction for 11 = 9.090909090909092, expected = 100/11, %diff = 0.0 %
for Prime: 11 pattern has Length = 481 that sums to 2312
 
nextPattern = for Prime: 13 pattern has Length = 5761 that sums to 30034
 
Prime Elimination Fraction for 13 = 7.6923076923076925, expected = 100/13, %diff = 0.0 %
for Prime: 13 pattern has Length = 5761 that sums to 30034
 
nextPattern = for Prime: 17 pattern has Length = 92161 that sums to 510512
 
Prime Elimination Fraction for 17 = 5.882352941176471, expected = 100/17, %diff = 0.0 %
for Prime: 17 pattern has Length = 92161 that sums to 510512
 
nextPattern = for Prime: 19 pattern has Length = 1658881 that sums to 9699694
 
Prime Elimination Fraction for 19 = 5.2631578947368425, expected = 100/19, %diff = 0.0 %
```
Eureka! The differce between the actual and expected is 0%! So yes..Each new prime p eliminates 1/p of the remaining candidate primes.

Success!

## Experiment 4: How many TWIN candidate primes does the new prime eliminate? 

Considering twin primes (primes separated by 2). In twin primes two primes are involved. It seems plausible that new primes will eliminate have a chance at eliminating either of these two.. It cannot eliminate both, since the difference is 2 and the new prime is bigger than 2.  So we propose that each prime p eliminates 2/p of the candidate twin primes.
Let's do  this experiment with code changes for addint one member and a method:

Method modified:

```python
    @staticmethod
    def getRawPattern(nP:int,rg:list)->list:
        #expands the rg np timess and appends the first element to the end
        #First element is appended, since tempRg[0] becomes the next Prime
        #Appending it to the end, completes the next rg 
        tempRg=[]
        for i in range(nP): #3
            tempRg.extend(rg)
        tempRg.append(tempRg[0])
        return tempRg

#member added
    def calcNumberOfTwinPrimes(self,noOfPrimes):
        def countTps(gaps:list):
            noOfCandTP=0
            for gap in gaps: 
                if gap==2: noOfCandTP +=1
            return noOfCandTP
        
        for i in range(noOfPrimes):
            noOfCandTP=0
            rg = self.pattern[1:]
            nP = self.primes[-1]+self.pattern[0]
            tempRg = self.getRawPattern(nP,rg)
            twinPrimesInRawPattern = countTps(tempRg)
            self.getNextPattern()
            twinPrimesAfterElimination = countTps(self.pattern)
            pctEliminated = (twinPrimesInRawPattern - twinPrimesAfterElimination) * 100/twinPrimesInRawPattern
            pctExpected = 2*100/nP
            print(f'For prime {nP} twinPrimesBeforeElimination = {twinPrimesInRawPattern}, after = {twinPrimesAfterElimination}'
                  f' %Eliminated = {pctEliminated}, expected = {pctExpected}')

```
Running this code results in:

```
for Prime: 2 pattern has Length = 2 that sums to 3
 
nextPattern = for Prime: 3 pattern has Length = 3 that sums to 8
 
For prime 3 twinPrimesBeforeElimination = 3, after = 1 %Eliminated = 66.66666666666667, expected = 66.66666666666667
for Prime: 3 pattern has Length = 3 that sums to 8
 
nextPattern = for Prime: 5 pattern has Length = 9 that sums to 32
 
For prime 5 twinPrimesBeforeElimination = 5, after = 3 %Eliminated = 40.0, expected = 40.0
for Prime: 5 pattern has Length = 9 that sums to 32
 
nextPattern = for Prime: 7 pattern has Length = 49 that sums to 214
 
For prime 7 twinPrimesBeforeElimination = 21, after = 15 %Eliminated = 28.571428571428573, expected = 28.571428571428573
for Prime: 7 pattern has Length = 49 that sums to 214
 
nextPattern = for Prime: 11 pattern has Length = 481 that sums to 2312
 
For prime 11 twinPrimesBeforeElimination = 165, after = 135 %Eliminated = 18.181818181818183, expected = 18.181818181818183
for Prime: 11 pattern has Length = 481 that sums to 2312
 
nextPattern = for Prime: 13 pattern has Length = 5761 that sums to 30034
 
For prime 13 twinPrimesBeforeElimination = 1755, after = 1485 %Eliminated = 15.384615384615385, expected = 15.384615384615385
for Prime: 13 pattern has Length = 5761 that sums to 30034
 
nextPattern = for Prime: 17 pattern has Length = 92161 that sums to 510512
 
For prime 17 twinPrimesBeforeElimination = 25245, after = 22275 %Eliminated = 11.764705882352942, expected = 11.764705882352942
for Prime: 17 pattern has Length = 92161 that sums to 510512
 
nextPattern = for Prime: 19 pattern has Length = 1658881 that sums to 9699694
 
For prime 19 twinPrimesBeforeElimination = 423225, after = 378675 %Eliminated = 10.526315789473685, expected = 10.526315789473685
Experiment 4 completed..
```
Eureka! The differce between the actual and expected is 0%! So yes..Each new prime p eliminates 2/p of the remaining candidate twin primes.

Success!

Now take a moment and reflect on Experiment #4. For twin patterns, the elimination pattern is 2/p, which is very similar to 1/p.  We know that infinite prime numbers exist. So this similarity in pattern implies that infinite twin primes exist!
Not only that, this method can be used to predict that primes separated by every even number exists infinitely!
Voila! Have we solved one of the most troublesome conjectures in Math? Has the slithering Python successfully weaved all around the number system?

## Experiment #5: Maximum Gap between prime numbers

This is an experiment to see how the gaps between primes behaves/increases. We see from the gap pattern of candidate primes (exxperiment #1), that every succesive prime simply removes one or more candidate primes, causing the gap to widen to the the sum of the gap prior and post to that candidate prime that was removed. Ex: for prime 3, the gap pattern is 2,2,4,2,4,2,4.. (i.e. candidate primes are 3+2,3+2, 3+4..). Now the next prime removes 25 from this pattern, and gap there between 23 and 25 now becomes the sum of gaps 2 and 4 = 6, and the next candidate prime becomes 29 instead of 25. This experiment finds the max gap between candidate primes and compares them with the max possible which is twice the previous maximum gap.

Another aspect of experiment 5, is that the first candidate prime that can be removed by a new prime (i.e. divisible by the new prime) is (new prime) squared. This difference between X and X squared is greater than 2x for all x>2. So if this gap must be less than the square of the prime.

Here is the result of experiment #5:

```
seq: 1, prime = 2, maxGap = 2, primeSqr = 4, 2^seq = 2, maxGap/prime = 1.0
seq: 2, prime = 3, maxGap = 4, primeSqr = 9, 2^seq = 4, maxGap/prime = 1.3333333333333333
seq: 3, prime = 5, maxGap = 6, primeSqr = 25, 2^seq = 8, maxGap/prime = 1.2
seq: 4, prime = 7, maxGap = 10, primeSqr = 49, 2^seq = 16, maxGap/prime = 1.4285714285714286
seq: 5, prime = 11, maxGap = 14, primeSqr = 121, 2^seq = 32, maxGap/prime = 1.2727272727272727
seq: 6, prime = 13, maxGap = 22, primeSqr = 169, 2^seq = 64, maxGap/prime = 1.6923076923076923
seq: 7, prime = 17, maxGap = 26, primeSqr = 289, 2^seq = 128, maxGap/prime = 1.5294117647058822
```

What is that last part of the the result 'maxGap/prime'? That is the point of this whole article. Using python we can speculate and calculate! 
The speculation is that when the maxGap falls below the prime, then from then on, the next prime must be between this prime and twice its value. This is an old conjecture, and here we have an opportunity to continue this sequence to see if that happens. Unfortunately in this version of Python, either number precision or the length of the pattern maxed out at prime = 17 and the program is 'hanging' there! So it remains a mystery and may even be a low hanging fruit if we move on to numpy to handle larger numbers or find a way to compress the pattern.

## Experiment #6: Finding the length of the repeating pattern

From experiment 1, we see that the pattern for prime X looks like n(a,b,c,..)* and a+b+c+..= prime factorial for X
So this experiment is to find length of the pattern.  The logic is like this: each prime eliminates 1/prime in the pattern. Ex: for 5, the pf(5)=2*3*5 = 30 => 15 eliminated by 2, of remaining 15 => 5 eliminated by 3, of remaining 10 2 eliminated by 5 which gives a pattern length 30-15-5-2 = 8. Verify this with experiment #1: 
Pattern for 5  (2,([4, 2, 4, 2, 4, 6, 2, 6])*) and we notice that the repeating pattern length is 8

Following this method here is length of the pattern for primes < 100

## Experiment #6: Compressing the Pattern

With each successive prime X, elimination in the candidate pattern start at X^2 and all X*Y where Y is a candidate prime > X. This forms the new list of candidate primes. What if this 'elimination' step itself is represented as a pattern? What if we can get a cascade of patterns instead of one pattern for each prime? The number of cascades will be the sequence number of the prime.  Ex: 
2 will have a cascade of only 1 pattern which is 1,(2)*
3 will have cascade of 2,(2)* and (2) instead of 2(2,4)*
5 will have cascades of 2,(2)*, (2), (6,2) instead of (2,([4, 2, 4, 2, 4, 6, 2, 6])*)

To derive the pattern for 5:
2,(2)*->2(2,2,2..=(2)=> 2,(2,4) =(6,3)=> 2,(4,2,4,2,4,x2,4,2,x4,2)->2(4,2,4,2,4,6,2,6)->2((4,2)(2),(6,2,6))*

Way to create a new pattern:
1. remove the 1st one in the repeating pattern and put it outside, and add it to the end:
2,(2,4) => 2(4,2)*
2. Get the x^2, Find the number of repeats to get to x^2 minus 1 => so the pattern is (4,2)(2) 

Now let us wait for the Greeks (i.e. formal proof using greek characters) to follow the path of the Python!

Appendix I: The complete code..

```python
import math
class CandPrimes:
    def __init__(self):
        self.primes=[2] #first prime
        self.pattern = [1,2] # the pattern 1,(1)* is stored in an array 
    
    @staticmethod
    def getRawPattern(nP:int,rg:list)->list:
        #expands the rg np timess and appends the first element to the end
        #First element is appended, since tempRg[0] becomes the next Prime
        #Appending it to the end, completes the next rg 
        tempRg=[]
        for i in range(nP): #3
            tempRg.extend(rg)
        tempRg.append(tempRg[0])
        return tempRg

    def getNextPattern(self):
        #now the new pattern
        #algorithm: New pattern is first element and a repeating group (rg). The sum of the rg = primeFactorial
        #ex: For 2, the pattern is [1,2]
        #To get the next pattern
        # 1. Add the first element to the prime list. 
        # 2. get the repeating group (everthing excep the first element)
        # 3. expand the rg  * new Prime (i.e. goes up to the prime factorial)
        # 4. Process the rg to remove candPrimes divisible by the new prime and this forms the new pattern
        #print(f'{self.patternStr()}')
        nP=self.primes[-1]+self.pattern[0]
        self.primes.append(nP) # 1
        rg=self.pattern[1:] #2
        tempRg=CandPrimes.getRawPattern(nP,rg)
        #print(f'tempRg = {tempRg}')
        #4. eliminate the non-primes
        cp=nP
        npmPrimeIdx=[]
        for idx,cpg in enumerate(tempRg):
            cp +=cpg
            #print(f'cp={cp}')
            if cp%nP==0:
                npmPrimeIdx.append(idx)
                #print(f'cp={cp}, nP={nP}, idx={idx}')
        #print(f'npmPrimeIdx:len: {len(npmPrimeIdx)} for prime {nP} with primeFactorial: {self.getPrimeFactorial()}')
        for i in reversed(npmPrimeIdx): #delete in reverse direction
            tempRg[i+1] += tempRg[i]
            del tempRg[i]
        self.pattern=tempRg
        #print(f'nextPattern = {self.patternStr()}')
        self.noOfcandPrimesEliminated= len(npmPrimeIdx)  #keep track of number of Candidate Primes eliminated in the pattern because they are divisible by the new prime.


    def getPrimeFactorial(self):
        #returns product of all primes (in self.primes)
        pf=1
        for p in self.primes: pf *=p
        return pf
    
    def patternStr(self,verbose=False):
        #get a printable representation of the patterncprimes
        pat=self.pattern
        p=self.primes[-1]
        if len(pat)<2: msg= f'Prime: {p} has Invalid Pattern: {pat}'
        sum=0
        for cp in self.pattern[1:]:
            sum +=cp
        if verbose:
            msg = f'Pattern ({pat[0]},({pat[1:]})*) \nfor Prime: {p} has Length = {len(self.pattern)} that repeats every {sum}\n '
        else:
            msg = f'for Prime: {p} pattern has Length = {len(self.pattern)} that repeats every {sum}\n '
        return msg
    #experiments:
    #Experiment #1:

    def getPrimesUptoN(self,N):
        #gets all prime number upto N
        maxP = int(math.sqrt(N))
        while self.primes[-1] < maxP:
            self.getNextPattern()
        self.printPrimesUptoN(N)

    def printPrimesUptoN(self,N):
        print(f'Primes: {self.primes}')
        sCP=self.primes[-1]
        primeArr = self.primes[:]
        for cpg in self.pattern:
            sCP +=cpg
            if sCP > N: break
            primeArr.append(sCP)
        print(f'NoOfPrimes = {len(primeArr)} \n primes: {",".join(map(str,primeArr))}')

    #Experiment #3:
    def getFraction(self,noOfPrimes):
        #Gets fraction of cprimes divisible by the first one (i.e. the first real prime)or 
        for i in range(noOfPrimes):
            self.getNextPattern()
            np=self.primes[-1] #new prime
            lrg = len(self.pattern) -1 #length of regular pattern (1st element is a prime and not part of regular patter of candidate primes)
            elimF = self.noOfcandPrimesEliminated*100 / (lrg+self.noOfcandPrimesEliminated)
            print(f'Prime Elimination Fraction for {np} = {elimF}, expected = 100/{np}, '
                f'%diff = {elimF - 100/np} %')
        
    #Experiment #4:
    def calcNumberOfTwinPrimes(self,noOfPrimes):
        def countTps(gaps:list):
            noOfCandTP=0
            for gap in gaps[1:]: 
                if gap==2: noOfCandTP +=1
            return noOfCandTP
        
        for i in range(noOfPrimes):
            noOfCandTP=0
            rg = self.pattern[1:]
            nP = self.primes[-1]+self.pattern[0]
            tempRg = self.getRawPattern(nP,rg)
            twinPrimesInRawPattern = countTps(tempRg)
            self.getNextPattern()
            twinPrimesAfterElimination = countTps(self.pattern)
            pctEliminated = (twinPrimesInRawPattern - twinPrimesAfterElimination) * 100/twinPrimesInRawPattern
            pctExpected = 2*100/nP
            print(f'For prime {nP} twinPrimesBeforeElimination = {twinPrimesInRawPattern}, after = {twinPrimesAfterElimination}'
                  f' %Eliminated = {pctEliminated}, expected = {pctExpected}')

    @staticmethod
    def test(args):
        expToDo=0
        CP=CandPrimes()
        match expToDo:
            case 4:
                CP.calcNumberOfTwinPrimes(7)
            case 3:
                CP.getFraction(7)
            case 1:
                CP.getPrimesUptoN(100)
            case 2:
                CP.getPrimesUptoN(1000)
            case 0:
                print(CP.patternStr(True))
                for i in range(3):
                    CP.getNextPattern()
                    print(CP.patternStr(True))
            case _:
                print(f'**Error: Experiment {expToDo} not implemented')
        print(f'Experiment {expToDo} completed..')


if __name__=='__main__':
    import sys
    args = sys.argv
    CandPrimes.test(args)
```

## Gedanken

Some thoughts on gaps to the next prime.
The gap between two consecutive primes cannot be a prime. The gap is even etc.  What this implies is that a new prime cannot eliminate the next candidate prime. Continuing on, the first candidate prime a number eliminates is its square. Therefore there must be a prime number between a prime and its square!