import cv2
import os
from pathlib import Path

# Ruta base del dataset de imágenes original
base_input_dir = '< path dataset original >'
# Ruta base donde se guardarán las imágenes procesadas
base_output_dir = '< path dataset nuevo >'

# Lista de nombres de las subcarpetas
subfolders = ['glioma', 'meningioma', 'notumor', 'pituitary']

# Crear el directorio de salida base si no existe
Path(base_output_dir).mkdir(parents=True, exist_ok=True)

# Inicializar el objeto CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Procesar cada subcarpeta
for subfolder in subfolders:
    input_dir = os.path.join(base_input_dir, subfolder)
    output_dir = os.path.join(base_output_dir, subfolder)
    
    # Crear el directorio de salida para la subcarpeta si no existe
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Obtener la lista de archivos de imagen en el directorio de entrada
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    
    # Procesar cada imagen
    for image_file in image_files:
        # Leer la imagen en escala de grises
        img = cv2.imread(os.path.join(input_dir, image_file), cv2.IMREAD_GRAYSCALE)
        
        # Aplicar CLAHE
        cl1 = clahe.apply(img)
        
        # Guardar la imagen procesada en el directorio de salida
        cv2.imwrite(os.path.join(output_dir, image_file), cl1)

print(f'Procesamiento completado. Las imágenes procesadas se guardaron en {base_output_dir}')
