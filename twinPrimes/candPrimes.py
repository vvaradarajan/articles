import math
from enum import Enum
from collections import deque

def noprint(*args):
    pass

class SeqGen:
    #Class that generates a new pattern, given the elements to be deleted on a rotating pattern
    #The elements to be deleted are indexed by element order, and the value is the cycle in which
    #it should be deleted
    def __init__(self,p:int,ng:int,patt:list[int]):
        #p=prime, ng=next gap, patt = pattern: example in patt for 3 = 2(2,4)*, p=3,ng=2,patt=[2,3]
        self.p,self.ng,self.patt = p,ng,patt
        #calc the next pattern
        #self.repCount,self.nng,self.patt,self.delList=SeqGen.calcDelList(p,ng,patt)
        # #self.patt=self.patt[1:]+self.patt[:1]
        # self.iLen =len(self.patt)
        # self.nLen = self.iLen*(self.repCount-1)
        # if len(self.delList) != self.iLen:
        #     raise ValueError('Error: inpPattern length){self.iLen} != delList length ({len(delList)})')
        # #inverse the delList (repcount:elemOrder to delete)
        # if self.delList[0]==0:
        #     raise ValueError('Error: Cannot delete the 0th element in the 0th rep!')
        # #flatten delList
        # noprint(f'delList={self.delList}\nsum(delList)={sum(self.delList)}')
        # self.delList = [idx+cn*self.iLen for idx,cn in enumerate(self.delList)]
        # self.delList.sort()
        #print(f'patt:{patt}')
        #print(f'self.delList={self.delList}')

    def getNewPattern(self,sort=False):
        newPatt=[None]*self.nLen #create an array of defined length
        nIdx=0
        dIdx=0
        kstart=0
        for i in range(self.repCount):  
            k=kstart
            kstart=0
            while k < self.iLen:
                #print(f'i={i},K={k},nIdx={nIdx},dIdx={dIdx},newPatt={newPatt}')
                if self.delList[dIdx] ==k+i*self.iLen:
                    if k+1==self.iLen:
                        toAdd = self.patt[0]
                        kstart = 1
                    else: toAdd=self.patt[k+1]
                    newPatt[nIdx] = self.patt[k]+ toAdd
                    k+=1
                    dIdx+=1
                    #self.delList[dIdx] -=1 #compensate for zeroing out k
                else:
                    try:
                        newPatt[nIdx] = self.patt[k]
                    except IndexError:
                        print(f'i={i},K={k},nIdx={nIdx},dIdx={dIdx},self.iLen={self.iLen}, self.nLen={self.nLen}')
                        #raise
                nIdx +=1
                k+=1
                #print(f'K={k},nIdx={nIdx},dIdx={dIdx},newPatt={newPatt}')
        #update self
        self.p +=self.ng
        return self.repCount,self.nng,newPatt
    
    @staticmethod
    def calcDelList(p:int,ng:int,patt:list[int])->tuple[int,int,list[int],list[tuple[int,int]]]:
        #returns np:next prime (or repCount), nng:next prime gap, patt: new pattern that is to repeated repcount times
        #delList: The elements in the new pattern that should be deleted.
        #This is a short form of a long pattern
        #ex: input 3,2,[2,4] -> 5,2,[4,2],[4,2 => [4,2]*3 ,,=>[4,2,4,2,4,2], next is "[4, 2, 4, 2, 4, 6, 2, 6]"
        #delList indicates the nth repitition of the element in the
        #pattern that is to be eliminated
        np=p+ng #The new prime
        nng=patt[0] #get the first element of the pattern as the new next gap
        patt=patt[1:]+patt[0:1] #the new pattern that is to be replicated
        #The dellist is a list of tuples[pattNo,elmntNo] that should be eliminated
        delList=[]
        repCount=np
        sPatt = sum(patt)
        sNewPatt = sPatt*repCount
        #start with square of np and multiples of np from the pattern
        ncp = np
        elimC = ncp*np - (np+nng)
        elimCIdx = 0
        print(f'elimC={elimC},sPatt={sPatt}, sNewPatt={sNewPatt}')
        while sNewPatt > elimC:
            pattIdx = 0 # Go thru multiple of each prime
            pattNo,rem = divmod(elimC,sPatt)
            noprint(f'pattNo,rem:{pattNo},{rem},elimC={elimC},sNewPatt={sNewPatt}')
            #Now find the index within patt pat of rem
            if rem==0:
                delList.append((pattNo-1,len(patt)-1))
            else:
                sRem = 0 #reminder sought
                for idx,n in enumerate(patt):
                    sRem +=n
                    noprint(f'sRem,rem = {sRem},{rem}')
                    if sRem==rem: #found element
                        delList.append((pattNo,idx))
                        break
            #eliminate beyond the square (multiples of candidatePrimed * np)
            if ncp == np:
                ncp += nng 
            else:
                ncp +=patt[elimCIdx]
                elimCIdx +=1

            elimC = ncp*np - (np+nng)

        noprint(f'DelList: np={np}, nng={nng}\npatt={patt},delList={delList}')
        return np,nng,patt,delList 
    
    @staticmethod
    def getPatternUsingDelList(p,patt:list[int],delList:list[tuple[int,int]]) -> list[int] :

        wPatt=deque(patt[:]) #make a copy. This will be rotated as elements are eliminated
        lpatt = len(patt)
        liRemoveIdx = [t[0]*lpatt+t[1] for t in delList ]
        nToRemove = len(liRemoveIdx)
        
        for i in range(nToRemove -1,0,-1):
            liRemoveIdx[i] -= liRemoveIdx[i-1]+1 #make list incremental
        #now do the CRC (copy, rotate copy)
        lNewpatt = lpatt*p- nToRemove
        newPatt:list[int]=[0]*(lNewpatt) #
        nIdx=0 #index into lNewpatt
        wIdx=0 #index into patt
        def adjIdx():
            nonlocal wIdx,nIdx
            if wIdx == lpatt : wIdx=0
            #if nIdx == lNewpatt: nIdx=0
        def copyN(n): #copy n elements from wpatt to newPatt
            nonlocal wIdx,nIdx
            adjIdx()
            for i in range(n):
                newPatt[nIdx]=wPatt[wIdx]
                wIdx +=1
                nIdx +=1
                adjIdx()

        for rIdx,n in enumerate(liRemoveIdx):
            if rIdx > 0: n = n-1  #except first, rest must be one less because of consolidation with next wPatt
            copyN(n)
            #consolidate the gap when an element is removed
            noprint(f'Vasan: n={n},newPatt={newPatt},nIdx={nIdx},wIdx={wIdx},liRemoveIdx: {liRemoveIdx}')
            #if nIdx == lNewpatt: nIdx -=1 #Handle the last element replacement,
            newPatt[nIdx] =wPatt[wIdx] + (wPatt[wIdx+1] if wIdx<lpatt-1 else wPatt[0])
            wIdx = wIdx+2-lpatt if wIdx+2>lpatt-1 else wIdx + 2 #skip where entry was deleted
            noprint(f'Vasan: n={n},newPatt={newPatt},nIdx={nIdx},wIdx={wIdx},liRemoveIdx: {liRemoveIdx}')
            nIdx +=1
        #Tail end copy
        if nIdx < lNewpatt:
            for i in range(nIdx,lNewpatt):
                newPatt[i]=wPatt[wIdx]
                wIdx = 0 if wIdx == lpatt -1 else wIdx +1 
        noprint(f'newPatt:{wPatt}, elements_to_remove: {liRemoveIdx}')

        return newPatt

    
    @staticmethod
    def printPattern(p:int,ng:int,patt:list[int]) -> list[str]:
        #takes the prime, next gap, pattern and prints prime and array of plen gaps
        plen,curIdx=22,0
        stPrime = p+ng
        pStr=[]
        loopOver=True
        patLen=len(patt)
        while loopOver:
            lIndex = curIdx+plen
            if  lIndex >= patLen:
                loopOver=False
                lIndex = patLen
            gArr = patt[curIdx:curIdx+plen]
            pStr.append(f'{stPrime}{gArr}')
            stPrime += sum(gArr)
            curIdx +=len(gArr)
        return pStr
    
    @staticmethod
    def gapStats(p:int,patt)-> dict:
        gapCounts={}
        mg = 0
        sum=p
        nGapn=0
        for x in patt:
            if x in gapCounts:
                gapCounts[x] +=1
            else: gapCounts[x]=1
            if x>mg: mg=x
            sum +=x
        return {'mg':mg,'gapCounts': gapCounts}

    @staticmethod
    def test():
        #sq=SeqGen(3,2,[2,4])
        '''
        2: 2,1,[2]*
        3: 3,2,[2,4]*
        5: 5,2,[4, 2, 4, 2, 4, 6, 2, 6]*
        '''
        np,nng,patt,delList = SeqGen.calcDelList(2,1,[2])
        for i in range(6):
            patt=SeqGen.getPatternUsingDelList(np,patt,delList)
            #create the candidate prime array
            cpArr=[0]*len(patt)
            cpArr[0]=np+nng+patt[0]
            for i in range(1,len(patt)): cpArr[i] +=cpArr[i-1]+patt[i]
            print(f'NewPatt: {np},{nng},{patt[:50]}\n{cpArr[0:50]}')
            np,nng,patt,delList = SeqGen.calcDelList(np,nng,patt)
            #print some counts to check with google
            if cpArr[-1] > 200:
                pIn100 = sum(1 for x in cpArr if x<100)
                pIn200 = sum(1 for x in cpArr if x<200)
                print(f'pIn100={pIn100}; pIn200={pIn200}')
        return
        #sq=SeqGen([2, 4, 2, 4, 6, 2, 6,4],[4,4,2,5,6,4,5],7)
        np,ng,patt = sq.getNewPattern() #n= nextPrime, ng = gap after np, patt=pattern
        print(f'NewPattern:\n{np},{ng},len(patt)={len(patt)}, sum(patt)={sum(patt)}\npattern:{patt}')
        #exit(0)
        maxGapTbl=[]
        for i in range(6):
            sq=SeqGen(np,ng,patt)
            np,ng,patt = sq.getNewPattern()
            print(f'NewPattern: *\n{np},{ng},len(patt)={len(patt)}, sum(patt)={sum(patt)}\n')
            pStrArr = SeqGen.printPattern(np,ng,patt)
            for x in pStrArr:
                noprint(x)
            stats=SeqGen.gapStats(np,patt)
            stats['gapCounts'] = dict(sorted(stats['gapCounts'] .items()))
            print (f'For prime {np}: mg = {stats["mg"]}\ngapCounts:{stats["gapCounts"]}')
            maxGapTbl.append((np,stats['mg']))
        for mt in maxGapTbl: print(f'{mt[0]}: {mt[1]}')

