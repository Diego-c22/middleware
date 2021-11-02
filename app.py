from flask import Flask, app
from users.resources import users_v1
from store.item_resources import items_v1
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(users_v1)
app.register_blueprint(items_v1)

if __name__ == "__main__":
    #app.run(debug=True, port=8000, host='0.0.0.0')
    app.run(debug=True)
