# DIY overnight spO2 monitoring
spO2 which indicates how well oxygen is available in your blood for use by all bodily organs, including the brain. The normal range is 100 to 95. Below 92 is concerning and below 88 is dangerous.
Here is a device that records spo2 every 2 seconds and can be used for over 10 hrs:  
APLPV3052R

<img src="img/spO2CheckmeO2Max.png"> 

You can use the viHealth app on your phone to view the results. For better viewing and analysis, you can download the data from the device to a desktop process it on a desktop.

All who have been diagnosed/concerned with sleep apnea, should get this device (100-200$)  

## Analysis
Appears that a cool clean body can give you a better sleep.

### Day 1 Score: 8.8, %good 99.37, %warn 0.63, %emer 0.00

A recording of about 9 hrs was taken, resulting in some 15K samples. The viHealth app on the phone was used to export this data to the desktop.  Using the AI kit Claude, this data was analyzed through a python program and the following shows the chart produced.  
Feeling: Had a good sleep.  
<img src="img/spO2/day1/all.png"> 
---

### Day 2 Score: 7.6, %good 97.86, %warn 2.14, %emer 0.11
Feeling: Had a bad sleep. Waking up 3-4 times. Bed/pillow felt hot. Should have taken a cool shower or rubdown before sleep.
<img src="img/spO2/day2/all.png">  
---

### Day 3 Score: 3.6, %good 84.39, %warn 15.61.14, %emer 3.06
Feeling: Had a bad sleep. Waking up 3-4 times. Bed/pillow felt hot. Tension (thoughts going thru the mind). Should meditate?  
<img src="img/spO2/day3/all.png">  
---

### Day 4: Score: 9.9, %good 99.92, %warn 0.00, %emer 0.00 : Different Person with No Sleep Apnea
Feeling: Did not sleep well  
<img src="img/spO2/day4/all.png">  
---

### Day 5: Score: 7.9, %good 97.70, %warn 2.30, %emer 0.05 :  On Bamboo topper bed
Mattress topper is cooling and comfortable
Feeling: slept well  
<img src="img/spO2/day5/all.png">  
---

## Summary  

| Night | Above warn | Below warn (92) | Below emergency (88) |
| --- | :---: | --- | --- |
| 0708 | 99.37 | 0.63 | 0 |
| 0709  | 97.86     | 2.14             | 0.11                   |
| 0710  | 84.39     | 15.61            | 3.06                  |
| 0711  | 99.92     | 0.00             | 0.00                    |
| 0712  | 97.70     | 2.30               | 0.05                    |
  