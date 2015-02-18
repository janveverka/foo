#!/bin/env python
# -*- coding: utf-8 -*-
'''
Test the behaviour of logging in imported modules
'''
import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(levelname)s: %(module)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def main():
    msg = ' message from foo/log/auxiliary.py'
    logger.debug('Debug'   + msg)
    logger.info ('Info'    + msg)
    logger.warn ('Warning' + msg)
    logger.error('Error'   + msg)
    logger.info('__name__: %s', __name__)

if __name__ == '__main__':
    main()

