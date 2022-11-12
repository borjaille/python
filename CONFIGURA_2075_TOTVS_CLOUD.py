import paramiko

erroCaixas = []

                    # ////////////////// DICIONARIO COM IP E NÚMERO DOS CAIXAS /////////////////////////////

caixasDiscionary = [{"ip": "172.16.1.91", "numero": "1001"},{"ip": "172.16.2.92", "numero": "2002"}
]

for caixa in caixasDiscionary:
    print (caixa['numero'])
    hostname = caixa['ip']
    username = "USERNAME_LINUX"
    password = "LINUX_PASSWORD"

    commands = [
                            # ////////////////// MATA ROTINA 2075 ABERTA /////////////////////////////
        "pkill PCAUX2075.EXE",
        "pkill PCAUX2075.exe",
        "pkill PCAUX2075.BIN",
        "pkill PCAUX2075.bin",
        "pkill PCSIS2075.BIN",
        "pkill PCSIS2075.bin",
        "pkill PCSIS2075.exe",
        "pkill PCSIS2075.EXE",
                    # ////////////////// DELETA ARQUIVO PCAUX2075.INI /////////////////////////////
        "rm -rf /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
                    # ////////////////// CRIA TEXTO BASE DENTRO DA 2075.INI /////////////////////////////
        "touch /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",               
        "echo '[GERAL]' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        f"echo '[NUMCAIXA={caixa['numero']}]' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'CONEXAODIRETA=S' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'ORACLE_PDB=S' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'NLS_CHARACTERSET_ATUALIZADO=S' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'USACONVQUANTPRODPESADO=S' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
                    # ////////////////// CRIA INFORMAÇÕES DO BANCO NOVO DENTRO DA 2075.INI  /////////////////////////////
        "echo 'UTILIZA_SFTP=S' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo '[RETAGUARDA]' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini", 
        "echo 'ENDERECOIP=ENDEREÇO IP CRIPTOGRAFADO' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'PORTA=PORTA CRIPTOGRAFADA' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'SERVIDOR=SERVIDOR CRIPTOGRAFADO' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'USUARIO=USUARIO CRIPTOGRAFADO' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'SENHA=SENHA CRIPTOGRAFADA' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'ALIASTNSNAMES=' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'USASID=N' >> /home/user/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini"
        "reboot"
        ]
                    # ////////////////// INICIALIZA SSH COM OS CAIXAS /////////////////////////////
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
        for command in commands:
            print("="*50, command, "="*50)
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read().decode())
            err = stderr.read().decode()
            if err:
                print(err)
    except:
        erroCaixas.append(caixa['numero'])
        print("[!] Cannot connect to the SSH Server")
        pass


print(erroCaixas)

