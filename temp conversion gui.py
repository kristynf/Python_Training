import easygui
print "This program converts a temperature from Fahrenheit to Celsius"
fahrenheit = float(easygui.enterbox('What is the temperature in Fahrenheit?'))
celsius = (fahrenheit - 32) * 5.0 / 9
easygui.msgbox("The temperature in Celsius is", + celsius)
