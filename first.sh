sudo apt-get update 
sudo apt-get install pip
sudo apt-get install tmux 
sudo apt-get install ffmpeg
sudo apt-get install imagemagick
cat /etc/ImageMagick-6/policy.xml | sed 's/none/read,write/g'> /etc/ImageMagick-6/policy.xml
tmux new

