'''
This is a test to understand the behaviour of multiprocessing and it's
ThreadPool.  It should answer these questions:

    * Does the processing of the parent block if the pool is exhausted or
      are the tasks queued somehow and the processing continues?
    * What is the purpose of ThreadPool.close() and ThreadPool.join()?
    * Does ThreadPool.join() block?
'''

import logging
logger = logging.getLogger(__name__)

def main:
    logging.basicConfig(
        level=logging.DEBUG,
        format=r'%(asctime)s %(name)s %(levelname)s: %(message)s',
    )
    logger.info('Start')
    logger.info('Finished with great success!')

if __name__ == '__main__':
    main()