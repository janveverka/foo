#!/bin/env python
'''
Test the behaviour of logging in imported modules

Questions and Answers:
Q1. What configuration is in effect when logging.basicConfig is called
    multiple times, e.g. in imported modules?
A1. The one that is used in the first call to logging.basicConfig.
    "As it’s intended as a one-off simple configuration facility, only the 
    first call will actually do anything: subsequent calls are effectively 
    no-ops." 
    --- https://docs.python.org/2/howto/logging.html#logging-basic-tutorial 
'''
import logging

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s in %(module)s: %(message)s')
    logger = logging.getLogger(__name__)
    import sublog
    sublog.main()
    logger.debug('This is a debug message from log.')
    logger.info('This is an info message from log.')
    logger.warn('This is an warn message from log.')
    logger.error('This is an error message from log.')

if __name__ == '__main__':
    main()

