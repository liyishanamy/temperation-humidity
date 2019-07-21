import Adafruit_DHT
import I2C_LCD_driver
from time import * 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=05
 
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
mylcd = I2C_LCD_driver.lcd()
while True:
	mylcd.lcd_display_string('Temp={0:0.1f}*C'.format(temperature), 1)
	print(humidity)
	mylcd.lcd_display_string('Humidity='+str(humidity), 2)