class CandPrimes:
    def __init__(self):
        self.primes=[2] #first prime
        self.ng = 1 #the next gap
        self.patt = [2] # the pattern [self.ng,(self.pattern)*] is stored in these structures 
    
    @staticmethod
    def getRawPattern(nP:int,rg:list)->list:
        #expands the  rg np times and  add the first element to the last element
        # (Reason is that the last element is always a multiple of nP and the next is same as the first)
        # and pop out the first element as ng
        tempRg=rg*nP #expand
        ng=tempRg[0]
        tempRg[-1] += ng
        return ng,tempRg[1:]

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
        nP=self.primes[-1]+self.ng
        self.primes.append(nP) # 1
        self.ng,tempRg = CandPrimes.getRawPattern(nP,self.patt)
        noprint(f'nP={nP}, self.ng={self.ng}; tempRg = {tempRg}')
        #exit(0)
        #4. eliminate the non-primes
        cp=nP+self.ng
        npmPrimeIdx=[]
        for idx,cpg in enumerate(tempRg):
            cp +=cpg
            if cp%nP==0:
                npmPrimeIdx.append(idx)

            #print(f'cp={cp}')

                #print(f'cp={cp}, nP={nP}, idx={idx}')
        #print(f'npmPrimeIdx:len: {len(npmPrimeIdx)} for prime {nP} with primeFactorial: {self.getPrimeFactorial()}')
        noprint(f'reversed = {npmPrimeIdx}')
        #exit(0)
        for i in reversed(npmPrimeIdx): #delete in reverse direction
            try:
                tempRg[i] += tempRg[i+1]
                del tempRg[i+1]
            except IndexError: #deleting the last element is just adding the next one
                tempRg[i] += tempRg[0]
        self.patt=tempRg
        noprint(f'nextPattern = {self.patternStr()} ****')
        
        self.noOfcandPrimesEliminated= len(npmPrimeIdx)  #keep track of number of Candidate Primes eliminated in the pattern because they are divisible by the new prime.

    #experiment 7
    def getNextPatternFromPrevPattern(self):
        #ng is the first part => the gap to the next prime
        #get nP=new prime
        #From the repeating group, remove first element and add it back to the end
        #Create mod for the repeating group = mRG
        #Create the elimination list (one for each element in the list with a value between 1 and p), The value is the mod 
        #of each element in the repeating group and n*mRG = 0 
        nP=self.primes[-1]+self.ng
        self.primes.append(nP) # 1
        self.ng = self.patt[0]
        self.patt= self.patt[1:]+self.patt[:1] #new pattern to be repeated nP times
        mRG = sum(self.patt) % nP
        noprint(f'Raw patt: {self.patt}')
        elimLs = [None]*len(self.patt)
        sumSoFar =0
        for idx,e in enumerate(self.patt):
            #sumSoFar +=e
            #modE = (nNG+sumSoFar) % nP # no need to add nP as nP is divisible by nP
            #modE+N*mRG = nP => N=(nP-modE)/mRG
            N=nP+self.ng+e
            N = nP-N%nP
            elimLs[idx] = N
        noprint(f'elimLS =  {elimLs}, np = {nP}, nG = {self.ng}, mRG = {mRG}, patt = {self.patt}')
        self.printPattFromElimLs(nP,self.ng,self.patt,elimLs)
        return elimLs

    def printPattFromElimLs(self,p:int,nG:int,patt:list[int],elimLs: list[int]):
        elemFl =[len(patt)*(e)+i for i,e in enumerate(patt)]
        elemFl.sort()
        print(f'elemFl = {elemFl}')
        #print pattern
        elemFlIdx=0
        pIdx=0
        collapsed=False
        for i in range(p*len(patt)):
            try:
                if i == elemFl[elemFlIdx]:
                    elemFlIdx +=1
                    try:
                        patVal = patt[pIdx]+patt[pIdx+1]
                        print(f'{patVal},',end='')
                    except IndexError:
                        patVal = patt[pIdx]+patt[0]
                        print(f'{patVal},',end='')
                    #self.pattern.append(patVal)
                    collapsed=True
                else:
                    if collapsed: collapsed=False
                    else:
                        patVal = patt[pIdx]
                        print(f'{patVal},', end='')
                        #self.pattern.append(patVal)

                pIdx+=1
                if pIdx==len(patt):pIdx=0
            except IndexError:
                break
        print()
        #4,2,4,2,4,x2,4,2,x4,2 => 4,2,4,2,4,6,2,6

    def getPrimeFactorial(self):
        #returns product of all primes (in self.primes)
        pf=1
        for p in self.primes: pf *=p
        return pf
    
    def patternStr(self,verbose=False):
        #get a printable representation of the patterncprimes
        pat=self.patt
        p=self.primes[-1]
        if len(pat)<2: msg= f'Prime: {p} has Invalid Pattern: {pat}'
        sum=0
        for cp in self.patt:
            sum +=cp
        if verbose:
            msg = f'Pattern ({self.ng},({self.patt})*) for Prime: {p} has Length = {len(self.patt)} that repeats every {sum}\n '
        else:
            msg = f'for Prime: {p} pattern has Length = {len(self.patt)} that repeats every {sum}\n '
        return msg
    #experiments:
    #Experiment #1:

    def getPrimesUptoN(self,N):
        #gets all prime number upto N
        maxP = int(math.sqrt(N))
        while self.primes[-1] < maxP:
            self.getNextPattern()
        sCP=self.primes[-1]
        primeArr = self.primes[:]
        for cpg in self.pattern:
            sCP +=cpg
            if sCP > N: break
            primeArr.append(sCP)
        return primeArr



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
            self.ng,tempRg = self.getRawPattern(nP,rg)
            twinPrimesInRawPattern = countTps(tempRg)
            self.getNextPattern()
            twinPrimesAfterElimination = countTps(self.pattern)
            pctEliminated = (twinPrimesInRawPattern-twinPrimesAfterElimination)*100/twinPrimesInRawPattern
            pctExpected = 2*100/nP
            print(f'For prime {nP} twinPrimesBeforeElimination = {twinPrimesInRawPattern}, after = {twinPrimesAfterElimination}'
                  f' %Eliminated = {pctEliminated}, expected = {pctExpected}')

    #Experiment #5:
    def maxGapVsPrimeSquare(self):
        #Theory=> with each prime the max GapSize at most double. However the next prime square goes up by 4X+4 (i.e. (x+2)^2 - x^2). So there must
        # be 1 or more primes before the prime^2
        #Here we show the max gap and primeSquare value for primes upto 100
        for i in range (1,10):
            maxGap= max(self.pattern)
            prime = self.primes[i-1]
            self.getNextPattern()
            print (f'seq: {i}, prime = {prime}, maxGap = {maxGap}, primeSqr = {prime*prime}, 2^seq = {2**i}, '
                   f'maxGap/prime = {maxGap/prime}')

    #Experiment #6:
    def patternLength(self,N):
        #Here we calculate the length of the repeating pattern of candidate primes for each prime <=N
        primeArr = self.getPrimesUptoN(N)
        pfac =1
        for pidx,p in enumerate(primeArr):
            pfac = p*pfac
            noEliminated = 0
            noLeft = pfac
            for ppidx in primeArr[:pidx+1]: 
                curEliminated = noLeft/ppidx
                noLeft -= curEliminated
                noEliminated += curEliminated
                
            noLeft = pfac - noEliminated
            print(f'Prime = {p}, GapLen = {noLeft}, pfac = {pfac}, lastEliminated: {curEliminated}') 

    @staticmethod
    def test(args):
        experiments = Enum('exp', ['calcNumberOfTwinPrimes', 'getFraction', 'getPrimesUpto100','getPrimesUpto1000','getNextPattern'
            ,'maxGapVsPrimeSquare','patternLength','getNextPatternFromPrevPattern'
        ])
        expToDo=experiments.getNextPatternFromPrevPattern
        CP=CandPrimes()
        match expToDo:
            case experiments.calcNumberOfTwinPrimes:
                CP.calcNumberOfTwinPrimes(7)
            case experiments.getFraction:
                CP.getFraction(7)
            case experiments.getPrimesUpto100:
                primeArr = CP.getPrimesUptoN(100)
                print(f'NoOfPrimes = {len(primeArr)} \n primes: {",".join(map(str,primeArr))}')
            case experiments.getPrimesUpto1000:
                CP.getPrimesUptoN(1000)
            case experiments.getNextPattern:
                print(CP.patternStr(True))
                for i in range(10):
                    CP.getNextPattern()
                    print(CP.patternStr(True))
            case experiments.maxGapVsPrimeSquare:
                CP.maxGapVsPrimeSquare()
            case experiments.patternLength:
                CP.patternLength(100)
            case experiments.getNextPatternFromPrevPattern:
                for i in range(4):
                    #CP.getNextPattern()
                    #print(f'***Old:\n{CP.patternStr(True)}\n***')
                    #CP.getNextPatternFromPrevPattern(5,2,[4, 2, 4, 2, 4, 6, 2, 6])
                    np=CP.primes[-1]+CP.patt[0]
                    print(f'inputs: p: {np}, ng: {CP.ng}, patt: {CP.patt}')
                    CP.getNextPatternFromPrevPattern()
                    print(f'============Primes = {CP.primes} for above results')
            case _:
                print(f'**Error: Experiment {expToDo} not implemented')
        print(f'Experiment {expToDo} completed..')


