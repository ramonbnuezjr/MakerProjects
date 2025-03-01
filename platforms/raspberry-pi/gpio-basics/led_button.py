# Importing the necessary libraries.
import gpiozero as gz
import time as t

# Defining the LED and Button objects.
led = gz.LED(17)
button = gz.Button(27)

print("Program starting. Press teh button.")

#Adding Define print statements, for debugging.
while True:
	if button.is_pressed:
		print("Buton is pressed: LED On.")
		led.on()
	else:
		print("Button is released: LED OFF.")
		led.off()

# Small delay so not to overwhelm the CPU.
t.sleep(0.1)
