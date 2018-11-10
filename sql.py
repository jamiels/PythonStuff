import mysql.connector as mc
print(mc.__version__)

connection = mc.connect(user='root',
password='jamiel',
host='127.0.0.1',
database='myfirstdb',
auth_plugin='mysql_native_password')

result = connection.cmd_query('select * from orders')
rows = list(connection.get_rows())
for r in rows[0]:
    print(r)

connection.close()