def maxGapCalulator(ps:list[int]):
    #Takes a list of primes starting with 3 and calculates the max gap. The theory is:
    #These primes can divide a sequence of numbers. So the min mg is np*2+2
    #The algorithm starts with the first prime and initial wmg=1 (working max gap).
    #Then it checks if the previous primes can increase this wmg (if wmp+1 mod p ==0). It continues on until the 
    #last prime is processed
    wmg=0
    lp,fp = ps[-1],ps[0] #largest prime in set and lowest prime in set
    weps:int =int((lp-fp)/2+1) #working gap size (in 2's)
    #look on the right side
    ncp = lp+2
    while True:
        added=False
        for idx,p in enumerate(ps):
            if ncp %p ==0 :
                #add to gap
                added = True
                weps +=1
                ncp +=2
                continue
        if not added : break
    return (weps*2+2)
    #now look on left side
    le = 1
    for idx,p in enumerate(ps):
        if int((p-ps[0])+(le*2)+1) %p ==0 :
            #add to gap
            le +=1
            continue
    print(f'ps:{ps}, weps={weps},le={le}')
    return (weps+le-1)*2+2



    def wmgIncrease(idx:int)->bool:
        nonlocal wmg
        for p in ps[:idx]: #prev primes
            if (wmg) % p ==0:
                return True
        return False
    for idx,p in enumerate(ps):
        wmg +=1
        if wmgIncrease(idx): wmg+=1
    #Now continue beyond ps until wmg is not increased
    ag=wmg+1
    while True:
        inc=False
        for idx,p in enumerate(ps):
            if ag % p ==0:
                inc=True
                ag +=1
                break
        if not inc: break
        #if len(ps)>4: print(f'{p} => wmg = {wmg}')
    print(f'wmg={wmg}, ag={ag}')
    ag -=2
    mg = ag*2+2
    return mg
if __name__=='__main__':
    import sys
    args = sys.argv
    #CandPrimes.test(args)
    SeqGen.test()
    exit(0)
    #primes upto 100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]
    pss=[ 3,5, 7, 11, 13] #, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]
    print(f'Expected gaps:\n 7: 10\n11: 14\n13: 22\n17: 26\n19: 34\n23: 40')
    for idx,ps in enumerate(pss):
        ps=pss[0:idx+1]
        print(f'Maxgap for {ps} is {maxGapCalulator(ps)}')
