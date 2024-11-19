from flask import Flask, render_template
from dotenv import load_dotenv
from database.db import db,init_db
from models import ingrediente,producto,base,complemento
from controllers.controller_ingrediente import ingrediente_bp
from controllers.controller_producto import producto_bp

import os

load_dotenv()
app = Flask(__name__, template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY-TRACK-MODIFICATIONS"] = False

db.init_app(app)
init_db(app)

app.register_blueprint(producto_bp)
app.register_blueprint(ingrediente_bp)


@app.route("/")
def index():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(debug=True)