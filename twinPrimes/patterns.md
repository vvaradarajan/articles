# Patterns

2: 2,1,[2]*
3: 3,2,[2,4]*
5: 5,2,[4, 2, 4, 2, 4, 6, 2, 6]*

5,3
4,2,4,2,4,(2,4),2,(4,2) [2,4]
4.2.4.2.4,6,2,6

newPatt:deque([2, 4, 2, 4, 6, 2, 6, 4]), elements_to_remove: [10, 6, 3, 6, 3, 6, 11, 2]
NewPatt: 7,4,[2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 4, 2, 4, 6, 2, 10, 2, 10, 4, 6, 2, 10, 8, 2, 10, 6, 4, 2, 4, 2, 10, 6, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 4, 6, 2, 6]

[2, 4, 2, 4, 6, 2, 6, 4,2, 4, -2, 4, 6, 2, 6, 4]
2, 4, 2, 4, 6, 2, 6, 4 (0-7): 41
2, 4, 6: 53

101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199

# Elimination in pattern:
Hypothesis: Each new prime creates a new pattern with each gap in the previous pattern being eliminated once and only once.
Ex: pattern for 2 = 1,[2]*. The next prime is 3 and the pattern is [2,2,2]* => one of the twos is eliminated (in this case the last one giving 2,[2,4]*).
The next is 5 and the pattern is [2,4,2,4,2,4,2,4,2,4]

Final proof:
We have shown that number of candidatec primes follow have the formula 1-series sum(2/p*N). We also know the candidate primes become real twin primes as we proceed to p**2 > N. For the formula to be valid for N1 > N, we know that the nT (no of twin primes) cannot decrease, and cnT > nT. Now we can derive the number nT for the new N1 using the forumula (which will be original formula, with some more subtractions). These formulas can never be equal, and hence nT must increase. QED!

Numerical method of proof:
For N = 100, calculate ncT for each p: output => ncT, ration, ratio with ncT > p (i.e. the first member of the tuple > p)

