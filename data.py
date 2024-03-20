from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression  # This is just for demonstration

app = Flask(__name__)

# Dummy model for demonstration. Replace it with your actual model.
model = LinearRegression()
# Assuming the model expects some features and predicts two values (high and low prices, for instance)

@app.route('/')
def home():
    # Render the home page
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Getting input data from the form
            close_last = float(request.form['close_last'])
            volume = float(request.form['volume'])
            open_price = float(request.form['open_price'])

            # For demonstration, replace the following line with your model's prediction code
            # Here, it's assumed your model returns a list/array with two numbers: [predicted_high_price, predicted_low_price]
            input_data = np.array([[close_last, volume, open_price]])
            predicted_prices = model.predict(input_data)

            # Extracting predicted values
            predicted_high_price = predicted_prices[0]  # Dummy value, replace with actual model output
            predicted_low_price = predicted_prices[1]  # Dummy value, replace with actual model output

            # Send the prediction to the 'result.html' template
            return render_template('result.html', high_price=predicted_high_price, low_price=predicted_low_price)
        except Exception as e:
            return render_template('result.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
