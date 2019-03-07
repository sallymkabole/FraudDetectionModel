import numpy as np
from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0]
    return jsonify(output)



@app.route('/transact', methods=['POST']) #GET requests will be blocked
def json_example():
	req_data = request.get_json()
	amount = req_data['amount']
	print(amount)
	return '''withdraw:{} '''.format(amount)




if __name__ == '__main__':
    app.run(port=5000, debug=True)


    