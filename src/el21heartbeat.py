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
import time
import struct
from pymodbus.client.sync import ModbusTcpClient

ip = sys.argv[1]
port = 502
timeout = sys.argv[2]

device = ModbusTcpClient(ip, port)

h = device.read_holding_registers(4600, 1, unit=1)
print('Current Heartbeat Timeout value:', h.registers[0])
configuration_begin = device.write_register(4000, 1, unit=1) # Begin writing configuration
heartbeat_timeout = device.write_register(4600, int(timeout), unit=1) # Write HeartBeat ModBus Timeout. 0 - turned off
configuration_commit = device.write_register(4001, 1, unit=1) # Commit changes
print('Heartbeat Timeout set to', str(timeout))
