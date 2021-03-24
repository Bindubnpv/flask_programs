from flask import Flask
from operations import Operator
app = Flask(__name__)
#obj = Operator(a,b)

@app.route('/<operator>/<int:a>/<int:b>')
def check(operator,a,b):
    obj = Operator(a,b)
    if operator == 'add':
        res = str(obj.add())
        return res
    if operator == 'sub':
        res = str(obj.sub())
        return res
    if operator == 'mul':
        res = str(obj.mul())
        return res
    if operator == 'divi':
        res = str(obj.divi())
        return res
    

'''
#this another type
@app.route('/sub/<sub>/<int:a>/<int:b>')
def subtract(sub,a,b):
    obj1 = Operator(a,b)
    res1 = str(obj1.sub())
    return res1
'''

if __name__ == '__main__':
    app.run(debug = True, port = 5132)        