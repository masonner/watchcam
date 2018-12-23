# !.sh
# this scrips converts all .avi from motion to .m4v (ios) und puts them
# into the NAS - important NAS has to mounted (mount -a) 
# directory with images 
IMAGE_DIR=/home/pi/Bilder/cam
# buffer directory for .avi files - perhaps not needed at all
BUFFER_DIR=/home/pi/Bilder/cam_transfer/buffer
# NAS, mounted
NAS_DIR=/home/pi/fritz_speicher/

# move all .avi in buffer directory
cd $IMAGE_DIR
for file in *.avi; do
	cp  "$file" "/home/pi/Bilder/cam_transfer/buffer"
done 

# convert all .avi in ios readable format, -y should force overwriting
# and put them on the NAS
cd $BUFFER_DIR
for file in *.avi; do
	ffmpeg -y -i "$file" $NAS_DIR"$file.m4v"
done
# TODO rm all *._* buffer files in NAS_DIR
# remove all this ugly .avi.m4k double extension
# TODO log everything
