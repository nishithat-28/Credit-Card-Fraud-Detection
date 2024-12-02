from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    result_class = ""  # New variable to hold the class for styling
    if request.method == 'POST':
        input_df = request.form['features']
        input_df_lst = input_df.split(',')
        features = np.array(input_df_lst, dtype=np.float64)
        prediction_result = model.predict(features.reshape(1, -1))
        
        if prediction_result[0] == 0:
            prediction = "✅ Legitimate transaction"
            result_class = "legitimate"  # Set class for legitimate
        else:
            prediction = "⚠️ Fraudulent transaction"
            result_class = "fraudulent"  # Set class for fraudulent
    
    return render_template('index.html', prediction=prediction, result_class=result_class)

if __name__ == '__main__':
    app.run(debug=True)