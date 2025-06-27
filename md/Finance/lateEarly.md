# Late vs Early Withdrawal from Tax perspective

## Overview
What is the Question? : 
Withdrawals from IRA are treated as ordinary income, and ordinary income tax rates are higher at the higher slab rates (some 37%). The capital gains tax rate is less (at most 20%). Therefore if we withdraw, the income earned after withdrawal is taxed at the capital gain tax rate.  
The question is: Is withdrawing early is good?

## Problem Discussion
In Early withdrawal, the tax has to be paid right away. After that any income earned (i.e. the withdrawal amount is invested in stocks earning capital gains income) 
In Late withdrawal, the ordinary income tax has to be paid at the withdrawal time.  
The after tax income of these two should be compared for some period of time (10 years or so) to answer to the question. 

## One simulation
The simulation below shows that Comparison:  
<img src="img/retirement/lateEarly/xl.png">

## Detailed Explanation  
<img src="img/retirement/lateEarly/eqn.png"> 

## Result Discussion

Intuitively the results are dependent on otr and ctr. The higher the otr, the more the tax paid early, leaving less for investment. This favors late withdrawal. From a different perspective, a lower ctr favors early withdrawal.  
Notice that the tax rate (ordinary) can be between early and late withdrawal depending on the difference in the tax rate slab at beginning and at end. Therefore the timing of the early withdrawal and timing of the final cashout will have significant impact.

### Roth IRA conversion: 
This comparison is made on the basis that the early withdrawals are invested. However in this case conversion to Roth IRA has a big advantage as the Capital gains will not be taxed. You can simulate this situation by setting the capital gains tax to zero. 

# When to take Social Security: 62, 65 or 70

## The simulation is on the tab 'SS_when' in the XL sheet
## Discussion of Result
Inflation plays an important role in the decision. High inflation favors getting the SS sooner, because payments received later are worth less due to inflation. The comparison between the ages to retire is made by calculating the Present Value of all SS payments at the age of 62. Ex: If SS is taken at 65, that PV is adjusted for 3 yrs (65-63) years of inflation. SS payments themselves can change due to inflation so basing the monthly payments on today's values (provided by the esteemed member) throws a wrench into these complex calculations. Simulating with 'reasonable' values for inflation, it appears to favor taking the SS at 65. However the difference is not very significant as to take it at 62.

## Other discussions:
How to type equations? LaTex, the academic standard is not easy. An easier one is LyX which has a workable visual interface, and if needed you can copy the equation as a pdf/image (which is used here) or as LaTex. So since math is getting prominence in retirement ("In this world nothing can be said to be certain, except math and taxes!") it will be a good idea to discuss LyX

<down-load fileNm="retirement/lateEarly/lateEarlySample.xlsx" label="lateEarlySample.xlsx"></down-load>