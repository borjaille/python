import paramiko


p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
p.connect("192.168.13.50", port=22, username="farid", password="123456")
stdin, stdout, stderr = p.exec_command("nano /scripts/teste2.ini")
stdin, stdout, stderr = p.exec_command("aaa")
opt = stdout.readlines()
opt = "".join(opt)
print(opt)

