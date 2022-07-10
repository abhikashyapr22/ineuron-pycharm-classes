import logging

logging.basicConfig(filename="test1.log", level=logging.INFO)
logging.info("This is my very first code for logging")
logging.warning("this will try to log a warning")

l = [1, 2, 3, 4, 5, 6, 7]
for i in l:
    if i == 2:
        logging.info(i)
        logging.warning("this is warning for a user that they have found out 2 in the list")

logging.shutdown()