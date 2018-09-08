import machine, ssd1306, time

i2c = machine.I2C(scl=machine.Pin(16),sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128,64,i2c,0x3c)

counter = 0

while counter < 50:
    oled.fill(0)
    oled.text(str(counter),0,0)
    oled.show()
    time.sleep(1)
    counter = counter + 1
