# Python-API
Fibonacci sequence - starting at 1 rather than 0
 
First install python version 3 or higher
pip install Flask

create your .py file in Atom
from flask import Flask
app = Flask(__name__)

write the code

test the code to see if it works:
in the browser, first i used: http://127.0.0.1:5000/?n=h
the output was: Please use a number as the 'n' argument

then, in the browser i used: http://127.0.0.1:5000/?n=8
the output was 21

next input was: 1
output was 1

finally using input 0
Output is 0

(negative numbers output 0) and do not cause error
