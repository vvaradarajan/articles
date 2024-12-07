from pyexcel_ods import get_data
import json
from dataclasses import dataclass
from matplotlib import pyplot as plt
from datetime import datetime
@dataclass
class spo2Rec:
    dt: str
    ti: str
    spo2: int
    hr: int

def getDatafromOds(fileNm ="SpO2-20241024-223043.ods" )-> list[spo2Rec]:
    data = get_data(fileNm)
    sheetNms = [k for k in data.keys()]
    sheet1Arr = data[sheetNms[0]]
    #print(f'sheet1Arr: {sheet1Arr}')
    spo2Arr=[]
    for r in sheet1Arr[1:]: #skip hdr
        try:
            rec = spo2Rec(*r)
            spo2Arr.append(spo2Rec(*r))
        except Exception as E:
            print(f'Error: {str(E)} in Record: {r}')
    return spo2Arr  

def hourDecimal(dtMin,dt,ti:datetime):
    #add 24 hrs if date passes
    addHrs =0 if dt==dtMin else 24
    return(ti.hour*3600+ti.minute*60+ti.second)/3600 + addHrs

def main():
    spO2FileNms = ['SpO2-20241206-045639.ods','LathaSpO2-20241029-230021.ods','SpO2-20241024-223043.ods','SpO2-20241026-224044.ods','SpO2-20241027-161248.ods']
    spo2Arr = getDatafromOds(spO2FileNms[0])
    #x-axia time seq
    dtMin,dtMax = min(x.dt for x in spo2Arr), max(x.dt for x in spo2Arr)
    hrTimeSeq = [hourDecimal(dtMin,x.dt,datetime.strptime(x.ti,'%I:%M:%S %p')) for x in spo2Arr ]
    tMin,tMax=hrTimeSeq[0],hrTimeSeq[-1]
    granularitySeconds = (tMax-tMin)/len(hrTimeSeq) *3600
    # y-axis seq
    spo2Seq,hrSeq = [x.spo2 for x in spo2Arr ],[x.hr for x in spo2Arr ]
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.plot(hrTimeSeq, spo2Seq)       #x axis and y-values
    ax.plot(hrTimeSeq,hrSeq)
    ax.set_xlabel(f'Hour - 24H : {dtMin} to {dtMax} (every {granularitySeconds:.2f} seconds)', fontweight ='bold')
    ax.set_ylabel('SpO2 above/Hr below', fontweight ='bold')
    
    hrUpperBound,hrLowerBound = 70,40
    spo2UB,spo2LB = 100,93
    ax.fill_between(hrTimeSeq,hrLowerBound,hrUpperBound, color='green', alpha=0.1, label='HeartRate')
    ax.fill_between(hrTimeSeq,spo2LB,spo2UB, color='green', alpha=0.1, label='SpO2')
    plt.title("Subject: L")
    plt.show()         


if __name__=='__main__': main()
