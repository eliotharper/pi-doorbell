# Pi Doorbell

A Python to cast doorbell music to home Google devices.

## Setup

Wire ground and available GPIO pin to DC voltage points on the doorbell. Ensure that you don't apply a voltage of >3.3v and 0.5mA to the pins, otherwise you will damage the GPIO board. I recommend making a voltage divider circuit as per below:

![Voltage Divider](http://www.learningaboutelectronics.com/images/Voltage-divider-circuit.png)

You can calculate the resistors to use on this [Voltage Divider Calculator](http://www.learningaboutelectronics.com/Articles/Voltage-divider-calculator.php).

## Dependencies

The script uses [catt](https://github.com/skorokithakis/catt).

## Configuration

Two scripts are used; a shell script and python script. Both are located in the [scripts](https://github.com/eliotharper/pi-doorbell/tree/master/scripts) directory. 

The shell script executes the catt command to cast an mp3 file to one or more Google devices.

Note, the shell script kills the process after executing the command, as catt requires manual intervention when using the command line (you need to press ctrl+c when executing the command manually).

The Python script listens for a voltage drop on a defined GPIO pin then runs the command `nohup sh doorbell.sh &` to run the shell script in the background.

## Logging

Output is logged to a 'nohup.out' folder along with a date time stamp each time the process executes.

## Usage

Run the following command to start monitoring a doorbell voltage drop on the designated Raspberry Pi GPIO pin.

```
python doorbell.py
```

It's recommended that you add the following line to your crontab file (edit using `crontab -e` command) to ensure that the script runs on startup. Alternatively, review [other options](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/) for running scripts on startup.

```
@reboot sudo python /home/pi/Scripts/doorbell.py
```

