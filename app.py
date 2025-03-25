from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/datetime', methods=['GET'])
def get_datetime():
    now = datetime.datetime.now()
    return jsonify({'datetime': now.isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)