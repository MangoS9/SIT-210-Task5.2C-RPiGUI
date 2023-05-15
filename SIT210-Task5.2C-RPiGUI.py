
import RPi.GPIO as GPIO
import tkinter as tk
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_num = {'Button 3':3,
	'Button 5':5,
	'Button 7':7,}

GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

def button_press(n):
	for btn,pin in pin_num.items():
		if btn == n:
			GPIO.output(pin,GPIO.HIGH) #Target high
		else:
			GPIO.output(pin,GPIO.LOW) #everything else low

root = tk.Tk()
root.title("Light up")
root.geometry ('300x300')

buttons = []
for btn_name,pin in pin_num.items():
	button = tk.Button(root, text=btn_name,width = 10,height = 2,command=lambda btn=btn_name:button_press(btn))
	button.pack(pady=5)
	buttons.append(button)

exit_btn = tk.Button(root,text='Exit',width=10,height=2,command=root.quit)
exit_btn.pack(pady=35)
buttons.append(exit_btn)

root.mainloop()

GPIO.cleanup()