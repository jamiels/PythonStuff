from flask import Flask
from flask import request
from flask import render_template
import mysql.connector as mc

app = Flask(__name__)

# Windows: $env:FLASK_DEBUG=1
# Mac: export FLASK_DEBUG=1
'''
create table products (
	product_id int not null,
    description varchar(20)
)

create table orders (
	orders_id int not null auto_increment,
    quantity int,
    product_id int,
    primary key (orders_id)
)

insert into products
values (1,'M&M'),(2,'KitKat'),(3,'Jelly Beans')

'''
@app.route('/logout')
def logout():
    return "Bye"

@app.route('/viewOrders')
def view_orders():
    connection = get_connection()
    sql = "select * from orders,products where orders.product_id = products.product_id"
    result = connection.cmd_query(sql)
    rows = connection.get_rows()
    connection.close()
    return render_template('candystore_orders.html',orders=rows[0])

@app.route('/process',methods=['POST'])
def process_order():
    qty = request.form['qty']
    product = request.form['itemOrdered']
    connection = get_connection()
    sql = 'insert into orders (quantity,product_id) values ('+qty+','+product+')'
    # i.e insert into orders (quantity, product_id) values (8000,2)
    result = connection.cmd_query(sql)
    connection.commit()
    connection.close()
    return "Order processed"

@app.route('/')
def candystore_main():
    products = get_products()
    return render_template('main.html',stuff=products,more_stuff=5)

@app.route("/hello")
def hello():
    return render_template('index.html')

@app.route('/orders/<orderid>')
def show_orders(orderid=None):
    calc = int(orderid) * 5
    stuff = "<b>Hello " + str(calc) +"</b>"
    return stuff

@app.route('/query')
def query():
    name = request.args.get('name')
    color = request.args.get('color')
    combined = name + ' ' + color
    return combined

def get_connection():
    return mc.connect(user='root',
    password='jamiel',
    host='127.0.0.1',
    database='candystore',
    auth_plugin='mysql_native_password')

def get_products():
    connection = get_connection()
    result = connection.cmd_query("select * from products")
    rows = connection.get_rows()
    connection.close()
    return rows[0]
