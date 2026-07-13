# DIY overnight spO2 monitoring
spO2 which indicates how well oxygen is available in your blood for use by all bodily organs, including the brain. The normal range is 100 to 95. Below 92 is concerning and below 88 is dangerous.
Here is a device that records spo2 every 2 seconds and can be used for over 10 hrs:  
APLPV3052R

<img src="img/spO2CheckmeO2Max.png"> 

You can use the viHealth app on your phone to view the results. For better viewing and analysis, you can download the data from the device to a desktop process it on a desktop.

All who have been diagnosed/concerned with sleep apnea, should get this device (100-200$)  

## Analysis
Appears that a cool clean body can give you a better sleep.

### Day 1 Score: 8.8

A recording of about 9 hrs was taken, resulting in some 15K samples. The viHealth app on the phone was used to export this data to the desktop.  Using the AI kit Claude, this data was analyzed through a python program and the following shows the chart produced:  
<img src="img/spO2/day1/all.png"> 

Feeling: Had a good sleep.

### Day 2 Score: 7.6
<img src="img/spO2/day2/all.png">  
Feeling: Had a bad sleep. Waking up 3-4 times. Bed/pillow felt hot. Should have taken a cool shower or rubdown before sleep.

### Day 3 Score: 3.6
<img src="img/spO2/day3/all.png">  
Feeling: Had a bad sleep. Waking up 3-4 times. Bed/pillow felt hot. Tension (thoughts going thru the mind). Should meditate?

### Day 4: Score: 9.9, Different Person with No Sleep Apnea
<img src="img/spO2/day4/all.png">  
Different Person with No Sleep Apnea
Feeling: Did not sleep well

## Summary  

| Night | Avg SpO2 | Below warn (92) | Below emergency (88) |
| --- | :---: | --- | --- |
| 0708 | 96.8 | 101 | 0 |
| 0709  | 96.1     | 251             | 13                   |
| 0710  | 94.6     | 1846            | 362                  |
| 0711  | 96.1     | 9               | 0                    |
  