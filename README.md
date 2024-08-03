# Clasificación de tumores de cerebro utilizando aprendizaje por transferencia

En este repositorio constan los resultados de la detección de tumores de cerebro empleando el modelo pre-entrenado Xception.

El conjunto de datos utilizado se encuentra en el siguiente enlace: [Tumor Brain](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

En el directorio Xception existen dos cuadernos de Google Colab

* __Tumor_Brain_Xception.ipynb__ : Detección de tumores de Cerebro sin aplicar CLAHE al set de datos.
* __Tumor_Brain_Xception_CLAHE.ipynb__ : Detección de tumores de Cerebro aplicando CLAHE al set de datos.


En el directorio clahe se encuentra el archivo _*clahe.py*_, el cual contien el código para aplicar CLAHE al conjunto de datos.
