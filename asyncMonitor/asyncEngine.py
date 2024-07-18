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