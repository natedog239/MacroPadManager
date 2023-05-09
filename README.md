# MacroPadManager
 Python application to manage 3x3 Pico MacroPad 
 
## Application:

Reference \lib\adafruit_hid\keycode.py for keycode call mappings. 

Testing a executable application that can manage the Macropad key combinations. 

Current limitations:
1. Path to the CircuitPython device is hard coded as device drive letter. 
2. Updating key combos is text input that is separated by commas, not the actual keystroke. 
3. Multi line key combinations for a single button are not supported. 

v.3 Application is able to update the code.py file and refresh with the applied change. 

![v3 applicaiton build](/Photos/Macro_Program.jpg)
