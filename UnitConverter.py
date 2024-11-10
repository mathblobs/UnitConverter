from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/length')
def form():
    return render_template('UnitLengthForm.html')

@app.route('/weight')
def form_w():
    return render_template('UnitWeight1.html')

@app.route('/temperature')
def form_t():
    return render_template('UnitTemperature1.html')


def length_calculations_extensive(absolut_value, unit_from, unit_to):
    length_conversion_table = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344
    }
    middle_value = absolut_value * length_conversion_table[unit_from]
    return middle_value / length_conversion_table[unit_to]

def weight_calculations_extensive(absolut_value, unit_from, unit_to):
    weight_conversion_table = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 0.03527,
        'pound': 0.0022
    }
    middle_value = absolut_value * weight_conversion_table[unit_from]
    return middle_value / weight_conversion_table[unit_to]

def temperature_calculations_extensive(absolut_value, unit_from, unit_to):
    temperature_conversion_table = {
        'celsius': -272.15,
        'fahrenheit': -457.87,
        'kelvin': 1,
    }
    middle_value = absolut_value * temperature_conversion_table[unit_from]
    return middle_value / temperature_conversion_table[unit_to]

@app.route('/length_calculate', methods=['POST'])
def length_calculate():
    length = float(request.form['length'])
    lunitfrom = str(request.form['lunitfrom'])
    lunitto = str(request.form['lunitto'])
    result = length_calculations_extensive(length, lunitfrom, lunitto)
    return render_template('UnitLengthResult.html', number=length, result=result, lunitfrom=lunitfrom, lunitto=lunitto)

@app.route('/weight_calculate', methods=['POST'])
def weight_calculate():
    weight = float(request.form['weight'])
    lunitfrom = str(request.form['lunitfrom'])
    lunitto = str(request.form['lunitto'])
    result = weight_calculations_extensive(weight, lunitfrom, lunitto)
    return render_template('UnitWeight2.html', number=weight, result=result, lunitfrom=lunitfrom, lunitto=lunitto)

@app.route('/temperature_calculate', methods=['POST'])
def temperature_calculate():
    temp = float(request.form['temp'])
    lunitfrom = str(request.form['lunitfrom'])
    lunitto = str(request.form['lunitto'])
    result = temperature_calculations_extensive(temp, lunitfrom, lunitto)
    return render_template('UnitTemperature2.html', number=temp, result=result, lunitfrom=lunitfrom, lunitto=lunitto)

if __name__ == '__main__':
    app.run(debug=True)