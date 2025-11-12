"""
Unit tests for NkuAlert Flask application
"""
import pytest
import os
import json
import tempfile
from datetime import datetime, timedelta
from app import app, load_alerts, save_alerts, is_past


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    # Create a temporary file for alerts during testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    # Set the alerts file environment variable
    os.environ['ALERTS_FILE'] = temp_file
    
    # Create app with test configuration
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    
    with app.test_client() as client:
        with app.app_context():
            yield client
    
    # Cleanup: remove temporary file
    if os.path.exists(temp_file):
        os.unlink(temp_file)


@pytest.fixture
def sample_alerts():
    """Create sample alerts for testing"""
    return [
        {
            "id": 1,
            "category": "Weather",
            "message": "Test weather alert",
            "location": "Test Location",
            "timestamp": datetime.now().isoformat()
        },
        {
            "id": 2,
            "category": "Health",
            "message": "Test health alert",
            "location": "Test Location",
            "timestamp": (datetime.now() - timedelta(hours=80)).isoformat()  # Past alert
        }
    ]


def test_index_page(client):
    """Test that the index page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'NkuAlert' in response.data or b'nkualert' in response.data.lower()


def test_load_and_save_alerts(client, sample_alerts):
    """Test loading and saving alerts"""
    # Save alerts
    save_alerts(sample_alerts)
    
    # Load alerts
    loaded_alerts = load_alerts()
    
    assert len(loaded_alerts) == 2
    assert loaded_alerts[0]['id'] == 1
    assert loaded_alerts[0]['category'] == 'Weather'


def test_is_past_function(client, sample_alerts):
    """Test the is_past function to check if alerts are older than 72 hours"""
    # Recent alert (should not be past)
    recent_alert = {
        "id": 1,
        "category": "Weather",
        "message": "Recent alert",
        "location": "Test",
        "timestamp": datetime.now().isoformat()
    }
    assert not is_past(recent_alert)
    
    # Old alert (should be past)
    old_alert = {
        "id": 2,
        "category": "Health",
        "message": "Old alert",
        "location": "Test",
        "timestamp": (datetime.now() - timedelta(hours=80)).isoformat()
    }
    assert is_past(old_alert)


def test_api_alerts_endpoint(client, sample_alerts):
    """Test the API alerts endpoint"""
    save_alerts(sample_alerts)
    
    response = client.get('/api/alerts')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['category'] in ['Weather', 'Health']


def test_post_alert_form(client):
    """Test that the post alert form page loads"""
    response = client.get('/post')
    assert response.status_code == 200


def test_filter_alerts(client, sample_alerts):
    """Test filtering alerts by category"""
    save_alerts(sample_alerts)
    
    # Test filtering by Weather category
    response = client.get('/filter/Weather')
    assert response.status_code == 200
    
    # Test filtering by All
    response = client.get('/filter/All')
    assert response.status_code == 200