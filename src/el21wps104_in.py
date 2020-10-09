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
from pymodbus.client.sync import ModbusTcpClient

ip = sys.argv[1]
PORT = 502
REGISTER = 7003  # 1 = Water is present

device = ModbusTcpClient(ip, PORT)
firmware = device.read_input_registers(REGISTER, 1, unit=1)

wps104_in = int(firmware.registers[0])

print('Register', register, ':', wps104_in)

if wps104_in == 1:
    print('Water is present')
elif wps104_in == 0:
    print('No water')
else:
    print('No data')
