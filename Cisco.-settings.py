import netmiko
from netmiko import ConnectHandler
sshCLI = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.56.101',
    port = '22',
    username = 'cisco',
    password = 'cisco123!'
)
sshCLI.enable()
output = sshCLI.send_command('show ip interface brief ')
print(r'Show ip int breef: {}'.format(output))
config_command = [
    'int loopbakc 1',
    'ip add 1.1.1.1 255.255.255.0',
    'description This int was config with netmiko'
]
output = sshCLI.send_config_set(config_command)
print(r'config int lo1: \n{}\n'.format(output))
config_command_2 = [
    'int loopbakc 2',
    'ip add 2.2.2.1 255.255.255.0',
    'description This int was config with netmiko lo2'
]
output = sshCLI.send_config_set('show int description')
print(r'config int lo2: \n{}\n'.format(output))