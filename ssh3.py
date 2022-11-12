import paramiko

hostname = "192.168.13.50"
username = "farid"
password = "123456"

commands = [
    "touch /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini "
    "echo '[GERAL]' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini",
    "echo 'UTILIZA_SFTP=S' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini",
    "echo '[RETAGUARDA]' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste.ini",
    "echo 'ENDERECOIP=082085065079083079069087077080065084' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini",
    "echo 'PORTA=082084065080' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste.ini",
    "echo 'SERVIDOR=032036071034090039044080087082075082080062036062011008020009077017018097016079028019002002031004077002028012' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini",
    "echo 'USUARIO=054062048036087034074039060054058' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini",
    "echo 'SENHA=044087066043053080070084051036056051045081066087084051' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini",
    "echo 'ALIASTNSNAMES=' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini",
    "echo 'USASID=N' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/teste2.ini"
    ]

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

    # execute the commands
for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)