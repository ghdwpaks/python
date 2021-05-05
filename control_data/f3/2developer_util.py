# -*- coding: utf-8 -*-
print("1\tHello\t1")
print("12345678Hello5678")
print("1\t안녕하세요\t1")
print("12345678안녕하세요1234567")
print("안녕하세\t1")

if 'a 'in "apple" :
    print(True)

word = "7904ghdwpaks"

if word.encode().isalpha():
    print("It is an alphabet")
elif word.encode().isdigit() :
    print("It is a number")

STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12
 
FOREGROUND_BLACK     = 0x00
FOREGROUND_BLUE      = 0x01 # text color contains blue.
FOREGROUND_GREEN     = 0x02 # text color contains green.
FOREGROUND_RED       = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE      = 0x10 # background color contains blue.
BACKGROUND_GREEN     = 0x20 # background color contains green.
BACKGROUND_RED       = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.
 
import ctypes
 
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool
 
for i in range(0, 16):
    set_color(i)
    print("Hello, world!")
 
set_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

print("\033[34mghdwpaks\033[0m")
