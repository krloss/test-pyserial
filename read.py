from sys import argv
from serial import Serial

# Main
# Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
# timeout = integer in seconds
serial = Serial(port=argv[1])
text = serial.read(int(argv[2])) if 3 == len(argv) else serial.readline()

serial.close()
print '>>> %s!\n' % (text)
