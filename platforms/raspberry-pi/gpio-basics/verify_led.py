# Load the libraries.
import gpiozero as gz
import time as t

# Create the LED object.
led = gz.LED(17)

# Test the LED.
print("LED should turn on for 5 seconds.")
led.on()
t.sleep(5)

print("LED should turn off.")
led.off()
t.sleep(1)

print("LED should blink 5 times.")
led.blink(on_time=0.5, off_time=0.5, n=5, background=False)

print("Test Complete.")
