
from time import time

class StopWatch:
    '''Models stopwatch for measuring elapsed time'''

    INIT_STATE = 0
    RUN_STATE = 1
    STOP_STATE = 2
    STATE_REPR = ["init", "running", "stop"]

    def __init__(self):
        self.__state = StopWatch.INIT_STATE
        self.__laps = []
        # following attributes are irrelevant in init state
        self.__startTime = 0.0
        self.__endTime = 0.0
        self.__lapStartTime = 0.0
 
    def start(self):
        '''Sets start time to current time and
           changes state to run state.
           Raises UserWarning if state is not init
        '''
        if self.__state == StopWatch.INIT_STATE:
            self.__startTime = self.__lapStartTime = time()
            self.__state = StopWatch.RUN_STATE
        elif self.__state == StopWatch.STOP_STATE:
            self.__state = StopWatch.RUN_STATE
        else:
            raise UserWarning('start method is not supported in ' + \
                              StopWatch.STATE_REPR[self.__state] + \
                              ' state')

    def stop(self):
        '''Sets end time to current time and
           changes state to stop state.
           Raises UserWarning if state is not run
        '''
        if self.__state == StopWatch.RUN_STATE:
            self.__endTime = time()
            self.__state = StopWatch.STOP_STATE

            # add latest elapsed time to last lap
            if len(self.__laps):
                self.__laps.append(self.__endTime - self.__lapStartTime)
        else:
            raise UserWarning('stop method is not supported in ' + \
                              StopWatch.STATE_REPR[self.__state] + \
                              ' state')

    def lap(self):
        '''Adds the elapsed time to laps and
           updates start time
           Raises UserWarning if state is not run
        '''
        if self.__state == StopWatch.RUN_STATE:
            currentTime = time()
            self.__laps.append(currentTime - self.__lapStartTime)
            self.__lapStartTime = currentTime
        else:
            raise UserWarning('lap method is not supported in ' + \
                              StopWatch.STATE_REPR[self.__state] + \
                              ' state')        

    def reset(self):
        '''Changes state to init state.
           The start time and end time are irrelevant in init state
        '''
        if self.__state == StopWatch.STOP_STATE:
            self.__state = StopWatch.INIT_STATE
            self.__laps.clear()
        else:
            raise UserWarning('reset method is not supported in ' + \
                              StopWatch.STATE_REPR[self.__state] + \
                              ' state')

    def getElapsedTime(self):
        '''Returns 0 in init state,
           or difference between end time and start time in stop state,
           or difference between current time and start time in run state.
        '''
        if self.__state == StopWatch.INIT_STATE:
            return 0
        elif self.__state == StopWatch.STOP_STATE:
            return self.__endTime - self.__startTime
        else: # RUN_STATE
            return time() - self.__startTime

    def getLapsElapsedTime(self):
        '''Returns a list of elpased time of all laps'''
        if not len(self.__laps):
            return []

        # self.__laps is always empty in init state
        laps = self.__laps.copy()        
        if self.__state == StopWatch.RUN_STATE:
            # add current running lap to the end
            laps.append(time() - self.__lapStartTime)

        return laps
            
    def __str__(self):
        s =  'StopWatch State: ' + StopWatch.STATE_REPR[self.__state] + \
             '\nStart Time: ' + format(self.__startTime, "18.6f") + \
             '\nEnd   Time: ' + format(self.__endTime, "18.6f") + '\n'
        for i in range(len(self.__laps)):
            s += 'Lap ' + str(i+1) + ': ' + format(self.__laps[i], "18.6f") + '\n'

        return s

# Following is the code for testing

from random import randrange
from time import sleep

def testStopWatch():
    '''Function for testing the class StopWatch'''

    # testing normal operation
    sw = StopWatch()
    print(sw)
    print("reading:", sw.getElapsedTime())
    print("starting...")
    sw.start()
    print(sw)
    sleep(randrange(5))
    print("reading:", sw.getElapsedTime())
    print(sw)
    sleep(randrange(5))
    sw.lap()
    print("reading:", sw.getElapsedTime())
    print(sw)
    sw.lap()
    print("reading:", sw.getElapsedTime())
    print(sw)
    print("reading laps: ", sw.getLapsElapsedTime())
    print("stopping...")
    sw.stop()
    print("reading:", sw.getElapsedTime())
    print(sw)
    sleep(randrange(5))
    print("reading:", sw.getElapsedTime())
    print("reading laps: ", sw.getLapsElapsedTime())
    print(sw)
    print("resetting...")
    sw.reset()
    print(sw)
    print("reading:", sw.getElapsedTime())
    print("reading laps: ", sw.getLapsElapsedTime())

if __name__ == '__main__':
    testStopWatch()
    
    
