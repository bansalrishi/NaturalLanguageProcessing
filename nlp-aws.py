from flask import Flask, request, jsonify
import numpy as np
import joblib
import json

pkl_file = "sentiment-trained-model.pkl"
tfidf_file = "sentiment-trained-tfidf.pkl"
custom_port = "5000"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome ML predictions"

@app.route('/predict/', methods=['POST'])
def predict():
    data = request.get_json()
    data = tfidf.transform(data).toarray()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)



if __name__ == '__main__':
    tfidf = joblib.load(tfidf_file)
    model = joblib.load(pkl_file)
    app.run(host='0.0.0.0', port=custom_port)



