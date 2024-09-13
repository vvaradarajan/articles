# A model for an async bot engine

## Intro

A coding situation that occurs quite often, is the need to have a monitoring process, that keeps track of and reacts to events. The requirement is that this monitor should be independent of system/event that it is monitoring. This  monitor then, should be a separate process, or a separate thread or an async task.  In this article the last alternative of ‘async task’ is explored. A model of how this can be constructed is developed and includes a working example at the end.

## Overview

An async engine is an async loop that asynchronously waits for some event to  to process. It is similar to thread in terms of executing independently of other code within system. Unlike threads which are allocated processing time by the underlying operating system, the processor allocation occurs by use of ‘await’ – i.e. give up the processor to other tasks.  Asyncio in python works in this manner.

There are many use cases for such an engine. One is a system ‘heartbeat’ reporter that does a ‘system’ check at regular intervals to ensure that the system is ‘up’. Another is a bot engine that monitors some variable such as temperature, price of a particular stock etc. at regular intervals and performs some action based on it value.

A simple model for coding an async engine is constructed here using object oriented paradigm i.e. using a class. This class is built around its core part: the async loop.

Conceptually it is convenient to think of async processes as having a certain ‘freedom’ similar to objects along with the ability to run their own tasks. They can be controlled via calls to their methods and manipulating their members.  Using this object oriented  approach we just have to think of the methods and members we need to control the async process.

## Design

The core part of the async engine is the async loop that has an ‘await’ along with other processing logic. The ‘await’ could be waiting for an event or for an interval of time.  We build methods and a member around this core part to facilitate starting and stopping this loop.

### Methods:

<b>run</b>: This method starts the core async loop as a separate task and returns.

<b>Stop:</b> This function sets a variable ‘active’ to false, and waits for the core-loop to exit.

### Members:

<b>stopEvent</b>: An asyncio event that is set by the core loop to indicate termination of the core task

<b>active:</b> A boolean which when true indicates the async engine is running

## Design Overview diagram:
<img src="img/asyncBot.jpeg" />

## Implementation

Now it is time to transform this diagram to code.. Since we are having record-breaking heat, an appropriate exercise is to create a monitor that can warn of impending heat stroke would help!

Below is an implementation of the model, with the core task being measurement of temp every 2 seconds and print a warning when it exceeds 100.

```python
import asyncio

class AsyncHeatStrokeEngine:
    def __init__(self,coreFunc,interval=2, limit=100):
        self.stopEvent=asyncio.Event()
        self.taskFunc=coreFunc #a function to measure the temperature
        self.name='Temperature Monitor'
        self.active=False
        #coreFunc related parameters
        self.measurementInterval=interval
        self.tempLimit=limit

    def run(self):
        self.active=True
        self.task = asyncio.create_task(self.measureTask())

    async def stop(self):
        self.active=False
        await self.stopEvent.wait()


    async def measureTask(self):
        print(f'{self.name} started')
        while self.active:
            if self.stopEvent.is_set(): break
            await asyncio.sleep(self.measurementInterval)
            curTemp = self.taskFunc()
            if curTemp > self.tempLimit:
                print(f"*** Warning : Temp is {curTemp}..Drink water, seek A/C to guard against heat stroke!")
            else:
                print(f"Not Too Bad: You will probably surive a temperature of {curTemp}..")
        self.stopEvent.set()
        print(f'{self.name} stopped')

# code below exercises the engine
import random
prevTemp=98.7
def getTemperature():
    #temperature measurement function (#returns a reasonable random temperature)
   return random.uniform(prevTemp,prevTemp+5)

async def main():
    x=AsyncHeatStrokeEngine(getTemperature)
    x.run()
    await asyncio.sleep(10) #Let the temperature monitor run for 10 seconds
    await x.stop()

if __name__=='__main__':
    asyncio.run(main())
```
Output
```
$ python3 asyncEngine.py 
Temperature Monitor started
*** Warning : Temp is 100.11097782778835..Drink water, seek A/C to guard against heat stroke!
Not Too Bad: You will probably surive a temperature of 99.98313998095253..
*** Warning : Temp is 101.07593387042367..Drink water, seek A/C to guard against heat stroke!
*** Warning : Temp is 102.67003188013372..Drink water, seek A/C to guard against heat stroke!
Not Too Bad: You will probably surive a temperature of 98.73400679989041..
Temperature Monitor stopped
```
## Conclusion

Be safe..use this design to code a monitor!

A simple model with just two methods and two members will make writing your monitor straightforward.

