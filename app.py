from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key')

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
                "category": "Civic",
                "message": "Monthly Umuganda scheduled for this Saturday at 7 AM. All community members should participate.",
                "location": "Kigali City",
                "timestamp": (datetime.now() - timedelta(hours=2)).isoformat()
            },
            {
                "id": 2,
                "category": "Weather",
                "message": "Heavy rainfall expected in Kigali tomorrow. Stay indoors and avoid flooded areas.",
                "location": "Kigali City",
                "timestamp": (datetime.now() - timedelta(hours=1)).isoformat()
            },
            {
                "id": 3,
                "category": "Health",
                "message": "Malaria prevention campaign starting next week at Kimironko Health Center. Free mosquito nets distribution.",
                "location": "Kimironko, Kigali",
                "timestamp": (datetime.now() - timedelta(hours=12)).isoformat()
            },
            {
                "id": 4,
                "category": "Emergency",
                "message": "Water supply interruption in Remera area for maintenance works. Water tankers available at sector office.",
                "location": "Remera, Kigali",
                "timestamp": (datetime.now() - timedelta(hours=6)).isoformat()
            },
            {
                "id": 5,
                "category": "Civic",
                "message": "Gacaca court hearing scheduled for Thursday at Nyarugenge District Court. All concerned parties to attend.",
                "location": "Nyarugenge District",
                "timestamp": (datetime.now() - timedelta(hours=18)).isoformat()
            },
            {
                "id": 6,
                "category": "Weather",
                "message": "Long dry season expected. Farmers advised to prepare for irrigation. Government subsidies available.",
                "location": "Rwanda",
                "timestamp": (datetime.now() - timedelta(days=1)).isoformat()
            },
            {
                "id": 7,
                "category": "Health",
                "message": "COVID-19 vaccination campaign at Kacyiru Health Center. Priority for elderly and immunocompromised.",
                "location": "Kacyiru, Kigali",
                "timestamp": (datetime.now() - timedelta(days=2)).isoformat()
            },
            {
                "id": 8,
                "category": "Emergency",
                "message": "Power outage scheduled for Nyamirambo sector due to infrastructure upgrade. Backup generators at hospitals.",
                "location": "Nyamirambo, Kigali",
                "timestamp": (datetime.now() - timedelta(hours=24)).isoformat()
            },
            {
                "id": 9,
                "category": "Civic",
                "message": "Genocide Memorial Week activities starting Monday at Kigali Genocide Memorial. Public invited to participate.",
                "location": "Kigali City",
                "timestamp": (datetime.now() - timedelta(days=3)).isoformat()
            },
            {
                "id": 10,
                "category": "Weather",
                "message": "Frost warning issued for Northern Province. Farmers urged to protect crops overnight.",
                "location": "Northern Province",
                "timestamp": (datetime.now() - timedelta(days=4)).isoformat()
            },
            {
                "id": 11,
                "category": "Health",
                "message": "Mobile health clinic visiting Gikondo sector. Free health screenings and consultations available.",
                "location": "Gikondo, Kigali",
                "timestamp": (datetime.now() - timedelta(days=5)).isoformat()
            },
            {
                "id": 12,
                "category": "Emergency",
                "message": "Flood alert for low-lying areas near Nyabarongo River. Residents advised to move to higher ground.",
                "location": "Kamonyi District",
                "timestamp": (datetime.now() - timedelta(days=6)).isoformat()
            },
            {
                "id": 13,
                "category": "Civic",
                "message": "Community meeting at Kanombe sector office to discuss waste management and recycling program.",
                "location": "Kanombe, Kigali",
                "timestamp": (datetime.now() - timedelta(days=7)).isoformat()
            },
            {
                "id": 14,
                "category": "Weather",
                "message": "Strong winds expected in Kigali. Secure outdoor furniture and be cautious on roads.",
                "location": "Kigali City",
                "timestamp": (datetime.now() - timedelta(days=8)).isoformat()
            },
            {
                "id": 15,
                "category": "Health",
                "message": "Nutrition training workshop at Muhima Health Center. Pregnant women and new mothers encouraged to attend.",
                "location": "Muhima, Kigali",
                "timestamp": (datetime.now() - timedelta(days=9)).isoformat()
            },
            {
                "id": 16,
                "category": "Emergency",
                "message": "Fire outbreak reported in Gisozi area. Fire department responding. Avoid the area until cleared.",
                "location": "Gisozi, Kigali",
                "timestamp": (datetime.now() - timedelta(days=10)).isoformat()
            },
            {
                "id": 17,
                "category": "Civic",
                "message": "Rwanda Day celebration at BK Arena. Cultural performances and community activities planned.",
                "location": "Kigali City",
                "timestamp": (datetime.now() - timedelta(days=11)).isoformat()
            },
            {
                "id": 18,
                "category": "Weather",
                "message": "Hailstorm warning for Eastern Province. Protect vehicles and crops from potential damage.",
                "location": "Eastern Province",
                "timestamp": (datetime.now() - timedelta(days=12)).isoformat()
            },
            {
                "id": 19,
                "category": "Health",
                "message": "Mental health awareness campaign at Kimisagara Youth Center. Free counseling sessions available.",
                "location": "Kimisagara, Kigali",
                "timestamp": (datetime.now() - timedelta(days=13)).isoformat()
            }
        ]
        save_alerts(sample_alerts)
    return load_alerts()


