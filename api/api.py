from flask import Flask, jsonify
from database.db_manager import get_logs

app = Flask(__name__)

@app.route('/api/logs', methods=['GET'])
def get_log_data():
    logs = get_logs()
    return jsonify(logs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)