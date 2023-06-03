from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/customsenstive', methods=['POST'])
def custompii():
    if 'rafa_test' not in request.json:
        return jsonify({'error': 'Missing rafa_test information'}), 400

    rafa_test = request.json['rafa_test']
    # Perform any necessary processing or validation on the rafa_test data
    
    # Example response
    response = {'message': 'rafa_test received successfully'}

    return jsonify(response)

if __name__ == '__main__':
    app.run()
