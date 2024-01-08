from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<string_to_print>')
def print_string(string_to_print):
   print(string_to_print) # Only print the string to the console
   return f'{string_to_print}', 200

@app.route('/count/<int:number>')
def count(number):
   numbers_range = range(number)
   return '\n'.join(map(str, numbers_range)) + '\n', 200

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
   result = None
   if operation == '+':
       result = num1 + num2
   elif operation == '-':
       result = num1 - num2
   elif operation == '*':
       result = num1 * num2
   elif operation == 'div':
       result = num1 / num2
   elif operation == '%':
       result = num1 % num2

   return str(result), 200

if __name__ == '__main__':
   app.run(port=5555, debug=True)
