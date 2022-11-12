import subprocess

"""
Example of running a sqlplus script from Python.
Works with Python 3 and 2.
"""

def run_sqlplus(sqlplus_script):

    """
    Run a sql command or group of commands against
    a database using sqlplus.
    """

    p = subprocess.Popen(['sqlplus','/nolog'],stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,stderr) = p.communicate(sqlplus_script.encode('utf-8'))
    stdout_lines = stdout.decode('utf-8').split("\n")

    return stdout_lines

sqlplus_script=
connect CAIXA/CAIXA@192.168.10.20:1521/XEPDB1
drop database link DBLSERVIDOR;
commit;
exit

sqlplus_output = run_sqlplus(sqlplus_script)

for line in sqlplus_output:
    print(line)