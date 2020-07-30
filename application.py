from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP!</h1>\nMBA! o/ \n Seja bem vindo ao bem primeiro deploy de aplicação Python!"

if __name__ == '__main__':
    application.run()
