from flask import Flask, request, jsonify
from tasks import process_data

app = Flask(__name__)

@app.route('/submit_task', methods=['POST'])
def submit_task():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'Data is required'}), 400

    task = process_data.delay(data)
    return jsonify({'task_id': str(task)}), 202

@app.route('/get_result/<task_id>', methods=['GET'])
def get_result(task_id):
    return jsonify({'status': 'Task completed', 'result': task_id}), 200

if __name__ == '__main__':
    app.run(debug=True)