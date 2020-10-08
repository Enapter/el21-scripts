<h3>Electrolyser (EL 2.1) control scripts examples</h3>

This repository contains example scripts that allow to control <a href="https://www.enapter.com/electrolyser">Electrolyser (EL 2.1).</a>

More technical details on the EL 2.1 electrolyser including network requirements, firmware and how to set up your electrolyser in the <a href="https://handbook.enapter.com/electrolyser/el21/el21.html">Enapter Handbook</a>.

---

Example scripts need pymodbus package to be installed. You can install it running:  
    #pip3 install pymodbus

**el21checkmodbus.py** - this script simply checks if Modbus connection is available with connected device.  
EL2.1 IP address is needed to be passed as an argument to this script when you run it. E.g.:  
    #python3 el21checkmodbus.py 192.168.1.2

**el21maintenance.py** - this script guides user through EL 2.1 maintenance process when electrolyte refilling is performed.  
EL2.1 IP address is needed to be passed as an argument to this script when you run it. E.g.:  
<code>#python3 el21maintenance.py 192.168.1.2</code>

**el21errors.py** - this script shows current EL2.1 errors (if any). 
You can find a list of errors codes <a href="https://handbook.enapter.com/electrolyser/el21/el21_firmware/1.2.0/modbus_tcp_communication_interface.html#error-codes">here</a>.  
EL2.1 IP address is needed to be passed as an argument to this script when you run it. E.g.:  
<code>#python3 el21errors.py 192.168.1.2</code>

**ieee754read.py** - this script reads Float32 value from a register. You can find more info about input registers <a href="https://handbook.enapter.com/electrolyser/el21/el21_firmware/1.2.0/modbus_tcp_communication_interface.html#input-registers-read-only">here</a>.  
EL2.1 IP address and register number (you can use 1006 for testing purposes) are needed to be passed as an arguments to this script when you run it. E.g.:  
<code>#python3 el21errors.py 192.168.1.2 1006</code>

**el21reboot.py** - this script writes a value ‘1’ to register 4 (Reboot). You can find more info about holding registers <a href="https://handbook.enapter.com/electrolyser/el21/el21_firmware/1.2.0/modbus_tcp_communication_interface.html#holding-registers-read-write">here</a>.  
EL2.1 IP address is needed to be passed as an arguments to this script when you run it. E.g.:  
<code>#python3 el21reboot.py 192.168.1.2</code>

**el21heartbeat.py** - this script sets HeartBeat ModBus Timeout. You can find more info about input registers <a href="https://handbook.enapter.com/electrolyser/el21/el21_firmware/1.2.0/modbus_tcp_communication_interface.html#input-registers-read-only">here</a>.  
EL2.1 IP address and timeout (in seconds, 0 - turn HeartBeat ModBus off) are needed to be passed as an arguments to this script when you run it. E.g.:  
<code>#python3 el21heartbeat.py 192.168.1.2 30</code>
