# Projects
### Three Bucket vs One Bucket approach to Money Management
### Programmable Induction Cook top.
### AI for day to day use with family information

<img src="img/projects.png">

### Three Bucket vs One Bucket approach to Money Management
#### Overview

Money management gets more and more important now, as money itself can generate a substantial income as you advance through the years. When in retirement money management is often the only income.  
The three bucket approach is to ensure a sense of stability considering stress and inclding the primary purpose - to have a good life. 
The one bucket approach is to invest in the highest return in the stock market, and claims that this will ensure better income both immediately and over time. The simulations will show that this aligns with the primary purpose - to have a good life and stress is not necessary.

#### Project:  
Show the performance over 10 years of a three bucket approach vs the one bucket approach.

#### Three bucket approach:
*
Bucket 1: Six months’ to two years’ worth of living expenses—not covered by Social Security—are housed in cash instruments.  
•
Bucket 2: Another 8-10 years’ worth of living expenses are housed in bonds.  
•
Bucket 3: The remainder of the portfolio is invested in stocks and a high-risk bond fund.  
Income and rebalancing proceeds from Buckets 2 and 3 are used to replenish Bucket 1 as it becomes depleted.
These investment portfolio examples include aggressive, moderate, and conservative portfolio options to align with a retiree’s level of risk tolerance. The portfolios are designed to be held in either tax-sheltered or taxable accounts. A retiree can build the right portfolio for their needs by customizing their allocations based on their own expected portfolio withdrawals.  

#### One bucket approach:

Put everything in stocks and a high-risk bond fund. This approach assumes that there are atleast 8-10 years worth of living expenses to start with.

#### category: software
#### Work

Develop and implement a web based/app based application that Simulates both approaches with reasonable assumptions based on currently available data on the internet. For Example:
1. Average stock market return: 10% varies(The year/year performance can be from the internet)
2. Average return on bonds: 4.5%
3. Average return on Savings Acct: 0.4 to 4
Tools available: Existing webApp code,  boldin.com has tools..

### Programmable Induction Cook top.
#### Overview

Induction currently have two very configurable parameters, the power transmitted via induction to the vessel, and time duration before turning off. This is very convenient for calculation of power consumed and allows precise timings for simple cooking operations such as boiling water.  

These two features alone make the induction stove a very convenient, safe, power efficient and most of all minimising the amount of attention required of the cook. The 'cook' can move on to other roles (writing, programming, watching TV..) knowing that the induction stove will complete and turn off after the food is cooked and just sitting there waiting to be consumed!  
The opportunity is to augment these features for more complex cooking scenarios. An example would making soup, with a recipe of heat to boil in 5 mins, and let it simmer or 10 mins.  To implement this we need a 'programmable sequence'. This sequence will allow following a series of power and duration pairs. In the soup scenario the sequence would be [(p,5),(p1,10)]. Here the first term (p,5) will bring the soup to a boil, and the second (p1,10) will keep it simmering. The powers p and p1 depend on the amount of soup. These have to be 'guesstimated' by the cook, or by some formula based on the vessel and the quantity of soup, which could hueristically calculated by the weight.  Since the feature of 'weighing' is not available on current cookware, this project will focus only on phase 1.  

#### Hardware
Using a Raspberry pie or similar computer, we need an interface API to manipulate the touch controls on an induction cooktop. The current thought is to open the induction cooktop panel, determine the mechanism of the touch switches. Following this the point of connection between the Raspberry pie and the induction cooktop is selected. The computer than should be able to manipulate the switches and control the cooktop.

#### Software
Programming the sequence of manipulating the switches. This is the first part. The further parts that would be included in this project are:  
1. Safety turn off when conditions are not met.  
2. Determine sequences for three common cooking tasks: boiling water, cooking soup, cooking  Rajma curry.