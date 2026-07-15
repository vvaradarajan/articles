# DIY overnight spO2 monitoring
spO2 which indicates how well oxygen is available in your blood for use by all bodily organs, including the brain. The normal range is 100 to 95. Below 92 is concerning and below 88 is dangerous.
Here is a device that records spo2 every 2 seconds and can be used for over 10 hrs:  
APLPV3052R

<img src="img/spO2CheckmeO2Max.png"> 

You can use the viHealth app on your phone to view the results. For better viewing and analysis, you can download the data from the device to a desktop process it on a desktop.

All who have been diagnosed/concerned with sleep apnea, should get this device (100-200$)  

## Analysis
Appears that a cool clean body can give you a better sleep.

### Dt: 0708 Score: 8.8, %good 99.37, %warn 0.63, %emer 0.00

A recording of about 9 hrs was taken, resulting in some 15K samples. The viHealth app on the phone was used to export this data to the desktop.  Using the AI kit Claude, this data was analyzed through a python program and the following shows the chart produced.  
Feeling: Had a good sleep.  
<img src="img/spO2/0708/all.png"> 
---

### Dt: 0709 Score: 7.6, %good 97.86, %warn 2.14, %emer 0.11
Feeling: Had a bad sleep. Waking up 3-4 times. Bed/pillow felt hot. Should have taken a cool shower or rubdown before sleep.
<img src="img/spO2/0709/all.png">  
---

### Dt: 0710 Score: 3.6, %good 84.39, %warn 15.61.14, %emer 3.06
Feeling: Had a bad sleep. Waking up 3-4 times. Bed/pillow felt hot. Tension (thoughts going thru the mind). Should meditate?  
<img src="img/spO2/0710/all.png">  
---

### Dt: 0711 Score: 9.9, %good 99.92, %warn 0.00, %emer 0.00 : Different Person with No Sleep Apnea
Feeling: Did not sleep well  
<img src="img/spO2/0711/all.png">  
---

### Dt: 0712 Score: 7.9, %good 97.70, %warn 2.30, %emer 0.05 :  On Bamboo topper bed
Mattress topper is cooling and comfortable
Feeling: slept well  
<img src="img/spO2/0712/all.png">  
---

### Dt: 0713: Score: 7.5, %good 95.14, %warn 4.86, %emer 0.07 :  On Bamboo topper bed
Mattress topper is cooling and comfortable
Feeling: slept well, but got up once and didn't go back to sleep for 30 mins with all thoughts
<img src="img/spO2/0713/all.png">  
---
### Dt: 0714: Score: ????, %good 100.00, %warn 0.00, %emer 0.00: AR
Feeling: Too short a recording. Must keep the probe throughout sleep.
Note the heart rate -- this is too high! 
<img src="img/spO2/0714/all.png">  

## Summary  

| Night | Above warn | Below warn (92) | Below emergency (88) |
| --- | :---: | --- | --- |
| 0708 | 99.37 | 0.63 | 0 |
| 0709  | 97.86     | 2.14             | 0.11                   |
| 0710  | 84.39     | 15.61            | 3.06                  |
| 0711  | 99.92     | 0.00             | 0.00                    |
| 0712  | 97.70     | 2.30               | 0.05                    |
| 0713  | 95.14     | 4.86               | 0.07                    |
| 0714  | 100.00     | 0.00               | 0.00                    |
  