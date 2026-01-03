import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Global variable to hold the model in memory
model = None

# --- STEP 3: DYNAMIC PATH LOGIC ---
# This finds the directory where THIS file (model_logic.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# This joins the BASE_DIR with your 'model' folder and file name.
# It automatically uses \ for Windows and / for Linux.
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'pneumodel.h5')
# ----------------------------------

def get_model():
    global model
    if model is None:
        # Check if the path exists (helpful for debugging on the server)
        if not os.path.exists(MODEL_PATH):
            # This will show up in your Render logs if the folder is named wrong
            raise FileNotFoundError(f"CRITICAL ERROR: Model not found at: {MODEL_PATH}")
            
        print(f"--- Successfully Loading AI Model from: {MODEL_PATH} ---")
        model = load_model(MODEL_PATH)
    return model

def predict_pneumonia(img_path):
    net = get_model()
    
    # Pre-processing (ensure 224x224 matches your CNN training)
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