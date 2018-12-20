# program is called after motion detection
# call is part of motion.conf either on_event_start or
# on_event_end

import os
import time
import logging
from cam_stamp import CamTimestamp
from cam_mail import SendMail

logfile= os.getenv("LOG_FILE")
# configuration error logger
# TODO later set limitatation to x MB, use logging.handlers.RotatingFileHandler
logging.basicConfig(format='%(asctime)s %(message)s', \
datefmt='%d/%m/%Y %I:%M:%S %p', \
filename=logfile, \
level=logging.DEBUG)

# log
logging.info("main_detected: motion detected")
# sleep and wait a moment, motion needs time to store the pictures
time.sleep(2)
# check if there was already a mail sent - prevent an email tsunami
ok_send = CamTimestamp()
ok_mail = SendMail()
if ok_send.shouldSend() == True:
    # send email with standard text and last new pictures as attachment
    ok_mail.send()
    # log it
    logging.info("main_detected: mail sent")
else:
    # send no mail
    logging.info("main_detected: no mail sent (tsunami)")
    pass