# ---- i18n helpers ----
LANG_EN = 'en'
LANG_RW = 'rw'

TRANSLATIONS = {
    'en': {
        'title': 'NkuAlert',
        'tagline': 'Timely local alerts for weather, health, and civic updates',
        'filters_all': 'All',
        'filters_weather': 'Weather',
        'filters_health': 'Health',
        'filters_civic': 'Civic',
        'filters_emergency': 'Emergency',
        'post_new': '+ Post New Alert (Admin)',
        'latest_alerts': 'Latest Alerts',
        'past': 'Past',
        'no_alerts': 'No alerts available at this time.',
        'footer': 'Community Alert System',
        'lang_en': 'English',
        'lang_rw': 'Kinyarwanda',
        'edit': 'Edit',
        'delete': 'Delete',
        'form_title_new': 'Post New Alert',
        'form_title_edit': 'Edit Alert',
        'form_tagline': 'Admin Alert Posting',
        'category': 'Category',
        'select_category': 'Select a category',
        'message': 'Message',
        'location': 'Location',
        'post_alert': 'Post Alert',
        'update_alert': 'Update Alert',
        'cancel': 'Cancel',
        'category_label': {
            'All': 'All',
            'Weather': 'Weather',
            'Health': 'Health',
            'Civic': 'Civic',
            'Emergency': 'Emergency',
        },
    },
    'rw': {
        'title': 'NkuAlert',
        'tagline': 'Amakuru yihutirwa y’ikirere, ubuzima, na serivisi z’abaturage',
        'filters_all': 'Byose',
        'filters_weather': 'Ikirere',
        'filters_health': 'Ubuzima',
        'filters_civic': 'Abaturage',
        'filters_emergency': 'Byihutirwa',
        'post_new': '+ Ongeramo Itangazo (Admin)',
        'latest_alerts': 'Amatangazo Aheruka',
        'past': 'Byashize',
        'no_alerts': 'Nta matangazo ahari ubu.',
        'footer': 'Sisitemu y’Amatangazo y’Abaturage',
        'lang_en': 'Icyongereza',
        'lang_rw': 'Ikinyarwanda',
        'edit': 'Hindura',
        'delete': 'Siba',
        'form_title_new': 'Ongeramo Itangazo',
        'form_title_edit': 'Hindura Itangazo',
        'form_tagline': 'Uburyo bwa Admin bwo Kwandika',
        'category': 'Icyiciro',
        'select_category': 'Hitamo icyiciro',
        'message': 'Ubutumwa',
        'location': 'Aho Biherereye',
        'post_alert': 'Ohereza Itangazo',
        'update_alert': 'Hindura Itangazo',
        'cancel': 'Subira Inyuma',
        'category_label': {
            'All': 'Byose',
            'Weather': 'Ikirere',
            'Health': 'Ubuzima',
            'Civic': 'Abaturage',
            'Emergency': 'Byihutirwa',
        },
    },
}


def get_lang():
    lang = session.get('lang', LANG_EN)
    return lang if lang in TRANSLATIONS else LANG_EN


def t(key):
    return TRANSLATIONS[get_lang()].get(key, key)


def category_label(category_key):
    mapping = TRANSLATIONS[get_lang()].get('category_label', {})
    return mapping.get(category_key, category_key)

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
    
    return render_template('post.html', alert=None)

@app.route('/api/alerts')
def api_alerts():
    """API endpoint to get all alerts (for potential future expansion)"""
    alerts = load_alerts()
    alerts.sort(key=lambda x: x['timestamp'], reverse=True)
    return jsonify(alerts)


@app.route('/edit/<int:alert_id>', methods=['GET', 'POST'])
def edit_alert(alert_id: int):
    alerts = load_alerts()
    target = next((a for a in alerts if a['id'] == alert_id), None)
    if not target:
        return redirect(url_for('index'))

    if request.method == 'POST':
        target['category'] = request.form['category']
        target['message'] = request.form['message']
        target['location'] = request.form['location']
        target['timestamp'] = datetime.now().isoformat()
        save_alerts(alerts)
        return redirect(url_for('index'))

    return render_template('post.html', alert=target)


@app.route('/delete/<int:alert_id>', methods=['POST'])
def delete_alert(alert_id: int):
    alerts = load_alerts()
    alerts = [a for a in alerts if a['id'] != alert_id]
    save_alerts(alerts)
    return redirect(url_for('index'))


@app.route('/lang/<lang_code>')
def set_language(lang_code: str):
    if lang_code in TRANSLATIONS:
        session['lang'] = lang_code
    return redirect(request.referrer or url_for('index'))

def is_past(alert):
    """Check if alert is older than 72 hours"""
    alert_time = datetime.fromisoformat(alert['timestamp'])
    return datetime.now() - alert_time > timedelta(hours=72)

# Make helpers available to templates
app.jinja_env.globals.update(is_past=is_past, t=t, category_label=category_label, get_lang=get_lang)

if __name__ == '__main__':
    init_alerts()
    app.run(debug=True, host='0.0.0.0', port=5000)