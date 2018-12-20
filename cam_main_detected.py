# program is called after motion detection
# call is part of motion.conf either on_event_start or
# on_event_end

import os
import time
import logging
from cam_stamp import CamTimestamp
from cam_mail import SendMail

# configuration error logger
# TODO later set limitatation to x MB, use logging.handlers.RotatingFileHandler
logging.basicConfig(format='%(asctime)s %(message)s', \
datefmt='%d/%m/%Y %I:%M:%S %p', \
filename='soncam.log', \
level=logging.DEBUG)

# set default for picture directory
pic_dir = "/Users/manfredsonner/Desktop/Projekte/repositories/cam_project/picture_examples"
# TODO get env variable PICTURE_DIR of picture directory,
# if there is not any keep the default

# list of snapshots
piclist = []
                           
# sleep and wait a moment, motion needs time to store the pictures
time.sleep(2)

# check if there was already a mail sent - prevent an email tsunami
ok_tosend = CamTimestamp()
ok_mail = SendMail()

if ok_tosend.shouldSend() == True:
    # send email with standard text and last new pictures as attachment
    ok_mail.send()
    # TODO log it
else:
    # send no mail
    # TODO log it
    pass

