from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your trained classifier
classifier = joblib.load('svm_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    try:
        data = request.get_json()
        # Ensure all columns are provided for prediction
        features = [data[col] for col in ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
                                          'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
                                          'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
                                          'touch_screen', 'wifi']]
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Invalid input data'}), 400

    # Predict the price range
    prediction = classifier.predict([features])
    return jsonify({'price_range': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
