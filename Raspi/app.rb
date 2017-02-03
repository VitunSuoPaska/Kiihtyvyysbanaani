require "mysql"
require "serialport"

port = "fill"
baudRate = 9600
dataBits = 8
stopBits = 1
parity = SerialPort::NONE

serial = SerialPort.new(port, baudRate, dataBits, stopBits, parity)

con = Mysql.new 'sql11.freemysqlhosting.net', 'sql11155651', 'uwh45VlDHi', 'sql11155651'

while true do
	while (msg = serial.gets) do
		#puts msg
		#con.query("INSERT INTO Acceleration(gyro_xyz) VALUES(?)")
		pst = con.prepare "INSERT INTO Acceleration(gyro_xyz) VALUES(?)"
		pst.execute msg
	end
	
end

serial.close