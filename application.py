from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP!</h1>\nMBA! o/ V2"

if __name__ == '__main__':
    application.run()
