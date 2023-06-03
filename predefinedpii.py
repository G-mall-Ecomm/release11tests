from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predefinedpii', methods=['POST'])
def predefinedpii():
    if 'creditcard' not in request.json:
        return jsonify({'error': 'Missing credit card information'}), 400

    credit_card = request.json['creditcard']
    # Perform any necessary processing or validation on the credit card data
    
    # Example response
    response = {'message': 'Credit card received successfully'}

    return jsonify(response)

if __name__ == '__main__':
    app.run()
