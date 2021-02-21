from flask import Flask, render_template
from flask import request

app = Flask(__name__)



    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer

    

    
@app.route('/',methods=['PUT'])
def api():
    sharon={
        "name": "sharon",
        "college":"stj",

    }
    return sharon

@app.route('/add', methods=['POST'])
def result():
    
    value1  = (request.values.get('city'))
    #value2  = int(request.form.get('value2'))
    
    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer
    
    #value3 = add(value1, value2)
    
    result = {
        'city' : value1,
        #'value2' : value2,
       # 'value3': value3
    }
    return result
        


if __name__ == "__main__":
    app.run(debug=True)
