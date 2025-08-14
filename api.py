import requests
import xml.etree.ElementTree as ET
import logging
from config import (
    KONEXUS_API_URL,
    XML_FEED_URL,
    KONEXUS_CLIENT_ID,
    KONEXUS_CLIENT_SECRET,
    KONEXUS_SENDER_ID
)

KONEXUS_TOKEN_URL = "https://auth.alertsense.com/connect/token"


def get_konexus_access_token():
    """Obtain OAuth2.0 access token using client credentials flow."""
    data = {
        "grant_type": "client_credentials",
        "client_id": KONEXUS_CLIENT_ID,
        "client_secret": KONEXUS_CLIENT_SECRET,
        "scope": "tamarack"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        resp = requests.post(KONEXUS_TOKEN_URL, data=data, headers=headers, timeout=10)
        resp.raise_for_status()
        token = resp.json().get("access_token")
        if not token:
            logging.error("Failed to obtain access token.")
        return token
    except Exception as e:
        logging.error(f"Error obtaining access token: {e}")
        return None


def fetch_gauge_data():
    """Fetch gauge data from XML feed."""
    try:
        response = requests.get(XML_FEED_URL, timeout=10)
        response.raise_for_status()
        return ET.fromstring(response.content)
    except Exception as e:
        logging.error(f"Error fetching gauge data: {e}")
        return None


def send_konexus_alert(gauge_id, gauge_name, stage_height, alert_type, config):
    """Sends an alert to the Konexus API for the specified gauge and alert type."""
    from config import KONEXUS_SENDER_ID
    subject = f"{alert_type.replace('_', ' ').title()}: {gauge_name}"
    message_body = f"<p>{alert_type.replace('_', ' ').title()}: {gauge_name} is at a stage height of {stage_height} ft.</p>"
    group_id = config.get("group_id")
    payload = {
        "settings": {
            "alertType": "Default",
            "channels": {
                "email": {"requestConfirmation": False, "send": True},
                "fax": {"send": False},
                "push": {"send": True},
                "textMessage": {"primary": True, "secondary": True, "deliveryMethod": "Sms", "send": True},
                "voice": {"send": False},
                "facebook": {"accountIds": [], "pageIds": [], "send": False},
                "twitter": {"accountIds": [], "send": False},
                "nextdoor": {"accounts": [], "send": False},
                "myAlertsApp": {"send": False},
                "microsoftTeams": {"send": False}
            },
            "clientContext": {
                "isResend": False,
                "clientId": "Python Application"
            },
            "formType": "Quick",
            "brandId": 2248,
            "facilities": {
                "facilities": [],
                "areas": []
            },
            "message": {
                "priority": "NonEmergency",
                "basic": {
                    "subject": subject,
                    "message": subject,
                    "messageBody": message_body
                },
                "files": [],
                "language": "en-us",
                "translate": True
            },
            "recipients": {
                "uniqueMyAlertsAppCount": 0,
                "uniqueEtnCount": 0,
                "uniqueGroupCount": 0,
                "uniqueContactCount": 1,
                "selectedContactCount": 1,
                "selectedGroupCount": 0,
                "groupIds": [group_id] if group_id else [],
                "mandatoryGroupIds": [],
                "contactIds": [],
                "groups": [],
                "contacts": [],
                "directories": [],
                "distributionListId": [],
                "searchFilters": []
            },
            "schedule": {
                "scheduled": False,
                "duration": 1440,
                "type": "Hickory"
            },
            "sender": {
                "id": KONEXUS_SENDER_ID,
                "displayName": "Water Sensor Integration",
                "email": "alerts@civicready.com",
                "callerId": "8334193463"
            },
            "hidden": False,
            "publicAlert": False,
            "weatherAlert": False,
            "requestConfirmation": False,
            "relatedAlertActions": {
                "disableReplyAll": False
            }
        },
        "status": {
            "isSuccess": True,
            "errorCode": "None",
            "validationFailures": [],
            "messages": []
        },
        "hasErrors": False,
        "isValid": True
    }
    access_token = get_konexus_access_token()
    if not access_token:
        logging.error("No access token available. Alert not sent.")
        return
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    try:
        resp = requests.post(KONEXUS_API_URL, json=payload, headers=headers, timeout=10)
        logging.info(f"Sent {alert_type} for {gauge_name} (ID: {gauge_id}) | Status: {resp.status_code}")
        logging.info(f"Response: {resp.text}")
    except Exception as e:
        logging.error(f"Error sending alert for {gauge_id}: {e}")
