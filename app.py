from flask import Flask, request, jsonify
from transformers import pipeline
import json
import os

app = Flask(__name__)

# --- Global variables for model and label map ---
classifier = None
label_map = None

MODEL_DIR = os.path.join(os.getcwd(), "DistBERT")
LABEL_MAP_FILE = os.path.join(MODEL_DIR, "int_to_category.json")

def load_model():
    """Loads the model and label map once."""
    global classifier, label_map

    print(f"Loading model from: {MODEL_DIR}")
    print(f"Loading label map from: {LABEL_MAP_FILE}")

    try:
        # Load the label mapping
        with open(LABEL_MAP_FILE, 'r') as f:
            label_map = json.load(f)
        print("Label mapping loaded successfully")

        # Create the text classification pipeline
        classifier = pipeline("text-classification", model=MODEL_DIR)
        print("Model pipeline loaded successfully!")

    except Exception as e:
        print(f"Error loading model or label map: {e}")
        classifier = None
        label_map = None 


def initialize_app():
    load_model()


with app.app_context():
    initialize_app()


@app.route('/api/predictions', methods=['POST'])
def predict():
    if classifier is None:
        return jsonify({"error": "Model not loaded. Server might be initializing or encountered an error."}), 503 

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    tags = data.get('tags')

    if not tags or not isinstance(tags, list):
        return jsonify({"error": "Missing or invalid 'tags' in request body. Expected a list of strings."}), 400

    if not all(isinstance(item, str) for item in tags):
        return jsonify({"error": "'tags' must contain only strings."}), 400

    try:
        predictions = classifier(tags)
        print('Predictions were succesfully made')
        results = []
        for i, text in enumerate(tags):
            predicted_label_raw = predictions[i]['label']

            # Extract integer from 'LABEL_X' format
            predicted_label_int = int(predicted_label_raw.split('_')[-1])

            # Map to real label name if label_map is available
            real_label = label_map.get(str(predicted_label_int), predicted_label_raw) if label_map else predicted_label_raw

            results.append({
                "text": text,
                "predicted_label": real_label,
                "score": predictions[i]['score']
            })
        print('Succesfully predicted all tags')
        return jsonify({"predictions": results}), 200

    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({"error": "An internal error occurred during prediction."}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    status = "ok" if classifier is not None else "model_loading_error"
    return jsonify({"status": status, "model_loaded": classifier is not None}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
