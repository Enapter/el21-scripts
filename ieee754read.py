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
#register = 1006 # Stack Total H2 Production (NL)
register = int(sys.argv[2])

device = ModbusTcpClient(ip, port)
firmware = device.read_input_registers(register, 2, unit=1) # unit here is an address of the slave device
ieee754register = struct.pack("BBBB", firmware.registers[0] >> 8, firmware.registers[0] & 0xff, firmware.registers[1] >> 8, firmware.registers[1] & 0xff)
ieee754value = struct.unpack(">f", ieee754register)

print('Reading register:',register)
print('Response (hex):', (hex(firmware.registers[0]) + hex(firmware.registers[1])).replace('0x', ''))
print('Value: ', str(ieee754value).replace('(', '').replace(')', '').replace(',', ''))
