#!/usr/bin/env python3
# Copyright 2020 Enapter, Alexander Shalin <ashalin@enapter.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distribut$
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express o$
# See the License for the specific language governing permissions and limitatio$

import sys
import struct
from pymodbus.client.sync import ModbusTcpClient

ip = sys.argv[1]
port = 502
register = 832 # Error Events Array represented by Error Codes. First Uint16 contains total quantity of Error Events

device = ModbusTcpClient(ip, port)
firmware = device.read_input_registers(register, 32, unit=1) # unit here is an address of the slave device
numberoferrors = firmware.registers[0]
print('Number of errors:', numberoferrors)
for e in range(1, numberoferrors+1) :
	print(hex(firmware.registers[e]))
