# Import Flask class from flask module
from flask import Flask, request
from operations import add, sub, mult, div

# Instantiate a Flask object and store it in a variable called app
app = Flask(__name__)


@app.route("/add")
def add_route():
    a, b = int(request.args["a"]), int(request.args["b"])
    return str(add(a, b))


@app.route("/sub")
def sub_route():
    a, b = int(request.args["a"]), int(request.args["b"])
    return str(sub(a, b))


@app.route("/mult")
def mult_route():
    a, b = int(request.args["a"]), int(request.args["b"])
    return str(mult(a, b))


@app.route("/div")
def div_route():
    a, b = int(request.args["a"]), int(request.args["b"])
    return str(div(a, b))


# View function dealing with all the math operations in one place
@app.route("/math/<operation>")
def math_route(operation):
    a, b = int(request.args["a"]), int(request.args["b"])
    if operation == "add":
        return str(add(a, b))
    elif operation == "sub":
        return str(sub(a, b))
    elif operation == "mult":
        return str(mult(a, b))
    elif operation == "div":
        return str(div(a, b))
    else:
        return "Invalid operation. Please try again."
