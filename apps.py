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
    return_on_investment = 0

    return render_template('index.html',
                           fixed_capital=fixed_capital,
                           raw_material_cost_per_tyre=raw_material_cost_per_tyre,
                           gross_margin=gross_margin,
                           taxes=taxes,
                           net_margin=net_margin,
                           profit_percentage=profit_percentage,
                           return_on_investment=return_on_investment)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
