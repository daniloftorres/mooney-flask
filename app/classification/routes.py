# app/classification/routes.py
from flask import request, jsonify
from .blueprint import classification_bp
import joblib
import numpy as np

# Carregar o modelo treinado
model = joblib.load('app/classification/iris_model.pkl')

@classification_bp.route('/predict', methods=['POST'])
def predict():
    input_data = request.json['data']
    
    # Converter input_data para um array NumPy para facilitar a manipulação
    input_array = np.array(input_data)
    
    # Garantir que input_array é 2D
    if input_array.ndim == 1:
        input_array = np.array([input_data])  # Transforma em 2D com uma única amostra
    
    # Fazer a previsão
    prediction = model.predict(input_array).tolist()
    
    return jsonify({'prediction': prediction})

    """# Resposta estática temporária para diagnóstico
    return jsonify({'message': 'Predict endpoint is working.'})"""
