#chassis.py coding:utf-8 42 底盘电机的驱动

import RPi.GPIO as GPIO
import time

__gproEn        = 21    #使能信号
__gproPmw11     = 19
__gproPmw12     = 16
__gproPmw21     = 12
__gproPmw22     = 6
__ps            = []

def init():
    print('init')
    GPIO.setmode(GPIO.BCM)
    #使能信号
    GPIO.setup(__gproEn, GPIO.OUT)
    GPIO.output(__gproEn, True)
    GPIO.setup(__gproPmw11, GPIO.OUT)
    GPIO.setup(__gproPmw12, GPIO.OUT)
    GPIO.setup(__gproPmw21, GPIO.OUT)
    GPIO.setup(__gproPmw22, GPIO.OUT)
    p11 = GPIO.PWM(__gproPmw11, 100)
    p12 = GPIO.PWM(__gproPmw12, 100)
    p21 = GPIO.PWM(__gproPmw21, 100)
    p22 = GPIO.PWM(__gproPmw22, 100)

    # testP(p11, 80, 3, 'p11')
    # testP(p12, 80, 3, 'p12')
    # testP(p21, 80, 3, 'p21')
    # testP(p22, 80, 3, 'p22')
  #  testP(p11, 100, 3, 'p11')

    print('start1')
    p11.start(90)
    p21.start(90)
    time.sleep(2)
    # print('stop1')
    p11.stop()
    p21.stop()

    print('start2')
    p12.start(90)
    p22.start(90)
    time.sleep(2)
    # print('stop2')
    p12.stop()
    p22.stop()

    # print('start3')
    # p11.start(90)
    # p22.start(90)
    # time.sleep(2)
    # # print('stop3')
    # p11.stop()
    # p22.stop()

    print('start4')
    p12.start(90)
    p21.start(90)
    time.sleep(2)
    # print('stop4')
    p12.stop()
    p21.stop()

    # __ps[0] = [p11, p12]
    # __ps[1] = [p21, p22]
    #
    # gohead(80, 2)

def testP(p, c, t, pn):
    print('start:', pn, ", cycle:", c)
    p.start(c)
    time.sleep(t)
    p.stop()

def gohead(speed, t):
    print('start')
    __ps[0][0].start(speed)
    __ps[1][0].start(speed)
    time.sleep(t)
    print('stop')
    __ps[0][0].stop()
    __ps[1][0].stop()

if __name__ == '__main__':
    GPIO.cleanup()
    init()
#    gohead(50, 1);
    GPIO.cleanup()

# p = GPIO.PWM(channel, frequency) 创建一个 PWM 实例：
# p.start(dc)   # dc 代表占空比（范围：0.0 <= dc >= 100.0）
# p.ChangeFrequency(freq)   # freq 为设置的新频率，单位为 Hz
# p.ChangeDutyCycle(dc)  # 范围：0.0 <= dc >= 100.0
# p.stop() 停止 PWM：




