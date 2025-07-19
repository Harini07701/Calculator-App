from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# API to calculate expression
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression")

    try:
        # Add scientific functions
        result = eval(expression, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi
        })
        return jsonify({"result": result})
    except:
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run(debug=True)
