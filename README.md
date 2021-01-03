# Pi Doorbell

A Python script to play music to home supported Chromecast devices when an analog doorbell button is pressed.

## Setup

Wire ground and available GPIO pin to DC voltage points on the doorbell. Ensure that you don't apply a voltage of >3.3v and 0.5mA to the pins, otherwise you will damage the GPIO board. I recommend making a voltage divider circuit as per below:

![Voltage Divider](http://www.learningaboutelectronics.com/images/Voltage-divider-circuit.png)

You can calculate the resistors to use on this [Voltage Divider Calculator](http://www.learningaboutelectronics.com/Articles/Voltage-divider-calculator.php).

## Dependencies

This project uses [Python 3](https://www.python.org/download/releases/3.0/) and [catt](https://github.com/skorokithakis/catt) to cast a music file to supported Chromecast devices on a local network.

## Configuration

Two scripts are used; a shell script and python script. Both are located in the [scripts](https://github.com/eliotharper/pi-doorbell/tree/master/scripts) directory. 

The shell script executes the catt command to cast an mp3 file to one or more Google devices.

## Logging

Output is logged to a 'nohup.out' folder along with a date time stamp each time the process executes.

## Usage

Run the following command to start monitoring a doorbell voltage drop on the designated Raspberry Pi GPIO pin.

```
python doorbell.py &
```

It's recommended that you add the following line to auto-run the script on startup. Run the command `sudo nano /etc/profile` and add the line below to the end of the file. Alternatively, review [other options](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/) for running scripts on startup.

```
python /home/pi/Scripts/doorbell.py &
```

