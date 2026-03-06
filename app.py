from flask import Flask, render_template, abort ,jsonify, request, redirect
from werkzeug.security import check_password_hash

from products import products as products_list
from flask_mail import Mail, Message

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text

from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager,get_jwt

# from model import User
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "**1234567ray"
app.config["JWT_TOKEN_EXPIRES"] = timedelta(minutes=30)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
import model

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sinthavry@gmail.com'
app.config['MAIL_PASSWORD'] = 'acds kmjr iopy xxmf'  # App password
app.config['MAIL_DEFAULT_SENDER'] = 'sinthavry@gmail.com'

mail = Mail(app)

REVOKED_JTIS =set()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_data):
    return jwt_data("jti") in REVOKED_JTIS

@app.post("/login")
def login():
    username = request.json.get("username", None)
    new_password = request.json.get("password", None)
    sql_str = text("select * from user where username = :username")
    pre_sql = db.session.execute(sql_str, {"username": username}).fetchone()

    if not pre_sql:
        return jsonify({"msg": "Incorrect username or password"}), 401

    # assert False , pre_sql
    user_id = str(pre_sql[0])
    old_password = pre_sql[3]
    # assert False, check_password_hash(old_password, new_password)
    # assert False , f"{user_id}-{old_password}"

    if check_password_hash(old_password, new_password):
        access_token = create_access_token(identity=user_id)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Incorrect username or password2"}), 401


@app.post("/logout")
@jwt_required()  # revoke current access token
def logout():
    jti = get_jwt()["jti"]
    REVOKED_JTIS.add(jti)
    return jsonify(msg="Access token revoked")


@app.post("/me")
@jwt_required()
def me():
    user = get_jwt_identity()
    return jsonify(user=user)


import routes

if __name__ == '__main__':
    app.run()
