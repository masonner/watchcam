
import time
import datetime
import logging


class CamTimestamp:
	'''
	handles minimum time between 2 mails in order to prevent to many mails sent
	environment variables are needed to be set 
	TIMESTAMP_CAM: filename for last timestamp, a default value is ser
	NEWMAIL_GAP: mimimum times in seconds between 2 mails, a default value is set
	'''
	
	# set filename for storing last call time to default
	# TODO include path
	stamp_file = 'stamp_default.txt'
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
		print('time stamp:',last_time)
		# get current time
		current_time =time.time()
		print('current time:', current_time)
		# time difference in seconds
		time_diff = current_time - last_time
		print('time difference',time_diff)
		# 
		# if time difference bigger than minimimum
		if time_diff > self.min_gap: 
			# set new timestamp, better after sending email 
			# in first try no attention to return values
			self._set_timestamp(current_time)
			logging.info('shouldSend: time_diff exceeds limit, new timestamp was set')
			print('set new time stamp')
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
		try:
			# filename: see class attribute
			fp = open(self.stamp_file,'r')
			gap = float(fp.read())
			fp.close()
		except OSError:
			print('get: cannot open file')
			logging.warning('get_timestamp: cannot open file')
			# give back 0, so the mail is sent in any case
			# that could raise problems - imagine hard disk full or access problems
			# in this case there would be no brake for a possible tsunami, 
			gap = 0
			return gap
		except:
			print('get: unexpected error')
			logging.warning('get_timestamp: unexpected error')
			# give back 0, so the mail is sent in any case
			# keep in mind comment above OSerror section
			gap = 0
			fp.close()
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
			# filename: see class attribute
			fp = open(self.stamp_file,'w')
			fp.write(str(new_time))
			fp.close()
			return True
		except OSError:
			print('set: cannot open file')
			logging.warning('set_timestamp: cannot open file')
			# 
			return False
		except:
			print('set: unexpected error')
			logging.warning('set_timestamp: cannot open file')
			# no fp.close(), could lead to problems
			return False

if __name__ == "__main__":
	
	# configuration error logger
	# TODO later set limitatation to x MB, use logging.handlers.RotatingFileHandler
	logging.basicConfig(format='%(asctime)s %(message)s', \
	datefmt='%d/%m/%Y %I:%M:%S %p', \
	filename='soncam.log', \
	level=logging.DEBUG)

	timestamp = CamTimestamp()	
	to_send = timestamp.shouldSend()
	print(to_send)

		

