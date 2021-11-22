import logging

logging.basicConfig(
    level=logging.DEBUG,
    filemode='w',
    filename='log.txt',
    format='%(name)s - %(levelname)s - %(message)s'
)
logging.debug('This will getlogged')


