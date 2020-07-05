date & catt --device 'Upstairs Wifi' cast ~/Music/doorbell.mp3 & catt --device 'Kitchen Wifi' cast ~/Music/doorbell.mp3
PID=`ps -eaf | grep syncapp | grep -v grep | awk '{print $2}'`
if [[ "" !=  "$PID" ]]; then
  kill -9 $PID
fi