<<<<<<< HEAD
from flask import Flask
from routes import bp as routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask
from routes.routes import bp as routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 78d9105157d3f4a6edade77023ead9244fc7fea6
