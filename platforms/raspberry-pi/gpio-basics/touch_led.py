from gpiozero import Button, LED
from signal import pause
import time

# Set up the touch sensor on GPIO17 (adjust if you used a different pin)
touch_sensor = Button(17, pull_up=False)

# Set up the LED on GPIO18
led = LED(18)

# Function to handle touch events
def handle_touch():
    print("Touch detected!")
    led.on()
    time.sleep(1)  # Keep LED on for 1 second
    led.off()

# Register the callback function
touch_sensor.when_pressed = handle_touch

print("Touch sensor program running. Press CTRL+C to exit.")

# Keep the program running
try:
    pause()
except KeyboardInterrupt:
    print("Program stopped")
