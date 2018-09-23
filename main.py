import machine, ssd1306, time, utime, onewire, ds18x20
from ntptime import settime

# Set up the display
i2c = machine.I2C(scl=machine.Pin(16),sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128,64,i2c,0x3c)

# Set up the temperature sensor
dat = machine.Pin(2)
ds = ds18x20.DS18X20(onewire.OneWire(dat))

def get_temp(ds_temp, num_dps):
    roms = ds_temp.scan()
    ds_temp.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds_temp.read_temp(rom)
    return round(temp, num_dps)

counter = 0

while counter < 5:
    #Show the time
    settime()
    tm = utime.localtime()
    year, month, mday, hour, minute, second, weekday, yearday = tm
    oled.fill(0)
    oled.text(str(hour) + ":" + str(minute),0,0)
    #Show the temperature
    temp = get_temp(ds, 1)
    oled.text(str(temp),0,10)
    oled.show()
    time.sleep(1)
    counter = counter + 1
