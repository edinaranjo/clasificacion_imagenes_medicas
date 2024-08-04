# Clasificación de tumores de cerebro utilizando aprendizaje por transferencia

En este repositorio constan los resultados de la detección de tumores de cerebro empleando los modelos pre-entrenados VGG19, ResNet50 y Xception.

El conjunto de datos utilizado se encuentra en el siguiente enlace: [Tumor Brain](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

En el directorio VGG19 hay dos cuadernos de Google Colab en donde se indica el proceso de detección de tumores de cerebro utilizando VGG19.


En el directorio ResNet50 hay un cuadernos de Google Colab en donde se indica el proceso de detección de tumores de cerebro utilizando ResNet50.


En el directorio Xception existen dos cuadernos de Google Colab

* __Tumor_Brain_Xception.ipynb__ : Detección de tumores de Cerebro con Xception sin aplicar CLAHE al set de datos.
* __Tumor_Brain_Xception_CLAHE.ipynb__ : Detección de tumores de Cerebro con Xception aplicando CLAHE al set de datos.


En el directorio clahe se encuentra el archivo _*clahe.py*_, el cual contien el código para aplicar CLAHE al conjunto de datos.
