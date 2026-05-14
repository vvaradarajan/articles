#target: continuously reduce pattern and print at end
def print1(*args):
    pass #don't print print1

import math
def nFraction(nEnd:int,p:int,nSt:int=0):
    #successively remove the eliminated fraction of N:  (nEnd-nSt) -  2*(nEnd-nSt)/p and returns the number left (rounded up)
    netN = nEnd-nSt
    return math.ceil(netN * (1-2/p))

def findGaps(pa:list[tuple[int,int]],np:int,lo:list[int])->tuple[list[tuple[int,int]],set[int],float,list[int]]:
    #returms new pattern array,set of gaps, ratio, leftOver
    gl:set[int]=set() #list of gaps
    lidx=0 #last index of gap
    npa:list[tuple[int,int]]=[]
    lo=[i for i in lo if i%np !=0 and i>np] #eliminate multiples
    lo.append(np)
    elim = 0
    for idx,t in enumerate(pa):
        alo:list[int]=[] #new lo elements
        print1(f'lo={lo}')
        eliminated=False
        for i in lo:
            if t[0]%i == 0 or t[1]%i == 0:
                g = idx-lidx
                gl.add(g)
                lidx=idx
                elim+=1
                alo.append(t[0] if t[1]%np==0 else t[1])
                eliminated=True
                break
        if not eliminated: npa.append(t)
    try:
        ratio = (elim)/len(pa)
    except ZeroDivisionError: ratio =1
    lo.extend(alo)
    return npa,gl,ratio,lo

def findGapsUsingNpOnly(pa:list[tuple[int,int]],np:int)->tuple[list[tuple[int,int]],set[int],float]:
    #returms new pattern array,set of gaps, ratio.
    #assumes that all primes < np have already pruned the pattern
    gl:set[int]=set() #list of gaps
    lidx=0 #last index of gap
    npa:list[tuple[int,int]]=[] #pruned pattern list
    elim = 0
    for idx,t in enumerate(pa):
        eliminated=False
        if t[0]%np == 0 or t[1]%np == 0:
            g = idx-lidx
            gl.add(g)
            lidx=idx
            elim+=1
            eliminated=True
            break
        if not eliminated: npa.append(t)
    try:
        ratio = (elim)/len(pa)
    except ZeroDivisionError: ratio =1
    return npa,gl,ratio


def createCTplist(maxlength)->list[tuple[int,int]]:
    #create all candidate twin primes from 3 onwards
    cTpArr:list[tuple[int,int]]=[]
    fn=3
    while fn+2 < maxlength:
        cTpArr.append((fn,fn+2))
        fn +=2
    return cTpArr

def findCTwins(np:int,nnp:int,cTpArr: list[tuple[int,int]],tpArr:list[tuple[int,int]]) -> tuple[list[tuple[int,int]],int,int,int]:
    #np=new prime, nnp=next prime,cTpArr=list of candidate twin primes, tpArr: lost of twin primes
    #returns the new CtpArr,ratio and the tpArr after elimination 
    cNTpArr:list[tuple[int,int]]=[]
    #process the head
    if nnp-np==2: #take care of case like [3,5]
        tpArr.append((np,nnp)) 
    idx=0
    #if cTpArr[0][0]==nnp: idx+=1
    #process the rest
    for t in cTpArr[idx:]:
        if t[0]%np == 0 or t[1]%np == 0: continue
        if t[1]<nnp: tpArr.append((t))
        else: cNTpArr.append(t)
    noOfTps = len(tpArr)
    return cNTpArr,len(cTpArr),len(cNTpArr),noOfTps


plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def verifyCTpArr(cTpArr:list[tuple[int,int]],pl:list[int]) -> tuple[bool,str]:
    #verifies that candidate prime array is not divisible by any in pl
    for p in pl:
        for t in cTpArr:
            if t[0] % p == 0 or t[1] %p == 0: return False,f' cTp: {t} is divisible by {p}'
    return True,f'cTpArr is good upto prime {pl[-1]}'
np,nnp = 2,3 #candidate twin primes start here (i.e. (3,5), (5,7)..)
s=1 #equals (np-1)! i.e. for 5 it is 3*2=6, 7=>3*2*5=30
for i in plist:
    s *=i
    if i == np:break
