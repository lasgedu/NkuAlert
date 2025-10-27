from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)

# JSON file to store alerts
ALERTS_FILE = 'alerts.json'

def load_alerts():
    """Load alerts from JSON file or return empty list"""
    if os.path.exists(ALERTS_FILE):
        try:
            with open(ALERTS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_alerts(alerts):
    """Save alerts to JSON file"""
    with open(ALERTS_FILE, 'w') as f:
        json.dump(alerts, f, indent=2)

def init_alerts():
    """Initialize with sample alerts if file doesn't exist"""
    alerts = load_alerts()
    if not alerts:
        sample_alerts = [
            {
                "id": 1,
                "category": "Weather",
                "message": "Heavy rainfall expected in Northern Province tomorrow. Stay indoors.",
                "location": "Northern Province",
                "timestamp": (datetime.now() - timedelta(hours=2)).isoformat()
            },
            {
                "id": 2,
                "category": "Health",
                "message": "Malaria prevention campaign starting next week in all health centers.",
                "location": "All Regions",
                "timestamp": (datetime.now() - timedelta(hours=12)).isoformat()
            },
            {
                "id": 3,
                "category": "Civic",
                "message": "Community meeting scheduled for Saturday at 2 PM at the community center.",
                "location": "Community Center",
                "timestamp": (datetime.now() - timedelta(days=1)).isoformat()
            },
            {
                "id": 4,
                "category": "Emergency",
                "message": "Power outage scheduled for maintenance from 9 AM to 12 PM.",
                "location": "Central District",
                "timestamp": (datetime.now() - timedelta(hours=6)).isoformat()
            }
        ]
        save_alerts(sample_alerts)
    return load_alerts()

@app.route('/')
def index():
    """Display all alerts on the homepage"""
    alerts = load_alerts()
    # Sort by timestamp, newest first
    alerts.sort(key=lambda x: x['timestamp'], reverse=True)
    return render_template('index.html', alerts=alerts, selected_category='All')

@app.route('/filter/<category>')
def filter_alerts(category):
    """Filter alerts by category"""
    alerts = load_alerts()
    if category != 'All':
        alerts = [alert for alert in alerts if alert['category'].lower() == category.lower()]
    alerts.sort(key=lambda x: x['timestamp'], reverse=True)
    return render_template('index.html', alerts=alerts, selected_category=category)

@app.route('/post', methods=['GET', 'POST'])
def post_alert():
    """Admin form to post new alerts"""
    if request.method == 'POST':
        alerts = load_alerts()
        
        # Get the next ID
        next_id = max([a['id'] for a in alerts], default=0) + 1
        
        new_alert = {
            "id": next_id,
            "category": request.form['category'],
            "message": request.form['message'],
            "location": request.form['location'],
            "timestamp": datetime.now().isoformat()
        }
        
        alerts.append(new_alert)
        save_alerts(alerts)
        
        return redirect(url_for('index'))
    
    return render_template('post.html')

@app.route('/api/alerts')
def api_alerts():
    """API endpoint to get all alerts (for potential future expansion)"""
    alerts = load_alerts()
    alerts.sort(key=lambda x: x['timestamp'], reverse=True)
    return jsonify(alerts)

def is_past(alert):
    """Check if alert is older than 72 hours"""
    alert_time = datetime.fromisoformat(alert['timestamp'])
    return datetime.now() - alert_time > timedelta(hours=72)

# Make is_past available to templates
app.jinja_env.globals.update(is_past=is_past)

if __name__ == '__main__':
    init_alerts()
    app.run(debug=True, host='0.0.0.0', port=5000)