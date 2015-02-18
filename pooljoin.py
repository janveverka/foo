#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time, sys, getopt, fcntl
import traceback
from multiprocessing.pool import Pool
import multiprocessing
import logging
from multiprocessing.pool import ThreadPool

def error(msg, *args):
    return multiprocessing.get_logger().error(msg, *args)

class LogExceptions(object):
    def __init__(self, callable):
        self.__callable = callable
        return

    def __call__(self, *args, **kwargs):
        try:
            result = self.__callable(*args, **kwargs)

        except Exception as e:
            # Here we add some debugging help. If multiprocessing's
            # debugging is on, it will arrange to log the traceback
            error(traceback.format_exc())
            # Re-raise the original exception so the ThreadPool worker can
            # clean up
            raise

        # It was fine, give a normal answer
        return result
    pass

class LoggingPool(ThreadPool):
    def apply_async(self, func, args=(), kwds={}, callback=None):
        return ThreadPool.apply_async(self, LogExceptions(func), args, kwds, callback)

def go(count):
    print "BEGIN: ",count
    sleepTime = 3
    if(count%5==1 or count%5==2): sleepTime = 10
    time.sleep(sleepTime)
    print "END: ",count,sleepTime

nThreadsMax=5
multiprocessing.log_to_stderr()
multiprocessing.get_logger().setLevel(logging.ERROR)
p = LoggingPool(processes=nThreadsMax)
os.system("rm -f test.txt")

count = 0
while count < 50:
   #print "count: ",count
   count = count + 1
   process = p.apply_async(go, [count])
p.close()
p.join()

