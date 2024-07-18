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
            elimF = self.noOfcandPrimesEliminated*100/(lrg+self.noOfcandPrimesEliminated)
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
            pctEliminated = (twinPrimesInRawPattern-twinPrimesAfterElimination)*100/twinPrimesInRawPattern
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
