'''
Created on Nov 14, 2015

@author: Juan_Insuasti
'''


import mraa
import time
import pyupm_grove as Grove
import pyupm_i2clcd as lcd
import random


light = Grove.GroveLight(0)

def PWM(lux):
    '''
    funcion pwm
    ''' 
    pwm = mraa.Pwm(5)
    pwm.period_us(100) # Set the period as 5000 us or 5ms
    pwm.enable(True)    # enable PWM
    pwm.write(2*lux/100.0)
        
    if lux <= 10:
        print("ALARM")
        #pwm.write(1)
        
    else:
        #pwm.write(0)
        pass

    
    
    
    
    
if __name__ == '__main__':    
    

    # Read the input and print both the raw value and a rough lux value,
    # waiting one second between readings
    while 1:
        print light.name() + " raw value is %d" % light.raw_value() + \
            ", which is roughly %d" % light.value() + " lux";
        
        print(light.value()/100.0)
        PWM(2*light.value())
        #time.sleep(1)
    
    # Delete the light sensor object
    
    
    del light
    
    
    pass