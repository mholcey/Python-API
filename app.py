from flask import Flask, json, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n ==1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            b = c
            return b
print(fibonacci(9))

class Fibonacci(Resource):
    def get(self, number):
        return jsonify({'fibonacci': number})

api.add_resource(Fibonacci, '/fibonacci/<int:number>')

if __name__ == '__main__':
    app.run(debug = True)
