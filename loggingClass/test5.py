import logging

logging.basicConfig(filename="test5.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    logging.info("I am trying to open the file")
    with open("sudh.txt","r"):
        logging.info("Successfully read the file")
except Exception as e:
    logging.critical("This is critical")
    logging.error(e) # ONLY log main error
    logging.exception(e) # give whole information of error/exception