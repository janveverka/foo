#!/bin/env python
'''
Test the behaviour of logging in imported modules
'''
import logging

def main():
    logging.basicConfig(level=logging.WARNING,
                        format='%(levelname)s in %(module)s: %(message)s')
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message from sublog.')
    logger.info('This is an info message from sublog.')
    logger.warn('This is an warn message from sublog.')
    logger.error('This is an error message from sublog.')

if __name__ == '__main__':
    main()

