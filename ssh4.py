import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.13.50', username='farid', password='123456')

stdin, stdout, stderr = client.exec_command('ls -l')

for line in stdout:
    print (line.strip('\n'))

client.close()