import paramiko

user_name = "farid"
passwd = "123456"
ip = "192.168.13.51"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username=user_name,password=passwd)
cmd="cat /scripts/teste3"
stdin, stdout, stderr=ssh_client.exec_command(cmd)
stdout=stdout.readlines()

print (stdout)