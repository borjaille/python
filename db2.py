import cx_Oracle

dsn = cx_Oracle.makedsn(
    '192.168.10.20', 
    '1521', 
    service_name='XEPDB1'
)
conn = cx_Oracle.connect(
    user='CAIXA', 
    password='CAIXA', 
    dsn=dsn
)
c = conn.cursor()
c.execute('drop database link DBLSERVIDOR')
c.execute('commit')
#for row in c: print(row)
conn.close()