from flask import Flask, request
app = Flask(__name__)

def fibo(n: int): #Calculate the fibonacci numbers
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

@app.route('/') #the actual route
def send_fibo(): #tell user input must be number
    try:
        return str(fibo(int(request.args['n'])))
    except ValueError:
        return "Please use a number as the 'n' argument"
if __name__== "__main__":
    app.run(debug=True)
