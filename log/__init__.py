#!/bin/env python
# -*- coding: utf-8 -*-
'''
Test the behaviour of logging in imported modules

Questions and Answers:
Q1. What configuration is in effect when logging.basicConfig is called
    multiple times, e.g. in imported modules?
A1. The one from the first call.
    "As it’s intended as a one-off simple configuration facility, only the 
    first call will actually do anything: subsequent calls are effectively 
    no-ops."
    --- https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
Q2. How to keep the defaults of imported sub-modules?
Q3. How to over-ride the defaults of imported sub-modules?
Q4. How to keep the defaults of imported 3rd-party modules?
Q4. How to over-ride the defaults of imported 3rd-party modules?

Interesting relevant reading:
https://docs.python.org/2/howto/logging.html#configuring-logging-for-a-library
http://pieces.openpolitics.com/2012/04/python-logging-best-practices/
http://stackoverflow.com/questions/15727420/using-python-logging-in-multiple-modules

'''
import logging
import logging.config
import auxiliary

def main():
    # This overrides the setting done in auxiliary
    #logging.getLogger('foo.log.auxiliary').setLevel(logging.INFO)
    auxiliary.main()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    lhandler = logging.StreamHandler()
    lhandler.setLevel(logging.INFO)
    lformatter = logging.Formatter('%(levelname)s in %(name)s: %(message)s')
    lhandler.setFormatter(lformatter)
    logger.addHandler(lhandler)
    print '%s handlers: %s' % (__name__, str(logger.handlers))
    print 'root handlers: %s' % str(logging.getLogger('root').handlers)
    msg = ' message from foo/log/__init__.py'
    logger.debug('Debug'   + msg)
    logger.info ('Info'    + msg)
    logger.warn ('Warning' + msg)
    logger.error('Error'   + msg)
    logger.info('__name__: %s', __name__)

if __name__ == '__main__':
    main()

