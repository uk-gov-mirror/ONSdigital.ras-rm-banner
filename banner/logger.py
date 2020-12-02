import logging
import os
import sys

logger_date_format = os.getenv('LOGGING_DATE_FORMAT', "%Y-%m-%dT%H:%M%s")

# 20 means info level of severity
log_level = os.getenv('LOGGING_LEVEL', 20)  
logger= logging.getLogger(__name__)

# for basic configurations, calling basicConfig() to configure the root logger 
# stdout is the destination to log the message.
logging.basicConfig(stream=sys.stdout, level=log_level, format="%(name)s %(message)s")

logger.info("started")


