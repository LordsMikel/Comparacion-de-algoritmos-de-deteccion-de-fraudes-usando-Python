# Detección de Fraudres en Transacciones Financieras

Este proyecto tiene como objetivo detectar fraudes en transacciones financieras utilizando múltiples algoritmos de detección de anomalías. Se implementa en Python y utiliza bibliotecas populares de aprendizaje automático y ciencia de datos.

## Características

- Comparación de varios algoritmos de detección de fraudes.
- Implementación en Python, aprovechando las bibliotecas populares como Scikit-learn.
- Análisis de diferentes características relevantes para la detección de fraudes en transacciones.
- Evaluación de la efectividad de los algoritmos mediante la comparación de resultados y métricas de rendimiento.

## Algoritmos Utilizados

El proyecto utiliza varios algoritmos de detección de anomalías para la detección de fraudes en transacciones financieras. A continuación, se describen brevemente los algoritmos utilizados:

- **Isolation Forest**: Este algoritmo construye un conjunto de árboles de aislamiento para separar las instancias normales de las anomalías. Las anomalías se consideran más fácilmente aislables y requieren menos particiones para ser aisladas. Por lo tanto, se consideran como puntos fuera de lo común.

- **Local Outlier Factor (LOF)**: Este algoritmo compara la densidad local de una instancia con respecto a sus vecinos. Las instancias con una densidad significativamente más baja que sus vecinos se consideran anomalías. LOF es capaz de detectar anomalías locales en entornos de diferentes densidades.

- **One-Class SVM**: Este algoritmo entrena un modelo utilizando solo instancias normales y luego mapea instancias nuevas en función de su proximidad al hiperplano de separación. Las instancias que se encuentran lejos del hiperplano se consideran anomalías.

- **Minimum Covariance Determinant (MCD)**: Este algoritmo estima la matriz de covarianza de los datos y calcula la distancia de Mahalanobis para cada instancia. Las instancias con una distancia de Mahalanobis más allá de un umbral se consideran anomalías. MCD es un estimador robusto que puede detectar puntos atípicos incluso en presencia de valores atípicos en los datos.

- **Gaussian Mixture Models (GMM)**: Este algoritmo asume que los datos se distribuyen según una mezcla de distribuciones Gaussianas. Estima los parámetros de las distribuciones y asigna probabilidades de pertenencia a cada instancia. Las instancias con una baja probabilidad de pertenencia se consideran anomalías.

Cada algoritmo tiene sus propias características y suposiciones subyacentes, por lo que es recomendable experimentar y evaluar su rendimiento en función de los datos específicos y los requisitos del proyecto.


## Requisitos
- Python 3.x
- Bibliotecas: Pandas, Scikit-learn, y otras bibliotecas requeridas (consultar el archivo `requirements.txt` para obtener una lista completa)

## Instrucciones de uso

1. Clona o descarga el repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado.
3. Instala las dependencias utilizando el siguiente comando: `pip install -r requirements.txt`.
4. Coloca tus datos de transacciones en formato CSV en el archivo `transacciones.csv` (asegúrate de que los datos sean apropiados y contengan características relevantes para la detección de fraudes).
5. Abre el archivo `deteccion_fraudes.py` y ajusta los parámetros, características y algoritmos según tus necesidades.
6. Ejecuta el programa utilizando el siguiente comando: `python deteccion_fraudes.py`.
7. Analiza los resultados en la consola y verifica el archivo `resultados.csv` que contiene los resultados guardados.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si tienes sugerencias, mejoras o correcciones, no dudes en abrir un pull request o reportar un problema en el repositorio.

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).
