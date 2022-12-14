from sqlite3 import DateFromTicks
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout/', methods=['POST'])         
def checkout():
    nombre=request.form['first_name']
    apellido=request.form['last_name']
    nro_tarjeta=request.form['student_id']
    strawberry=int(request.form['strawberry'])
    raspberry=int(request.form['raspberry'])
    apple=int(request.form['apple'])

    frutas=str(strawberry+raspberry+apple)
    print("Cobrando a "+nombre+" por "+frutas+ " frutas")
    return render_template("checkout.html", nombre=nombre, apellido=apellido,nro_tarjeta=nro_tarjeta,apple=apple, raspberry=raspberry, strawberry=strawberry)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    