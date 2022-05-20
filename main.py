from netmiko import ConnectHandler

f = open('/home/moakod/BackupConfigs/routers.txt')
IP_Addresses = f.read().splitlines()

for IP in IP_Addresses:
    Device = {
        'device_type': 'cisco_ios',
        'host': IP,
        'username': 'moakod',
        'password': 'cisco'
    }

    ssh = ConnectHandler(**Device)
    print('Backing up device ' + str(IP))
    ssh.send_command('terminal length 0')
    run_config = ssh.send_command('show run')
    print(run_config)

    f = open('/home/backups/Device ' + str(IP), 'w')
    f.write(run_config)
    f.close()

