>>> import onewire, ds18x20
dat = machine.Pin(2)
>>> ds = ds18x20.DS18X20(onewire.OneWire(dat))
>>> roms = ds.scan()
>>> print('found devices:', roms)
found devices: [bytearray(b'\x10,v\x13\x02\x08\x00H')]
>>> for i in range(10):
...     print('temperatures:', end=' ')
...     ds.convert_temp()
...     time.sleep_ms(750)
...     for rom in roms:
...         print(ds.read_temp(rom), end=' ')
...         
...     print()


scl = 16
sda = 5

>>> import machine
>>> i2c = machine.I2C(scl=machine.Pin(16), sda=machine.Pin(5))
>>> devices = i2c.scan()
>>> print(len(devices))
1
>>> print(hex(device))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'device' is not defined
>>> print(hex(devices))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't convert list to int
>>> print(hex(devices[0]))
0x3c
>>> 
https://diyprojects.io/oled-display-ssd1306-micropython-example-digital-barometer-bme280-i2c/#.W42eynWnFhF

>>> import machine, ssd1306
>>> i2c = machine.I2C(scl=machine.Pin(16),sda=machine.Pin(5))
>>> oled = ssd1360.SSD1306_I2C(128,64,i2c,0x3c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ssd1360' is not defined
>>> oled = ssd1306.SSD1306_I2C(128,64,i2c,0x3c)
>>> oled.fill(0)
>>> oled.text("Hello World",0,0)
>>> oled.show()
>>> 
>>> sta_if = network.WLAN(network.STA_IF)
>>> print(sta_if.isconnected())
True
>>> from ntptime import settime
>>> settime()
(2018, 9, 5, 21, 1, 35, 2, 248)
>>> print(utime.localtime())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'utime' is not defined
>>> import utime
>>> t = time()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> tm = utime.localtime()
>>> print(tm)
(2018, 9, 5, 21, 4, 25, 2, 248)
>>> year, month, mday, hour, minute, second, weekday, yearday = tm
>>> print(hour)
21
>>> 



