#require "mysql"
require "serialport"

port = "fill"
baudRate = 9600
dataBits = 8
stopBits = 1
parity = SerialPort::NONE

serial = SerialPort.new(port, baudRate, dataBits, stopBits, parity)

#con = Mysql.new 'localhost', 'user', 'pass', 'db'

while true do
	while (msg = serial.gets) do
		puts msg

	end
	
end

serial.close