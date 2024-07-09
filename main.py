from machine import Pin
import time

# 设置 GPIO 7 为输入引脚，并启用上拉电阻
door_sensor = Pin(7, Pin.IN, Pin.PULL_UP)

print('开始监听传感器状态变化...')

# 读取引脚状态
try:
    while True:
        input_state = door_sensor.value()
        if input_state == 1:
            print('门是关的')
        else:
            print('门是开的')
        time.sleep(1)  # 每秒读取一次状态
except KeyboardInterrupt:
    print('程序已终止')

