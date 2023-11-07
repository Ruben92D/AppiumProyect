import logging
logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s",filename="test.log", datefmt="%d/%m/%y %I:%M:%S %p %A", level=logging.DEBUG)
logging.critical("this is critical")
logging.error("this is an errror")
logging.warning("this is a warning")
logging.info("this is an info")
logging.debug("this is debugging")