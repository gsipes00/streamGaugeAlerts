import os
import json
import logging

ALERTS_FILE = os.path.join(os.path.dirname(__file__), "active_flood_alerts.json")

def load_active_flood_alerts():
    """Load active flood alerts from JSON file."""
    if os.path.exists(ALERTS_FILE):
        try:
            with open(ALERTS_FILE, "r") as f:
                data = json.load(f)
                return data.get("active_flood_alerts", {})
        except Exception as e:
            logging.error(f"Error loading alerts file: {e}")
    return {}

def save_active_flood_alerts(alerts):
    """Save active flood alerts to JSON file."""
    try:
        with open(ALERTS_FILE, "w") as f:
            json.dump({"active_flood_alerts": alerts}, f)
    except Exception as e:
        logging.error(f"Error saving alerts file: {e}")
