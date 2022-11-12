import paramiko



hostname = "192.168.10.20"
username = "farid"
password = "123456"

commands = [

    'echo "PATH=$ORACLE_HOME/bin:$PATH:/opt/oracle/product/18c/dbhomeXE/bin" >> ~/.bashrc'
    # "cat /home/farid/sql.sh",
    # "echo 'export ORACLE_HOME=/opt/oracle/product/18c/dbhomeXE' >> /home/farid/sql.sh",
    # "echo 'export ORACLE_SID=XE' >> /home/farid/sql.sh",
    # "echo 'export PATH=$ORACLE_HOME/bin:$PATH' >> /home/farid/sql.sh",
    # "chmod 777 /home/farid/sql.sh",
    # "sh /home/farid/sql.sh",
    # "sqlplus",
    # #"/opt/oracle/product/18c/dbhomeXE/bin/sqlplus",
    # "CAIXA/CAIXA@localhost:1521/XEPDB1",
    # "drop database link DBLSERVIDOR;",
    # "commit;",
    # "exit",
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