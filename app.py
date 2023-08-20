from flask import Flask, request, render_template, redirect, flash
# from forex_python.converter import CurrencyRates, CurrencyCodes
from currency_converter import CurrencyConverter

app = Flask(__name__)
c = CurrencyConverter()
app.config["SECRET_KEY"] = "4534gdghjkef5d#$RGR^HDG"

def forex_converter(x, y, z):
    return c.convert(x, y, z)
    
@app.route('/') 
def home_page():
    return render_template('home.html')

@app.route('/result')
def result_page():
    FROM = request.args['FROM']
    TO = request.args['TO']
    AMOUNT = request.args['AMOUNT']

    try:
        result = round(forex_converter(AMOUNT, FROM, TO), 2)
        formatted_result = f"{result:.2f}"
        return render_template('result.html', result = formatted_result, to = TO)
    
    except ValueError as e:
        error_message = str(e)
        if error_message[0] == 'c':
            error_message = 'Please enter a valid number'
            flash(error_message)
        else: 
            flash(error_message)
        return redirect('/')
        


# c = CurrencyRates()
# c.get_rates('USD')
# c.get_rate('USD', 'INR')

