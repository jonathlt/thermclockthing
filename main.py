import machine, ssd1306, time, utime, onewire, ds18x20
from ntptime import settime

# Set up the display
i2c = machine.I2C(scl=machine.Pin(16),sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128,64,i2c,0x3c)

# Set up the temperature sensor
dat = machine.Pin(2)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()

counter = 0

while counter < 5:
    #Show the time
    settime()
    tm = utime.localtime()
    year, month, mday, hour, minute, second, weekday, yearday = tm
    oled.fill(0)
    oled.text(str(hour) + ":" + str(minute),0,0)
    #Show the temperature
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds.read_temp(rom)
    oled.text(str(temp),0,10)
    oled.show()
    time.sleep(1)
    counter = counter + 1
