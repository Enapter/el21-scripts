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
timeout = sys.argv[2]

device = ModbusTcpClient(ip, PORT)

h = device.read_holding_registers(4600, 2, unit=1)
current_timeout = h.registers[1] | (h.registers[0] << 16)
print('Current Heartbeat Timeout value:', current_timeout)
configuration_begin = device.write_register(4000, 1, unit=1)  # Start writing configuration
# Writing Uint16 to 4601 instead if Uint32 to 4600
heartbeat_timeout = device.write_register(4601, int(timeout), unit=1)  # 0 - turned off
configuration_commit = device.write_register(4001, 1, unit=1)  # Commit changes
print('Heartbeat Timeout set to', str(timeout))
