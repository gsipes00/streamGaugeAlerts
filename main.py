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
        last_stage = active_flood_alerts.get(gauge_id)
        send_alert, alert_type = should_send_alert(gauge_id, stage_height, last_stage, config)
        if send_alert and alert_type:
            send_konexus_alert(gauge_id, gauge_name, stage_height, alert_type, config)
            if alert_type == "FLOOD ALL-CLEAR":
                del active_flood_alerts[gauge_id]
            else:
                active_flood_alerts[gauge_id] = alert_type.split()[1].lower()  # "stage1" or "stage2"
            save_active_flood_alerts(active_flood_alerts)


def run_monitoring_loop():
    logging.info("Starting Stream Gauge Flood Alert Application...")
    while True:
        process_gauges()
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_monitoring_loop()
