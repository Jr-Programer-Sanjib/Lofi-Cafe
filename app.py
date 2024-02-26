from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store orders in a list (you can replace this with a database)
orders = []

# Routes
@app.route('/')
def index():
    return render_template('place_order.html')

@app.route('/order', methods=['POST'])
def order():
    if request.method == 'POST':
        coffee_name = request.form['coffee_name']
        table_number = request.form['table_number']
        
        # Store the order
        orders.append({'coffee_name': coffee_name, 'table_number': table_number})
        
        return render_template('order_success.html')

@app.route('/view_orders')
def view_orders():
    return render_template('view_orders.html', orders=orders)

@app.route('/fetch_orders')
def fetch_orders():
    return jsonify(orders)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)