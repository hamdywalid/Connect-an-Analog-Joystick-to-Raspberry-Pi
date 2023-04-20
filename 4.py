import socket
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

HOST = '192.168.1.100' 
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def motor_control(x_axis, y_axis):
    #Left 
    if y_axis > 0:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)

    #Right
    if y_axis < 0:
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
    else:
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)

    # Up and down 
    if x_axis < 0:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
    if x_axis > 0:
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)

while True:
    # send from joystick to Raspberry Pi
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            motor_control(x_axis, y_axis)
                    
    # send from Raspberry Pi to Arduino
    if GPIO.input(11) == GPIO.HIGH:
        s.sendall(b'11')
    else:
        s.sendall(b'99')
    if GPIO.input(13) == GPIO.HIGH:
        s.sendall(b'13')
    else:
        s.sendall(b'98')
    if GPIO.input(15) == GPIO.HIGH:
            s.sendall(b'15')
    else:
        s.sendall(b'97')
    if GPIO.input(16) == GPIO.HIGH:
            s.sendall(b'16')
    else:
        s.sendall(b'96')
    if GPIO.input(18) == GPIO.HIGH:
            s.sendall(b'18')
    else:
        s.sendall(b'95')
    if GPIO.input(19) == GPIO.HIGH:
            s.sendall(b'19')
    else:
        s.sendall(b'94')
    if GPIO.input(21) == GPIO.HIGH:
            s.sendall(b'21')
    else:
        s.sendall(b'93')
    if GPIO.input(22) == GPIO.HIGH:
            s.sendall(b'22')
    else:
        s.sendall(b'92')
s.close()