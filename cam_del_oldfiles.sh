# !/bin/sh
# script deletes all pictures and movie older than x days 
# (motion generated ones)
# expects no parameters
IMAGE_DIR=/home/pi/Bilder/cam
# number of days, if this not works use -mmin 360 (e.g. 6 hours)
# option -delele is missing, for security reason
sudo chown pi $IMAGE_DIR/*.*
find $IMAGE_DIR -mtime +1 -type f -delete 

