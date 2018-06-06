#! /usr/bin/python3

"""
Author: liulei

Version: 1.0

Main Function:
  PC control Android
    The script intercepts the pc's keyboard input and sends the corresponding 
  key value  to the android device using ADB.

Extra Support: Python、ADB
"""

import os
import sys
import tty
import termios
import time


def connect_device():
  ip = input('please input android device ip: ')
  if ip=='':
    print('emppty ip')
    exit()

  os.system('adb disconnect')
  os.system('adb connect ' + ip)
  os.system('adb root')
  os.system('adb connect ' + ip)
  os.system('adb remount')


def process_input():
  print('--------------------------------------------------------')
  print('8(Up),2(Down),4(Left),6(Right),5(Center),1(Back),3(Home)')
  print("'ctrl+d' or 'q' to exist")
  print('--------------------------------------------------------')
  
  while True:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(fd)
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ord(ch) == 0x3 or ch == 'q':
      print('\n---> stop send key <---')
      break
    else:
      move(ch)


def move(ch):
  asc = ord(ch)
  # print('input key=' + str(ch) + ' ascii=' + str(asc))
  if ch == '8' or asc == 0x41:
    input_event(19)
  elif ch == '2' or asc == 0x42:
    input_event(20)
  elif ch == '4' or asc == 0x44:
    input_event(21)
  elif ch == '6' or asc == 0x43:
    input_event(22)
  elif ch == '5':
    input_event(23)
  elif ch == '1':
    input_event(4)
  elif ch == '3':
    input_event(3)


def input_event(code):
  os.system('adb shell input keyevent ' + str(code))


if __name__ == '__main__':
  connect_device()
  process_input()
