from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/custompii', methods=['POST'])
def custompii():
    if 'rafaTest' not in request.json:
        return jsonify({'error': 'Missing rafaTest information'}), 400

    rafa_test = request.json['rafaTest']
    # Perform any necessary processing or validation on the rafaTest data
    
    # Example response
    response = {'message': 'rafaTest received successfully'}

    return jsonify(response)

if __name__ == '__main__':
    app.run()
