class CandPrimes:
    def __init__(self, noOfPrimes,rangeMax: int):
        self.max=rangeMax
        self.primes=[2] #first prime
        self.pattern = [1,1] # the pattern 1,(1)* is stored in an array 
        self.noOfPrimes = noOfPrimes #number of real primes to calculate and then use for candidate primes
        for i in range(self.noOfPrimes):
            self.primes.append(self.getNextPrime())

    def getCandPrimesUntilN(self,rangeMax: int):
        #finds candidate primes using self.primes
        npr=self.primes[-1]
        cprimes=[]
        for i in range(self.primes[-1],rangeMax+1):
            npr=self.getNextPrime(startAt=npr+1)
            cprimes.append(npr)
        self.newPrime=cprimes[0] #this is a real prime
        return cprimes
    
    def getCandTwinPrimesUntilN(self,rangeMax:int):
        #find candidate twin primes using self.primes
        cTwinPrimes=[]
        cprimes=self.getCandPrimesUntilN(rangeMax)
        for idx,p in enumerate(cprimes[1:]):
            if p - cprimes[idx] ==2:
                cTwinPrimes.append((cprimes[idx],p))
        return cTwinPrimes
    
    def getFractionOfTwinPrimes(self,rangeMax):
        #Gets fraction of cprimes divisible by the first one (i.e. the first real prime)
        numerator=0
        cTwinPrimes=self.getCandTwinPrimesUntilN(rangeMax)
        fp= self.newPrime
        numerator=0
        for tp in cTwinPrimes:
            if tp[0] % fp ==0 or tp[1] % fp ==0: 
                numerator +=1
                #print(f'Knocked out {tp}')
                continue
        
        print(f'Twin Prime Elimination Fraction = {numerator}/{len(cTwinPrimes)}, expected = {2}/{fp}, '
            f'%diff = {fp*(numerator/len(cTwinPrimes) - 2/fp)*100} %'
            f'\nPrimes:\n{",".join(map(str, self.primes))}')
        


    def getFraction(self,cprimes):
        #Gets fraction of cprimes divisible by the first one (i.e. the first real prime)
        numerator=0
        fp = self.newPrime
        for p in cprimes:
            if p % self.newPrime ==0:numerator+=1
        print(f'Prime Elimination Fraction = {numerator}/{len(cprimes)}, expected = 1/{fp}, '
              f'%diff = {fp*(numerator/len(cprimes) - 1/fp)*100} %')

    def getNextPrime(self,startAt=-1):
        if startAt<0:
            startAt = self.primes[-1]+1
        curNo=startAt
        while True:
            found=True
            for p in self.primes:
                if curNo%p == 0: 
                    found=False
                    curNo+=1
                    break
            if found: 
                return curNo
        
    def getPrimeFactorial(self):
        pf=1
        for p in self.primes: pf *=p
        return pf
    
    def patternStr(self):
        pat=self.pattern
        p=self.primes[-1]
        if len(pat)<2: msg= f'Prime: {p} has Invalid Pattern: {pat}'
        msg = f'Prime: {p} has ({pat[0]},({pat[1:]})*)'
        return msg
    
    def printPrimes(self):
        print(f'Primes: {self.primes}')
        sCP=self.primes[-1]
        pStr=''
        noOfPrimes = len(self.primes)
        primesPerLine=20
        for cpg in self.pattern:
            sCP +=cpg
            pStr +=f'{sCP}, '
            noOfPrimes +=1
            if noOfPrimes % primesPerLine ==0:
                print(f'CandPrimes({primesPerLine}) = {pStr} \n ')
                pStr=''
            if noOfPrimes==100: break
        print(f'CandPrimes = {pStr} \n ')

    def calcNumberOfTwinPrimes(self):
        noOfRealTP=0
        for idx,p in enumerate(self.primes):
            if idx==0: continue
            if p - self.primes[idx-1] ==2 : noOfRealTP +=1
        noOfCandTP =0
        for cpg in self.pattern: 
            if cpg==2: noOfCandTP +=1
        print(f'noOfRealTP= {noOfRealTP}; noOfCandTP= {noOfCandTP}, :: lastPrime = {self.primes[-1]} primeFactorial = {self.getPrimeFactorial()}')        


    
    def getNextPattern(self):
        #now the new pattern
        #algorithm: New pattern is first element and a repeating group (rg). The sum of the rg = primeFactorial
        #ex: For 2, the pattern is [1,2]
        #To get the next pattern
        # 1. Add the first element to the prime list. 
        # 2. get the repeating group (everthing excep the first element)
        # 3. expand the rg  * new Prime (i.e. goes up to the prime factorial)
        # 4. Process the rg to remove candPrimes divisible by the new prime and this forms the new pattern
        print(f'{self.patternStr()}')
        nP=self.primes[-1]+self.pattern[0]
        self.primes.append(nP) # 1
        rg=self.pattern[1:] #2
        tempRg=[]
        for i in range(nP): #3
            tempRg.extend(rg)
        tempRg.append(tempRg[0])
        print(f'tempRg = {tempRg}')
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

    
    def getPrimeGaps(self):
        #Start with 2,2,2, and add each adjacent until prime factorial
        self.getNextPattern()
        
        # self.primes.append(nP)
        # pf=self.getPrimeFactorial()

        # 1=>1,1,1,1=>1,1,1=>1,2=>2
        # (2=>2,3,4,5=>3,4,5=>3,5)
        # 2=>2,2,2,2,2=>2,2,2,2=>2,2,4 #pattern after 3


        # 1=>1,1,1=>1,1=>2
        # 2=>2,2,2,2=>2,2,2=>
        #  2,4, 2,6,4,2,4,2
        # 5,7,11,13,17

    
    @staticmethod
    def test(args):
        #usage python3 candPrimes.py noOfPrimes rangeMax
        noOfPrimes,rangeMax=0,1000
        if len(args) > 1: noOfPrimes=int(args[1])
        if len(args) > 2: rangeMax=int(args[2])
        if len(args) > 3: maxNoOfPrimes=int(args[3])
        CP=CandPrimes(noOfPrimes,rangeMax)
        CP.pattern=[2,2,4]
        CP.primes=[2,3]
        for i in range(maxNoOfPrimes):
            CP.getPrimeGaps()
        CP.printPrimes()
        CP.calcNumberOfTwinPrimes()
        exit(0)
        #print(f'Primes:\n{",".join(map(str, CP.primes))}')
        cprimes = CP.getCandPrimesUntilN(rangeMax)
        #print(f'Candidate Primes of {CP.primes[-1]}:\n{",".join(map(str,cprimes ))}')
        CP.getFraction(cprimes)
        cTwinPrimes=CP.getCandTwinPrimesUntilN(rangeMax)
        #print(f'Twin Candidate Primes of {CP.primes[-1]}:\n{",".join(map(str,cTwinPrimes ))}')
        CP.getFractionOfTwinPrimes(rangeMax)

if __name__=='__main__':
    import sys
    args = sys.argv
    CandPrimes.test(args)
