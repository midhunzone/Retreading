from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Define all variables used in the template
    fixed_capital = 0
    raw_material_cost_per_tyre = 0
    gross_margin = 0
    taxes = 0
    net_margin = 0
    profit_percentage = 0
    roi = 0

    return render_template('index.html',
                           fixed_capital=fixed_capital,
                           raw_material_cost_per_tyre=raw_material_cost_per_tyre,
                           gross_margin=gross_margin,
                           taxes=taxes,
                           net_margin=net_margin,
                           profit_percentage=profit_percentage,
                           roi=roi)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Extract data from form submission
    total_operating_expenses = float(request.form['total_operating_expenses'])
    total_sales_realization = float(request.form['total_sales_realization'])
    fixed_capital = 3730000  # Example value, replace with actual logic
    raw_material_cost_per_tyre = 3326.50  # Example value, replace with actual logic
    gross_margin = total_sales_realization - total_operating_expenses
    taxes = gross_margin * 0.12
    net_margin = gross_margin - taxes
    profit_percentage = (net_margin / total_operating_expenses) * 100
    roi = (net_margin / fixed_capital) * 100

    return render_template('index.html',
                           fixed_capital=fixed_capital,
                           raw_material_cost_per_tyre=raw_material_cost_per_tyre,
                           gross_margin=gross_margin,
                           taxes=taxes,
                           net_margin=net_margin,
                           profit_percentage=profit_percentage,
                           roi=roi)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
