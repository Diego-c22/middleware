from flask import Flask, app
from users.resources import users_v1

app = Flask(__name__)
app.register_blueprint(users_v1)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
