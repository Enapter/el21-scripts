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
import datetime
from pymodbus.client.sync import ModbusTcpClient


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ip = sys.argv[1]
PORT = 502
register = 6  # Maintenance Mode. 1 = Enable.

device = ModbusTcpClient(ip, PORT)
response = device.read_holding_registers(register, 1, unit=1)

maintenance = bool(response.registers[0])

level = device.read_input_registers(7000, 4, unit=1)
LSHH102A_in = bool(level.registers[1])
if LSHH102A_in:
    print('Very High Electrolyte Level\nMaintenance mode can\'t be turned on. Drain electrolyte, reset your EL 2.1 and run this script again.')
    sys.exit()

mlf = 0  # Medium Level Flag
llf = 0  # Low Level Flag
zlf = 0  # Zero Level Flag


def electrolyte_level(mlf, llf, zlf):
    level = device.read_input_registers(7000, 4, unit=1)
    LSH102B_in = bool(level.registers[0])
    LSHH102A_in = bool(level.registers[1])
    LSL102D_in = bool(level.registers[2])
    LSM102C_in = bool(level.registers[3])
    if LSHH102A_in:
        print('Very High Electrolyte Level\nMaintenance mode can\'t be turned on. Drain electrolyte, reset your EL 2.1 and run this script again.')
        sys.exit()
    if LSH102B_in:
        t = datetime.datetime.now()
        input('[' + str(t) + '] High Electrolyte Level\nPress Enter to finish')
        res = device.write_register(register, 0, unit=1)
        if 'Exception' in str(res):
            print('Maintenance mode can\'t be turned off. Please contact Enapter Support')
        else:
            print(f'{BColors.WARNING}Maintenance mode turned off{BColors.ENDC}\n{BColors.OKGREEN}Refilling process completed{BColors.ENDC}')
        sys.exit()
    elif LSM102C_in:
        if mlf == 0:
            t = datetime.datetime.now()
            print('[' + str(t) + '] Medium Electrolyte Level - fill more electrolyte')
            mlf = 1
    elif LSL102D_in:
        if llf == 0:
            t = datetime.datetime.now()
            print('[' + str(t) + '] Low Electrolyte Level - fill more electrolyte')
            llf = 1
    else:
        if zlf == 0:
            print(f'{BColors.OKBLUE}Start filling electrolyte{BColors.ENDC}')
            zlf = 1
    return [mlf, llf, zlf]


if maintenance is False:
    input(f'{BColors.FAIL}Maintenance mode will be turned on for refilling process.{BColors.ENDC}\nPress Ctrl+C to stop this script or Enter to proceed.')
    res = device.write_register(register, 1, unit=1)
    if 'Exception' in str(res):
        print('Maintenance mode can\'t be turned on. Please contact Enapter Support')
        electrolyte_level()
    else:
        maintenance = True

if maintenance is True:
    print(f'{BColors.WARNING}Maintenance mode turned on{BColors.ENDC}\n{BColors.OKBLUE}Start draining electrolyte{BColors.ENDC}')
    LSH102B_in = bool(level.registers[0])
    LSL102D_in = bool(level.registers[2])
    LSM102C_in = bool(level.registers[3])
    dmf = 0  # Drain Medium Level
    dlf = 0  # Drain Low Level
    while True:
        level = device.read_input_registers(7000, 4, unit=1)
        LSH102B_in = bool(level.registers[0])
        LSL102D_in = bool(level.registers[2])
        LSM102C_in = bool(level.registers[3])
        if LSL102D_in is False:
            break
        else:
            if LSH102B_in is False:
                if dmf == 0:
                    t = datetime.datetime.now()
                    print('[' + str(t) + '] Medium Electrolyte Level - drain more electrolyte')
                    dmf = 1
            if LSM102C_in is False:
                if dlf == 0:
                    t = datetime.datetime.now()
                    print('[' + str(t) + '] Low Electrolyte Level - drain more electrolyte')
                    dlf = 1
    while True:
        flag = electrolyte_level(mlf, llf, zlf)
        mlf = flag[0]
        llf = flag[1]
        zlf = flag[2]
