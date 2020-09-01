<h3>Electrolyser (EL 2.1) example control scripts</h3>

This repository contains example scripts that allow to control <a href="https://www.enapter.com/electrolyser">Electrolyser.</a>

More technical details on the EL 2.1 electrolyser including network requirements, firmware and how to set up your electrolyser in the <a href="https://handbook.enapter.com/electrolyser/el21/el21.html">Enapter Handbook</a>.
=====
Example scripts need pymodbus package to be installed. You can install it running:<br>
<code>#pip3 install pymodbus</code> 

<b>el21checkmodbus.py</b> - this script simply checks if Modbus connection is available with connected device.<br> 
EL2.1 IP-address is needed to be passed as an argument to this script when you run it. E.g.:<br> 
<code>#python3 el21checkmodbus.py 192.168.1.2</code>

<b>el21errors.py</b> - this script shows current EL2.1 errors (if any). 
You can find a list of errors codes <a href="https://handbook.enapter.com/electrolyser/el21/el21_firmware/1.2.0/modbus_tcp_communication_interface.html#error-codes">here</a>.<br>
EL2.1 IP-address is needed to be passed as an argument to this script when you run it. E.g.:<br>
<code>#python3 el21errors.py 192.168.1.2</code>

<b>ieee754read.py</b> - this script reads Float32 value from a register. You can find more info about input registers <a href="https://handbook.enapter.com/electrolyser/el21/el21_firmware/1.2.0/modbus_tcp_communication_interface.html#input-registers-read-only">here</a>.<br>
EL2.1 IP-address and register number (you can use 1006 for testing purposes) are needed to be passed as an arguments to this script when you run it. E.g.:<br> 
<code>#python3 el21errors.py 192.168.1.2 1006</code>

<b>el21reboot.py</b> - this script writes a value ‘1’ to register 4 (Reboot). You can find more info about holding registers <a href="https://handbook.enapter.com/electrolyser/el21/el21_firmware/1.2.0/modbus_tcp_communication_interface.html#holding-registers-read-write">here</a>.<br>
EL2.1 IP-address is needed to be passed as an arguments to this script when you run it. E.g.:<br>
<code>#python3 el21reboot.py 192.168.1.2</code>
