import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from sklearn.mixture import GaussianMixture

# Cargar el conjunto de datos de transacciones
data = pd.read_csv('transacciones.csv')

# Seleccionar las características relevantes para la detección de fraudes
features = ['monto', 'hora', 'día_semana']

# Crear modelos para la detección de fraudes
models = {
    'Isolation Forest': IsolationForest(contamination=0.01),
    'Local Outlier Factor': LocalOutlierFactor(contamination=0.01),
    'One-Class SVM': OneClassSVM(nu=0.01),
    'Minimum Covariance Determinant': EllipticEnvelope(contamination=0.01),
    'Gaussian Mixture Models': GaussianMixture(n_components=2)
}

# Entrenar y predecir con cada modelo
predictions = {}
for model_name, model in models.items():
    model.fit(data[features])
    predictions[model_name] = model.predict(data[features])

# Agregar las predicciones al conjunto de datos
for model_name, preds in predictions.items():
    data[model_name] = preds

# Mostrar las transacciones marcadas como anómalas (fraudes) por cada modelo
for model_name in models.keys():
    frauds = data[data[model_name] == -1]
    print(f"Fraudes detectados por {model_name}:")
    print(frauds)
    print()

# Guardar los resultados en un archivo CSV
data.to_csv('resultados.csv', index=False)
print("Resultados guardados en 'resultados.csv'")
