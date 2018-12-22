
import time
import datetime
import logging
import os
import cam_constants


class CamTimestamp:
	'''
	handles minimum time between 2 mails in order to prevent to many mails sent
	NEWMAIL_GAP: mimimum times in seconds between 2 mails, a default value is set
	'''
	

	# set minimum time gap between 2 mails to default, units are seconds
	# TODO before going productive set this value e.g. to 1800, otherwise you risk tsunami
	min_gap = 15
	
	def __init__(self):
		# TODO read here env variable TIMESTAMP_CAM and NEWMAIL_GAP in class attributes,
		# if no successful keep on using default
		pass
	
	def shouldSend(self):
		''' 
		checks at which time last email was sent to prevent email tsunami
		
		reads time of last email sending from file TIMESTAMP_CAM and check 
		if the passed time is bigger than NEWMAIL_GAP minutes, 
		in this case the time stamp is newly set, means current time is written in file
		
		returns True when last email was sent before NEWMAIL_GAP minutes - send email
		returns False if there was an email sent in this period - send no email
		'''
		last_time = self._get_timestamp()
		# get current time
		current_time =time.time()
		# time difference in seconds
		time_diff = current_time - last_time
		# 
		# if time difference bigger than minimimum
		if time_diff > self.min_gap: 
			# set new timestamp, better after sending email 
			# in first try no attention to return values
			self._set_timestamp(current_time)
			logging.info('shouldSend: time_diff exceeds limit, new timestamp was set')
			return True
		else:
			# no new email necessary, no new timestamp
			logging.info('shouldSend: time_diff under limit')
			return False

	def _get_timestamp(self):
		''' 
		read last time email was sent from file TIMESTAMP_CAM

		returns time in minutes elapsed from last time a email was sent
		returns 0, if file cannot be read
		'''
		# TODO rebuild with <with>
		try:
			# open and read last timestamp
			fp = open(cam_constants.TIMESTAMP_CAM,'r')
			gap = float(fp.read())
			fp.close()
		except OSError:
			logging.warning('get_timestamp: cannot open file')
			# give back 0, so the mail is sent in any case
			# that could raise problems - imagine hard disk full or access problems
			# in this case there would be no brake for a possible tsunami, 
			gap = 0
			return gap
		except:
			logging.warning('get_timestamp: unexpected error')
			# give back 0, so the mail is sent in any case
			# keep in mind comment above OSerror section
			gap = 0
			# fp.close()
			return gap
		return gap
	
	def _set_timestamp(self, new_time):
		'''
		set timestamp, means write current into file TIMESTAMP_CAM
		
		time is written in absolute seconds, no readable time format
		returns True if every is ok
		returns False if there were writing errors
		'''
		try:
			# open or create, if file not exists
			fp = open(cam_constants.TIMESTAMP_CAM,'w+')
			fp.write(str(new_time))
			fp.close()
			return True
		except OSError:
			logging.warning('set_timestamp: cannot open file')
			# 
			return False
		except:
			logging.warning('set_timestamp: cannot open file')
			# no fp.close(), could lead to problems
			return False

if __name__ == "__main__":
	
	# configuration error logger
	# TODO later set limitatation to x MB, use logging.handlers.RotatingFileHandler
	logging.basicConfig(format='%(asctime)s %(message)s', \
	datefmt='%d/%m/%Y %I:%M:%S %p', \
	filename=cam_constants.LOG_FILE, \
	level=logging.DEBUG)

	timestamp = CamTimestamp()	
	to_send = timestamp.shouldSend()
	print(to_send)

		

