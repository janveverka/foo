#!/bin/env python
# -*- coding: utf-8 -*-
'''
This is a test to understand the behaviour of multiprocessing and it's
ThreadPool.  It should answer these questions:

    * Does the processing of the parent block if the pool is exhausted or
      are the tasks queued somehow and the processing continues?
    * What is the purpose of ThreadPool.close() and ThreadPool.join()?
    * Does ThreadPool.join() block?
'''

import logging
import time
logger = logging.getLogger(__name__)

#______________________________________________________________________________
def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format=r'%(asctime)s %(name)s %(levelname)s: %(message)s',
    )
    driver = Driver(nloops=3, pool_size=2)
    driver.run()

#______________________________________________________________________________
class LoggingObject(object):
    def __init__(self):
        self.logger = logging.getLogger(type(self).__module__ + '.' +
                                        type(self).__name__)

#______________________________________________________________________________
class Driver(LoggingObject):
    def __init__(self, nloops=3, pool_size=2):
        super(Driver, self).__init__()
        self.nloops = nloops
        self.pool_size = pool_size
        self.work_slow = Sleeper(seconds_to_sleep = 1)
        self.work_fast = Sleeper(seconds_to_sleep = 0.1)
    def run(self):
        self.logger.info(
            'Starting %d loops with a pool of %d ...' % (
                self.nloops, self.pool_size
            )
        )
        for iloop in range(self.nloops):
            self.logger.info('Loop %d' % iloop)
            self.do_work(iloop)
        self.logger.info('Finished running with great succes!')
    def do_work(self, iloop):
        self.work_fast('fast job %d' % iloop)
        self.work_slow('slow job %d' % iloop)

#______________________________________________________________________________
class Sleeper(LoggingObject):
    def __init__(self, seconds_to_sleep):
        super(Sleeper, self).__init__()
        self.seconds_to_sleep = seconds_to_sleep
    def __call__(self, name=None):
        if name:
            self.logger.info('Starting %s ...' % name )
        time.sleep(self.seconds_to_sleep)
        if name:
            self.logger.info('Finished %s.' % name )

#______________________________________________________________________________
if __name__ == '__main__':
    main()