fn=nnp
maxN=100 #np+s
#create pattern starting with 3,5
cTpArr = createCTplist(maxN)
print(f'Pattern = {len(cTpArr)}: {cTpArr}')
tpArr:list[tuple[int,int]]=[]
nPtoConsider = 11
cTpArrVsUptoP: list[tuple[int,int]] =[] #no of cTp's upto prime P
printArr : list[str] = []
for idx,np in enumerate(plist[1:nPtoConsider]):
    cTpArr,inCTplen,outCTplen,noOfTps = findCTwins(np,plist[idx+2],cTpArr,tpArr)
    # print(f'Twin Primes = {tpArr}\ncTpArr={cTpArr}')
    # print(f'maxN: {maxN}, cTpArrLen={len(cTpArr)}')
    # print(f'np={np},nnp={plist[idx+2]},ratio={ratio},noOfTps={noOfTps}')
    cTpArrVsUptoP.append((len(cTpArr),np))
    t=cTpArrVsUptoP[-1]
    nTps = len(tpArr)
    try:
        ratioAfter = 1.0 - (outCTplen-nTps)/(inCTplen-nTps) if outCTplen != inCTplen else 1.0
    except Exception as E:
        print (f'cTpArr: {cTpArr}')
        print(f'ratioAfter error: outCTplen: {outCTplen}, nTps:{nTps}, inCTplen: {inCTplen}, np:{np}')
        exit (1)
    predictedNoOfcTp = (inCTplen-nTps)*(1-2/np)+nTps
    printArr.append(f'{t[0]} upto {t[1]}: {t[1]**2}, {maxN} {nTps} {ratioAfter:.4f} {predictedNoOfcTp:.0f} - {tpArr}')

print(f'{verifyCTpArr(cTpArr,plist[1:nPtoConsider])[1]}')
print(f'maxN={maxN}\nNoOfcTp,upToP:upToP**2, nTps, ratio, predictedNoOfcTp maxN - [tpArr]')
for l in printArr: print(l)
for t in cTpArrVsUptoP:
    pass
    #print(f'{t[0]} upto {t[1]}: {t[1]**2}, {maxN}  - {tpArr}')

exit(0)

lo:list[int]=[]
# for np in [5,7,11,13,17,19,23,29,31,37,223]:
#     #print(f'pattern(np={np})={pattern}\n')
#     pattern,tpGaps,ratio,lo = findGaps(pattern,np,lo)
#     #print(f'tpGaps = {tpGaps}\nnewPattern={pattern}\nratio={ratio}')
#     print(f'np={np}, ratio ={ratio:.2f}, expect={2/np:.2f},lo={lo}')
# print1(f'Twin Primes: {pattern}')
#Twin primes left
pArr = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]
nEnd=len(pattern)
pMax = pattern[-1][1]
fl = 1 #fraction left
for np in pArr:
    nEnd=nFraction(nEnd,np)
    fl *=1-2/np
    print(f'twin primes left after {np} = {nEnd}, fraction = {fl}')
    if np > pMax: break
exit(0)
#[(3, 5), (5, 7), (11, 13), (13, 15), (17, 19),  (23, 25), (29, 31)]
#Proof: n*[fraction] increases a n increases: i.e. n*(n(1-2/np) for np) increases
#(or atleast there exists n > N where n*(n(1-2/np) > N*(N(1-2/np) for any N )

''' Logical proof:
    1. Each candidate twin prime tuple is of the form p,p+2, where both p and p+2 are candidate primes. p+2 is also not divisible by p, since p > 2.
    2. The number candidate twin primes upto N is N*(1-2/p)*(1-2/p1)*(1-2/p2).. Ex: The number of twin primes for N=30 is:

'''


exit(0)


result = pattern * 7

running_sum = 0
for i, num in enumerate(result):
    running_sum += num
    total = running_sum + 7
    if total % 7 == 0:
        print(f"Index {i}: value={num}, sum_of_prior + 7 = {total} (divisible by 7)")


print()
for i in range(0, len(result), 8):
    print(result[i:i+8])
#Lathar562@

03/19 03/19 APPLE.COM/BILL 866-712-7753 CA 4901 4128 37.95
04/05 04/06 APPLE.COM/BILL 866-712-7753 CA 7103 4128 119.99
04/06 04/06 APPLE.COM/BILL 866-712-7753 CA 5787 4128 124.99
04/16 04/16 APPLE.COM/BILL 866-712-7753 CA 1189 4128 34.99