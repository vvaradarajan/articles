Proof of the Twin prime conjecture:
The twin prime conjecture is there are infinitely many prime numbers seperated by 2. Think of 3,5 or 5,7 or 11,13 or 17,19 ...
This twin prime is a natural guess that follows from 'there are infinitely many prime numbers', but unfortunately the proof has not been found so far and now we claim to have found the proof!
<Think, ruminate, do not eat or drink and try to prove the conjecture>

Basic concepts behind this proof:
Candidate primes of prime p: These are numbers that are greater than p, but cannot be divided by any number <=p. ex: 
candidate primes of 2 are 3,5,7,.. i.e. all odd numbers > 2.
candidate primes of 3 are 5,7,11,13,17,19,23.. i.e. all numbers with the gaps following a pattern 5+(2,4)*

Gap Pattern:
Candidate primes of p, follow a Gap pattern. ex: for 2, the pattern is 3+(2)*. For 3 the pattern is 5+(2,4)*
The form of the pattern is the np+(x1,x2..)* where (x1,x2,..) repeat and np is the next prime.  The sum of the repeating part is a multiplication of all primes p and below. We call this the prime factorial. ex: For 2 the pf(2) =2 and the pattern is (2)*
Theorem: There is a prime number between any number and its multiple.
Proof:
1. The number considered here is a prime = p
2. Find the pattern of candidate primes = cp(p)
3. find the next prime np
4. Notice that the pattern can only change at np^2 (i.e. np 'knocks' out np^2 from list of candidate primes)
5. Determine how the max gap increases when the next prime comes in = mg(p) + mg(p-1) = mp(np)
6. Show that mp(p)+mp(p-1) < 2*np
Example: p=3, cp(p) = [2,4]*, mg(p)=4, mg(p-1)=2, mp(np)=6, np=5, np^2=25, mp^2 > mg(np) or 25 > 6. Therefore there is a prime within 6 of 5 which is definitely within 5*2 = 10.
Now the proof is straightforward, once we recognize that the max gap doubles (until prime 3) less than doubles (prime > 3) with each new prime. Starting with 1 as a prime, the gaps for 1 is (1)*, np=2;  for 2 it is (2)*,np=3; for 3 it is (2,4)*, np=5; for 5 it is (4, 2, 4, 2, 4, 6, 2, 6)*,np=7
So we lay down the following rules:
1. The max gap doubles or less that doubles with each new prime np.
2. After prime 11 the max gap is less that 2*11 and the max gap is continuously < 2 *np
Therefore there is prime between np and 2*np!
**all wrong***

Computing max-gap. 2^n < nth prime:
ex: For 3: 2^2 = 4 < 2*3> = 6

The max gap theorem: The max gap occurs when a sequence of candidate primes are divisible by the primes before it. The algorithm to determine this is:
Steps:
1. The max gap is then the number of primes before *2.
2. Try to extend the gap as follows:
a. For each prime number (starting with 3):
a1. If np (no of primes) > p increase max gap by 2

write out the sequence of primes: [2,3]
count number of primes in group = cp =2 above. Also make pcp = cp
 Start with 3. Then number of primes after 3 = naa(3). If naa(p)+1 mod p =0, then pcp++ => Loop until mod !=0 for all p
 The max gap is 2*pcp. The next prime is lp + (pcp-cp+1)*2

 Ex: [3], cp=1, pcp=1, naa(3)=0 naa(3)+1 = 1 => np=3+(1-1+1)*2 = 5, pcp-cp = 0
 [3,5], cp=2, pcp=2,naa(3)=1 naa(3)+1=2 => np=5+(2-2+1)*2 = 7, mg = 2*2 = 4,  pcp-cp = 0
 [3,5,7], cp=3, pcp=3, naa(3)=2 naa(3)+1 = 3 pcp++=4 => np= 7+(4-3+1)*2 = 11, mg = 2*4 = 8,  pcp-cp = 1
 [3,5,7,11], cp=4, pcp=4, naa(3)=3, .. np=11+(4-4+1)*2 = 13, if pcp==cp then mg = prev max gap +2 = 10


3 => nop = 2, g = nop=2, nop mod 2 = 0 so g++ = 3 gap is g+1=4
3,5 => g=(nop+1)*2 = 6
3,5,7 => g = (nop+2)*2 = 10
3,5,7,11 => g = (nop+1)

The max group theorem redefined:
1. Get a set of primes [3] cp=1, pcp=1, naa(3)=0 naa(3)+1 = 1 => np=lp+(pcp-cp+1)*2 = 3+(1-1+1)*2 = 5, pcp-cp = 0
2. Now plg=4 (previous max gap)
3. [3,5] cp=2 pcp =2 For 3: naa(3)=1, naa(3)+1 mod 3 <>0, pcp-cp = 0 
                        5: <same>
                        nlg = plg+2*1 = 6
4.  [3,5,7]

Initial conditions
ps=[3] - prime set
cpc=1 - count of primes in prime set
naa(3)=0 - primes after 3 is
plg=2 - previous largest gap
clg=4 - current largest gap
pcp(3)=0 - primes after 3
nnp = 5 - next new prime

Iteration:
ps=[3,5] - append the nnp
cp=2
plg2=3 - previous largest gap/2 + 1
eE = 0 - extra elimination - happens if mod naa(p)+1 mod p ==0. The loop should continue with plg2++ 
naa(3)=1, eE=0
naa(5)=0, eE=0
lg=plg2*2 = 6

ps=[3,5,7]
plg2=4 - previous largest gap/2 + 1
eE = 0 - extra elimination - happens if mod plg2 mod p ==0. The loop should continue with plg2++ 
naa(3)=2, eE=1 : plg2++, addTonaa is 1 loop breaks here 
naa(5)+addTonaa=2, eE=0
naa(5)+addTonaa=0+1=1, eE=0
Since addToNaa > 0, repeat with new addToNaa for those that created the addTonaa (3) (or repeat with addTonaa until eE is zero for all primes)
lg=plg2*2 = 10

p=[3,5,7,11]
pp = plg2/2 -1 = 4 (4 successive numbers is a gap of 10: 2 to the first and two after the last)
addToNaa=1 (pp-(cp-1))
naa(3) = 3+1 = 4 (3+addToNaa)/), eE=0
naa(5) = 3, eE=0
naa(7) = 2 
naa(11) = 0 -> addToNaa applies to everything except the last one
lg = (np+addToNaa)*2+2 = 12

p=[]



