#blink .py

import mraa
import time
import pyupm_grove as Grove
import pyupm_i2clcd as lcd
import random


print (mraa.getVersion())
class Load():
	x = 0

x = Load()
temp = Grove.GroveTemp(0)


def test(args):
	
	if x.x == 1:
		x.x = 0
	else:
		x.x = 1
	
	print(x.x)

	#tambien leemos temperatura con el boton 

	print temp.name()
	for i in range(0, 10):
	    celsius = temp.value()
	    fahrenheit = celsius * 9.0/5.0 + 32.0;
	    print "%d degrees Celsius, or %d degrees Fahrenheit" \
	        % (celsius, fahrenheit)
	    
	# read pot/print/convert to string/display on lcd
	potVal = float(celsius)
	print potVal   
	potStr = str(potVal)
	lcdDisplay.setCursor(0, 0)
	lcdDisplay.write("Temp " + potStr + " Celsius")
	lcdDisplay.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))   


	time.sleep(1)

def test2(args):
	pass


#pin 4 en la tarjeta
led = mraa.Gpio(4)
led.dir(mraa.DIR_OUT)
print(x.x)
led.write(x.x)

#pin 6 en la tarjeta
button = mraa.Gpio(6)
button.dir(mraa.DIR_IN)

# display - lcd
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)


while(True):
	led.write(x.x)
	button.isr(mraa.EDGE_BOTH, test, test2)
	