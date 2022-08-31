import serial

print("Handling ctrl-alt-delete")
char = 222
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=2)
ser.write(chr(char))
with open("~/Pi-Keylogger/test.txt", 'w+') as f:
    f.write("ctrl-alt-delete")
