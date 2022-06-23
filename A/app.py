from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('')
#decorador de la ruta SALUDO
@app.route('/',methods = ['POST','GET'])
def saludo():   #primer metodo que se ejecuta
    if request.method == 'POST':
        if(request.form['email'] and request.form['password']):
            datosForm = request.form
            return render_template('index.html')
        else:
            return render_template('mensaje.html')
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug= True)