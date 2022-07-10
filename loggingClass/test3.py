import logging
logging.basicConfig(filename="test4.log",level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

def divide(a,b):
    logging.info("Values enter by user are %s and %s",a, b)
    try:
        logging.info("we are into the function")
        div = a/b
        logging.info("we have completed a division operation")
        logging.info("Result of the operation is %s",div)
        return div
    except Exception as e:
        logging.exception(e)

print(divide(3,5))
