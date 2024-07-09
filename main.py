import RPi.GPIO as GPIO
import time

# 设置引脚编号模式为 BCM
GPIO.setmode(GPIO.BCM)

# 设置 GPIO 7 为输入引脚
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 启用上拉电阻

print("开始监听传感器状态变化...")

# 读取引脚状态
try:
    while True:
        input_state = GPIO.input(7)
        if input_state == GPIO.HIGH:
            print("门是关的")
        else:
            print("门是开的")
        time.sleep(1)  # 每秒读取一次状态
except KeyboardInterrupt:
    # 清理 GPIO 设置
    GPIO.cleanup()
    print("程序已终止")
