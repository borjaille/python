import paramiko
import logging

erroCaixas = []

                    # ////////////////// MATRIZ COM IP E NÚMERO DOS CAIXAS /////////////////////////////

caixasDiscionary = [{"ip": "192.168.1.91", "numero": "6001"},{"ip": "192.168.1.22", "numero": "6002"},{"ip": "192.168.1.223", "numero": "6003"},{"ip": "192.168.1.24", "numero": "6004"},{"ip": "192.168.1.235", "numero": "6006"},{"ip": "192.168.1.27", "numero": "6007"},{"ip": "192.168.1.53", "numero": "6008"},{"ip": "192.168.1.21", "numero": "6009"},{"ip": "192.168.13.50", "numero": "6010"},{"ip": "192.168.1.25", "numero": "6011"},{"ip": "192.168.13.52", "numero": "6012"},{"ip": "192.168.13.53", "numero": "6013"},{"ip": "192.168.1.55", "numero": "6014"},{"ip": "192.168.13.51", "numero": "6015"},{"ip": "192.168.1.50", "numero": "6016"},{"ip": "192.168.1.51", "numero": "6017"},{"ip": "192.168.1.26", "numero": "6018"},{"ip": "192.168.7.60", "numero": "6101"},{"ip": "192.168.7.62", "numero": "6103"},{"ip": "192.168.7.63", "numero": "6104"},{"ip": "192.168.7.65", "numero": "6105"},{"ip": "192.168.7.66", "numero": "6106"},{"ip": "192.168.7.67", "numero": "6107"},{"ip": "192.168.7.69", "numero": "6108"},{"ip": "192.168.7.68", "numero": "6109"},{"ip": "192.168.7.61", "numero": "6110"},{"ip": "192.168.7.70", "numero": "6111"},{"ip": "192.168.10.58", "numero": "6201"},{"ip": "192.168.10.20", "numero": "6203"},{"ip": "192.168.10.55", "numero": "6204"},{"ip": "192.168.10.85", "numero": "6205"},{"ip": "192.168.10.57", "numero": "6206"},{"ip": "192.168.10.52", "numero": "6207"},{"ip": "192.168.10.59", "numero": "6208"},{"ip": "192.168.10.19", "numero": "6209"},{"ip": "192.168.10.20", "numero": "6210"},{"ip": "192.168.10.56", "numero": "6211"},{"ip": "192.168.10.65", "numero": "6212"},{"ip": "192.168.10.54", "numero": "6214"},{"ip": "192.168.4.51", "numero": "6301"},{"ip": "192.168.4.52", "numero": "6302"},{"ip": "192.168.4.53", "numero": "6303"},{"ip": "192.168.4.54", "numero": "6304"},{"ip": "192.168.4.55", "numero": "6305"},{"ip": "192.168.4.56", "numero": "6306"},{"ip": "192.168.4.57", "numero": "6307"},{"ip": "192.168.4.58", "numero": "6308"},{"ip": "192.168.4.59", "numero": "6309"},{"ip": "192.168.4.61", "numero": "6311"},{"ip": "192.168.4.62", "numero": "6312"},{"ip": "192.168.4.63", "numero": "6313"},{"ip": "192.168.4.64", "numero": "6314"},{"ip": "192.168.4.65", "numero": "6315"},{"ip": "192.168.4.66", "numero": "6316"},{"ip": "192.168.0.73", "numero": "6417"},{"ip": "192.168.11.83", "numero": "6418"},{"ip": "192.168.11.82", "numero": "6419"},{"ip": "192.168.11.70", "numero": "6420"},{"ip": "192.168.11.71", "numero": "6421"},{"ip": "192.168.11.72", "numero": "6422"},{"ip": "192.168.11.73", "numero": "6423"},{"ip": "192.168.11.74", "numero": "6424"},{"ip": "192.168.11.75", "numero": "6425"},{"ip": "192.168.11.76", "numero": "6426"},{"ip": "192.168.11.77", "numero": "6427"},{"ip": "192.168.11.78", "numero": "6428"},{"ip": "192.168.11.79", "numero": "6429"},{"ip": "192.168.11.80", "numero": "6430"},{"ip": "192.168.11.81", "numero": "6434"},{"ip": "192.168.11.84", "numero": "6701"},{"ip": "192.168.12.51", "numero": "6702"},{"ip": "192.168.12.52", "numero": "6703"},{"ip": "192.168.12.53", "numero": "6704"},{"ip": "192.168.12.54", "numero": "6705"},{"ip": "192.168.12.55", "numero": "6706"},{"ip": "192.168.12.56", "numero": "6707"},{"ip": "192.168.12.57", "numero": "6708"},{"ip": "192.168.12.58", "numero": "6709"},{"ip": "192.168.12.59", "numero": "6710"},{"ip": "192.168.12.60", "numero": "6711"},{"ip": "192.168.12.61", "numero": "6712"},{"ip": "192.168.12.62", "numero": "6713"},{"ip": "192.168.12.63", "numero": "6714"},{"ip": "192.168.12.64", "numero": "6715"},{"ip": "192.168.12.65", "numero": "6716"}
]

for caixa in caixasDiscionary:
    print (caixa['numero'])
    hostname = caixa['ip']
    username = "farid"
    password = "12"

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
        "rm -rf /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
                    # ////////////////// CRIA TEXTO BASE DENTRO DA 2075.INI /////////////////////////////
        "touch /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",               
        "echo '[GERAL]' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        f"echo '[NUMCAIXA={caixa['numero']}]' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'CONEXAODIRETA=S' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'ORACLE_PDB=S' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'NLS_CHARACTERSET_ATUALIZADO=S' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'USACONVQUANTPRODPESADO=S' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
                    # ////////////////// CRIA INFORMAÇÕES DO BANCO NOVO DENTRO DA 2075.INI  /////////////////////////////
        "echo 'UTILIZA_SFTP=S' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo '[RETAGUARDA]' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini", 
        "echo 'ENDERECOIP=082085065079083079069087077080065084' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'PORTA=082084065080' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'SERVIDOR=032036071034090039044080087082075082080062036062011008020009077017018097016079028019002002031004077002028012' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'USUARIO=054062048036087034074039060054058' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'SENHA=044087066043053080070084051036056051045081066087084051' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'ALIASTNSNAMES=' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini",
        "echo 'USASID=N' >> /home/farid/.wine/drive_c/Winthor/Prod/MOD-020/PCAUX2075.ini"
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

