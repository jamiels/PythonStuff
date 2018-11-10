from flask import Flask
#import mysql.connector as mc
#print(mc.__version__)
app = Flask(__name__)

@app.route('/')
def webapp1():
    connection = mc.connect(user='root',
    password='jamiel',
    host='127.0.0.1',
    database='myfirstdb',
    auth_plugin='mysql_native_password')
    app = Flask(__name__)
    result = connection.cmd_query('select * from orders')
    rows = list(connection.get_rows())
    connection.close()
    return str(rows)

@app.route('/address')
def get_address():
    return '''
    <html>
  <head>
    <title>My first page</title>
  </head>
  <body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <table border=1>
      <tr>
        <th>symbol</th>
        <th>qty</th>
      </tr>
        
      <tr>
        <td>hello</td>
        <td>hello2</td>
      </tr>
      <tr>
        <td>bye</td>
        <td>bye2</td>
      </tr>
    </table>
  </body>
</html>
    '''