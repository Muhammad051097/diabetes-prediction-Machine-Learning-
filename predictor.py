import joblib

def predict_diabetes(input_data, model_name):
    model = joblib.load(f'ml_model/{model_name}_model.pkl')
    prediction = model.predict([input_data])
    return 'Positive' if prediction[0] == 1 else 'Negative'
