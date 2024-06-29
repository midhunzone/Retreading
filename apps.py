from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num_tires = float(request.form['num_tires'])
        raw_material_cost_per_unit = float(request.form['raw_material_cost_per_unit'])
        fixed_capital = 3730000.00
        selling_price_per_tire = 4000  # assuming a fixed selling price per tire
        
        raw_material_cost = num_tires * raw_material_cost_per_unit
        total_sales_realization = num_tires * selling_price_per_tire
        total_operating_expenses = raw_material_cost + 2000000  # assuming other fixed expenses
        
        gross_margin = total_sales_realization - total_operating_expenses
        taxes = gross_margin * 0.12
        net_margin = gross_margin - taxes
        profit_percentage = (net_margin / total_operating_expenses) * 100
        roi = (net_margin / fixed_capital) * 100

        return render_template('index.html', fixed_capital=fixed_capital, raw_material_cost_per_unit=raw_material_cost_per_unit, 
                               gross_margin=gross_margin, taxes=taxes, net_margin=net_margin, profit_percentage=profit_percentage, 
                               roi=roi, num_tires=num_tires, raw_material_cost=raw_material_cost, total_sales_realization=total_sales_realization, 
                               total_operating_expenses=total_operating_expenses)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
