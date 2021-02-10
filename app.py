import pickle
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


modelpath = os.path.join(os.getcwd(),'Model\model.pkl')
with open(modelpath, 'rb') as f:
    model = pickle.load(f)
print(modelpath,'This was success')

@app.route('/hello')
def hello():
    return 'hi'


@app.route('/CustomerRetentionPrediction', methods=['GET', 'POST'])
def SalaryPredict():
    exp_input = [request.json['gender'],request.json['SeniorCitizen'],request.json['Partner'],request.json['Dependents'],request.json['tenure'],request.json['PhoneService'],request.json['MultipleLines'],request.json['InternetService'],request.json['OnlineSecurity'],request.json['OnlineBackup'],request.json['DeviceProtection'],request.json['TechSupport'],request.json['StreamingTV'],request.json['StreamingMovies'],request.json['Contract'],request.json['PaperlessBilling'],request.json['PaymentMethod'],request.json['MonthlyCharges'],request.json['TotalCharges']]
    Retention = model.predict([exp_input])
    return jsonify({'results': str(Retention[0])})


if __name__ == "__main__":
    app.run()
