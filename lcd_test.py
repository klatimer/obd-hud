import time
import Adafruit_CharLCD as LCD

lcd_rs = 27
lcd_en = 22
lcd_d4 = 16
lcd_d5 = 12
lcd_d6 = 25
lcd_d7 = 7
lcd_backlight = 21

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
			   lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
lcd.message('Hello\nworld!')
time.sleep(5.0)
lcd.clear()
