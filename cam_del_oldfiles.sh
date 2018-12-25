# !.sh
# script deletes all pictures and movie older than x days 
# (motion generated ones)
IMAGE_DIR=/home/pi/Bilder/cam
# number of days, if this not works use -mmin 360 (e.g. 6 hours)
# option -delele is missing, for security reason
find $IMAGE_DIR -mtime +1 -type f -delete 

