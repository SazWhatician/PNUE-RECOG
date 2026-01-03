import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = None

# --- PASTE YOUR PATH HERE ---
# Example: r"C:\Users\saswa\Desktop\PNEUFINAL\models\pneumodel.h5"
MODEL_PATH = r"C:\Users\saswa\Desktop\PNEUFINAL\model\pneumodel.h5"
# ----------------------------

def get_model():
    global model
    if model is None:
        # Check if the path actually exists
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"CRITICAL ERROR: The path you pasted does not exist: {MODEL_PATH}")
            
        print(f"--- Successfully Loading: {MODEL_PATH} ---")
        model = load_model(MODEL_PATH)
    return model

def predict_pneumonia(img_path):
    net = get_model()
    
    # Pre-processing
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255.0
    
    prediction = net.predict(x)[0][0]
    
    if prediction > 0.5:
        label = "Pneumonia Detected"
        conf = prediction * 100
    else:
        label = "Lungs Normal"
        conf = (1 - prediction) * 100
        
    return label, round(float(conf), 2)