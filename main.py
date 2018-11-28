import machine, ssd1306, time, utime, onewire, ds18x20
from ntptime import settime
import network

# Set up the display
i2c = machine.I2C(scl=machine.Pin(5),sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128,64,i2c,0x3c)

# Set up the temperature sensor
dat = machine.Pin(12)
ds = ds18x20.DS18X20(onewire.OneWire(dat))

def get_temp(ds_temp, num_dps):
    roms = ds_temp.scan()
    ds_temp.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds_temp.read_temp(rom)
    return round(temp, num_dps)

def dayofweek(d, m, y): 
	t = [ 0, 3, 2, 5, 0, 3, 
		5, 1, 4, 6, 2, 4 ] 
	y -= m < 3
	return (( y + int(y / 4) - int(y / 100) 
			+ int(y / 400) + t[m - 1] + d) % 7) 

def is_bst(time):
    # is it between November and Feb ?
    month = time[1]
    mday = time[2]
    hour = time[3]
    year = time[0]

    def last_sunday_in_month(year, month):
        last_sunday = 0
        days_in_month = 31
        for i in range(31, 0, -1):
            if dayofweek(i, month, year) == 0:
                last_sunday = i
                break
        return last_sunday

    last_sunday_in_march = last_sunday_in_month(year, 3)
    last_sunday_in_october = last_sunday_in_month(year, 10)

    if month >= 11 or month <= 2:
        return False
    else:
        if month >= 4 and month <= 9:
            return True
        if month == 3 and mday >= last_sunday_in_march and hour >= 1:
            return True
        if month == 10 and mday >= last_sunday_in_october and hour >= 2:
            return True

def get_time():
    try:
        settime()
    except:
        print('.')
        pass
    tm = utime.localtime()
    year, month, mday, hour, minute, second, weekday, yearday = tm
    if is_bst(tm):
        hour = hour + 1
    return year, month, mday, hour, minute, second, weekday, yearday

def format_time(hour, minute):
    hour_str = ""
    minute_str = ""
    if hour < 10:
        hour_str = "0" + str(hour)
    else:
        hour_str = str(hour)
    if minute < 10:
        minute_str = "0" + str(minute)
    else:
        minute_str = str(minute)
    return hour_str + ":" + minute_str

while True:

    tm = get_time()
    #Show the date
    day = tm[2]
    month = tm[1]
    year = tm[0]
    oled.fill(0)
    print(month)
    oled.text(str(day) + '/' + str(month) + '/' + str(year),30 ,0)
    #Show the time
    hour = tm[3]
    minute = tm[4]
    oled.text(format_time(hour, minute), 45, 10)
    #Show the temperature
    temp = get_temp(ds, 1)
    oled.text(str(temp) + "C", 45, 40)
    oled.show()
    time.sleep(1)

