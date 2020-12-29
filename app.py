from flask import Flask

app = Flask(__name__)

@app.route('/')
def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(21))
app.run(port=5000)
