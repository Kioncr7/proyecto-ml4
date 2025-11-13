# Importar
from flask import Flask, render_template, request, redirect
# Conexión de la biblioteca de bases de datos
from flask_sqlalchemy import SQLAlchemy
# 1. Configuración inicial de Flask
app = Flask(__name__)
# Conexión con SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creación de una base de datos
db = SQLAlchemy(app)

# 4. Definición de un modelo (estructura de la tabla)
class User(db.Model):
    # Clave primaria única y obligatoria
    id = db.Column(db.Integer, primary_key=True)
    # Columna de tipo string, de 20 caracteres de largo, única y obligatoria
    username = db.Column(db.String(20), unique=True, nullable=False)
    # Columna de tipo string, de 120 caracteres de largo, única y obligatoria
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Columna de tipo string, de 60 caracteres de largo, obligatoria
    password = db.Column(db.String(60), nullable=False)

    # Representación de la clase para facilitar la impresión
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# 5. Creación de la base de datos
def create_db():
    with app.app_context():
        # Crea las tablas definidas en los modelos (ej. la tabla 'user') en la base de datos.
        db.create_all()
        print("¡Base de datos y tablas creadas con éxito!")

if __name__ == '__main__':
    # Esta función se ejecuta una sola vez para crear el archivo 'site.db'
    create_db()
    # Para iniciar la aplicación Flask (opcional, solo para verificar)
    # app.run(debug=True)