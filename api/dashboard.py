import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    energy_response = requests.get('http://localhost:5000/api/energy_usage_insights')
    maintenance_response = requests.get('http://localhost:5000/api/predictive_maintenance_alerts')
    recommendations_response = requests.get('http://localhost:5000/api/dynamic_recommendations')

    energy_insights = energy_response.json()
    maintenance_alerts = maintenance_response.json()
    dynamic_recommendations = recommendations_response.json()

    return render_template('dashboard.html', energy_insights=energy_insights, maintenance_alerts=maintenance_alerts, dynamic_recommendations=dynamic_recommendations)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)