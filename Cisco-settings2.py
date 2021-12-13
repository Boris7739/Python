
import netmiko
from netmiko import ConnectHandler

cisco_router_1 = {
    'device_type': 'cisco_ios',
    'host': '192.166.1.2',
    'port': '22',
    'username': 'cisco',
    'password': 'cisco123!',
    'SECRET': 'class'
}
sshCLI = ConnectHandler(**cisco_router_1)
sshCLI.enable()

config_command = [
    'conf t'
    'int GigabitEthernet 0/1',
    'ip add 192.166.1.1 255.255.255.0',
    'description LAN to PC_area',
    'ip nat inside',
    'no shutdown'
]
output = sshCLI.send_config_set(config_command)
print(r'config int gi0/1: \n{}\n'.format(output))
config_command_2 = [
    'conf t'
    'int GigabitEthernet 0/0',
    'ip add 192.168.0.1 255.255.255.0',
    'description LAN to net',
    'ip nat outside'
    'no shutdown'
]

output = sshCLI.send_config_set(config_command_2)
print(r'config int gi0/0: \n{}\n'.format(output))


config_command_3 = [
'ip access-list standard 7',
'permit 192.166.1.0 0.255.255.255',
'exit'
'ip nat inside source list 7 interface gi0/1 overload',
'ip route 0.0.0.0 0.0.0.0 192.168.0.2'
]
output = sshCLI.send_config_set(config_command_3)


output1 = sshCLI.send_command('show ip interface brief ')
print(r'Show ip int breef: {}'.format(output1))
sshCLI.exit_enable_mode()

sshCLI.disconnect()