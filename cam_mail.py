#!/usr/bin/python

#creates email and sends it
#Example usage: to be defined
#one line for git

import sys, smtplib, os
from email.message import EmailMessage
# imghdr to find the types of our images
import imghdr
from cam_pictures import find_newpics
import logging
import cam_constants


class SendMail(object):
    # email-address receiver
    mailadress = cam_constants.MAIL_ADDRESS
    # mail-Server
    smtpserver = cam_constants.SMTPSERVER
    # own email-address
    username = cam_constants.MAIL_ADDRESS   
    password = cam_constants.MAIL_PW

    def send(self):
        """
        send email to hotmail server
        parameter: no parameter
        """
        to = cam_constants.MAIL_ADDRESS
        From = self.mailadress
        # Connect to server and send mail to hotmail
        server = smtplib.SMTP(self.smtpserver)
        server.ehlo() #Has something to do with sending information
        server.starttls() # Use encrypted SSL mode
        server.ehlo() # To make starttls work
        server.login(self.username, self.password)
        # prepare email
        msg = self.prepareEmail(to, From)
        failed = server.sendmail(From, to, msg.as_string())
        if failed == True:
            logging.info("send: Error sending E-Mail")
        server.quit()

    def prepareEmail(self, to, From):
        """
        prepares an object in EmailMessage-Format
        parameter:
        to: mail address receiver
        from: mail adress sender
        mail content is a standard information text with attachments (last pictures
        from cammera
        """
        lastpictures = []
        # prepare email
        msg = EmailMessage() 
        msg['From'] = From
        msg['To'] = to
        # msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = 'Bewegung von Kamera 1 entdeckt'
        # message body
        msg.set_content('motion: alert detected')
        # get last 3 pictures from cam
        # first: get directory
        # TODO extract from here and make class attribute
        pic_dir = cam_constants.PICTURE_DIR
        # findNew... give only filenames, but module give a chdir, so that file
        # automatically is looked for in the correct directory
        lastpictures = find_newpics(pic_dir, 3, ".jpg")
        # msg.add_header('Content-Disposition', 'attachment', filename='FRITZ-picture.jpg')
        # Open the files in binary mode.  Use imghdr to figure out the
        # MIME subtype for each specific image.
        for file in lastpictures:
            with open(file, 'rb') as fp:
                img_data = fp.read()
                msg.add_attachment(img_data, maintype='image',
                                     subtype=imghdr.what(None, img_data))
        return(msg)

if __name__ == '__main__':
    mail = SendMail()
    # Send all files included in command line arguments
    mail.send()
