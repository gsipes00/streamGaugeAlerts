"""
Configuration for the Stream Gauge Flood Alert Application.
"""


# Use /data for persistent disk on Render
ALERTS_FILE = "/data/active_flood_alerts.json"

# OAuth2.0 credentials for Konexus API (read from environment variables)
import os
KONEXUS_CLIENT_ID = os.environ.get("KONEXUS_CLIENT_ID")
KONEXUS_CLIENT_SECRET = os.environ.get("KONEXUS_CLIENT_SECRET")

# XML feed for stream gauge data
XML_FEED_URL = "https://hayscounty.wetec.us/WETMap/public/hayswlpublic.xml"

# Polling interval (seconds)
CHECK_INTERVAL_SECONDS = 30

# Gauge configuration: gauge ID mapped to flood stage and name
GAUGE_CONFIGS = {
    # "50080007": {
    #     "stages": {
    #         "stage1": 0.0,
    #         "stage2": 0.001
    #     },
    #     "name": "Cottonwood Creek at East McCarty Lane Water Level"
    # },
    # "50081007": {
    #     "stages": {
    #         "stage1": 0.01 * 1.25,
    #         "stage2": 0.01 * 1.50
    #     },
    #     "name": "Cottonwood Creek at Clovis R. Barker Road Water Level"
    # },
    # "50082007": {
    #     "stages": {
    #         "stage1": 0.01 * 1.25,
    #         "stage2": 0.01 * 1.50
    #     },
    #     "name": "Purgatory Creek at Hunter Road Water Level"
    # },
    "50083007": {
        "stages": {
            "stage1": 0.05,
            "stage2": 3.0
        },
        "name": "Purgatory Creek at Guadalupe Street Water Level",
        "group_id": 437933
    },
    "50084007": {
        "stages": {
            "stage1": 0.05,
            "stage2": 5.0
        },
        "name": "San Marcos River at Cape Road Water Level",
        "group_id": 437919
    },
    # "50085007": {
    #     "stages": {
    #         "stage1": 0.01 * 1.25,
    #         "stage2": 0.01 * 1.50
    #     },
    #     "name": "By Pass Creek at Harris Hill Road Water Level"
    # },
    # "50086007": {
    #     "stages": {
    #         "stage1": 0.02 * 1.25,
    #         "stage2": 0.02 * 1.50
    #     },
    #     "name": "Sink Creek at Lime Kiln Road Water Level"
    # },
    # "50087007": {
    #     "stages": {
    #         "stage1": 0.01 * 1.25,
    #         "stage2": 0.01 * 1.50
    #     },
    #     "name": "Sink Creek at Bert Brown Road Water Level"
    # },
    # "50088007": {
    #     "stages": {
    #         "stage1": 0.02 * 1.25,
    #         "stage2": 0.02 * 1.50
    #     },
    #     "name": "Willow Springs at Hunter Road Water Level"
    # },
    # "50089007": {
    #     "stages": {
    #         "stage1": 0.01 * 1.25,
    #         "stage2": 0.01 * 1.50
    #     },
    #     "name": "Willow Springs at Patton Street Water Level"
    # }
}

# Konexus distribution list and sender IDs
# KONEXUS_DISTRIBUTION_LIST_ID = "b328849f-3cc4-48da-a983-6e0677f87879"
KONEXUS_SENDER_ID = 0
# KONEXUS_CONTACT_ID = [7605685]