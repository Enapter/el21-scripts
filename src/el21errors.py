#!/usr/bin/env python3
# Copyright 2020 Enapter, Alexander Shalin <ashalin@enapter.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from pymodbus.client.sync import *

ip = sys.argv[1]
PORT = 502
REGISTER = 832  # Error Events Array represented by Error Codes. First Uint16 contains total quantity of Error Events

device = ModbusTcpClient(ip, PORT)
firmware = device.read_input_registers(REGISTER, 32, unit=1)  # unit here is an address of the slave device
numberoferrors = firmware.registers[0]
print('Number of errors:', numberoferrors)
for e in range(1, numberoferrors + 1):
    print(hex(firmware.registers[e]))
