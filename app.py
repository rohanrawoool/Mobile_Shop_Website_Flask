

from flask import Flask,render_template,url_for,request
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="localhost",user="root",password="",database="flaskp")
cursor = conn.cursor()


#Render to login page
@app.route('/')
def login_page():
    return render_template("login.html")


#Render to register page
@app.route('/reg')
def reg_page():
    return render_template("register.html")




@app.route('/login_validation',methods=['get','post'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""select * from info where email like '{}' and password like '{}' """.format(email,password))
    us = cursor.fetchall()
    if len(us)>0:
        return render_template("home.html")
    else:
        return render_template("login.html",info="Invalid User")



#Add New User/Register
@app.route('/add_user',methods=['post','get'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    cursor.execute("""insert into info(name,email,password) values('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return render_template("login.html")


@app.route("/go",methods=['get','post'])
def go_there():
    return render_template("buy.html")




#Contactus
@app.route('/contact',methods=['post','get'])
def contact():
    name= request.form.get('uname')
    email=request.form.get('uemail')
    adress=request.form.get('uadress')
    pincode=request.form.get('upincode')
    payment=request.form.get('upayment')
    cursor.execute("""insert into  orders(name,email,adress,pincode,mode) values('{}','{}','{}','{}','{}')""".format(name,email,adress,pincode,payment))
    conn.commit()
    return render_template("confirm.html")



@app.route("/get_to_shop",methods=["post","get"])
def go_shop():
    return render_template("home.html")


@app.route('/write')
def write_to():
    return render_template("home.html")

    



if __name__=="__main__":
    app.run()
