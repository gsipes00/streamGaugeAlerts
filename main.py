"""
Stream Gauge Flood Alert Application

Monitors a real-time XML stream gauge feed and sends alerts to the Konexus API based on flood conditions.
"""
import time
import requests
import xml.etree.ElementTree as ET
import time
import logging
from config import CHECK_INTERVAL_SECONDS, GAUGE_CONFIGS, KONEXUS_CLIENT_ID, KONEXUS_CLIENT_SECRET, XML_FEED_URL, KONEXUS_API_URL, KONEXUS_SENDER_ID
from api import fetch_gauge_data, send_konexus_alert
from alerts import should_send_alert
from storage import load_active_flood_alerts, save_active_flood_alerts
active_flood_alerts = load_active_flood_alerts()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
# Konexus OAuth2.0 token endpoint
KONEXUS_TOKEN_URL = "https://auth.alertsense.com/connect/token"


def process_gauges():
    root = fetch_gauge_data()
    if root is None:
        return
    for gauge in root.findall(".//gage_wl"):
        gauge_id = gauge.get("id")
        gauge_name = gauge.get("name", "Unknown")
        stage_str = gauge.get("stage", "0")
        logging.info(f"Gauge {gauge_id}: {gauge_name}, Stage: {stage_str}")
        try:
            stage_height = float(stage_str)
        except ValueError:
            logging.warning(f"Invalid stage value for gauge {gauge_id}: {stage_str}")
            continue
        config = GAUGE_CONFIGS.get(gauge_id)
        if not config:
            continue  # Only monitor configured gauges
        last_alert = active_flood_alerts.get(gauge_id)
        last_stage = last_alert["stage"] if isinstance(last_alert, dict) and "stage" in last_alert else last_alert
        send_alert, alert_type = should_send_alert(gauge_id, stage_height, last_stage, config)
        if send_alert and alert_type:
            api_response = send_konexus_alert(gauge_id, gauge_name, stage_height, alert_type, config)
            # Parse timestamp from DateSent in API response
            def parse_datesent(datesent):
                import re, datetime
                match = re.match(r"/Date\((\d+)-\d+\)/", datesent)
                if match:
                    ms = int(match.group(1))
                    dt = datetime.datetime.utcfromtimestamp(ms / 1000)
                    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                return None
            timestamp = None
            alert_sent = False
            if api_response and "SentStatus" in api_response:
                datesent = api_response["SentStatus"].get("DateSent")
                timestamp = parse_datesent(datesent) if datesent else None
            if api_response and "Status" in api_response:
                alert_sent = api_response["Status"].get("isSuccess", False)
            if alert_type == "FLOOD ALL-CLEAR":
                del active_flood_alerts[gauge_id]
            else:
                active_flood_alerts[gauge_id] = {
                    "timestamp": timestamp if timestamp else time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "stage": alert_type.split()[1].lower(),
                    "level": stage_height,
                    "alertSent": alert_sent
                }
            save_active_flood_alerts(active_flood_alerts)


def run_monitoring_loop():
    logging.info("Starting Stream Gauge Flood Alert Application...")
    while True:
        process_gauges()
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_monitoring_loop()
