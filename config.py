"""
Configuration for the Stream Gauge Flood Alert Application.
"""

# Konexus API endpoint and authentication
KONEXUS_API_URL = "https://admin.alertsense.com/api/v2/alerts"
KONEXUS_BEARER_TOKEN = (
    "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg4Qzc1Nzg2RTkzMjUyN0U3M0VFOEM4MDE2NzY0NDRBOTBBQjk2REVSUzI1NiIsIng1dCI6ImlNZFhodWt5VW41ejdveUFGblpFU3BDcmx0NCIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJodHRwczovL2F1dGguYWxlcnRzZW5zZS5jb20iLCJuYmYiOjE3NTQ0MzIyNTAsImlhdCI6MTc1NDQzMjI1MCwiZXhwIjoxNzU3MDYxOTkzLCJhdWQiOiJ0YW1hcmFjayIsInNjb3BlIjpbInRhbWFyYWNrIl0sImNsaWVudF9pZCI6ImV4dC0yMzc4LXdhdGVyLXNlbnNvciIsImFkbWluIjoiZmFsc2UiLCJnbG9iYWxUZW5hbnRJZCI6Ii5zYW5tYXJjb3NkcHd0eGNwIiwibmFtZSI6IlNhbiBNYXJjb3MgRFBXLCBUWCAoQ1ApIC0gV2F0ZXIgU2Vuc29yIEludGVncmF0aW9uIiwic3ViIjoiOTg5MjIxIiwidGVuYW50SWQiOiIyMzc4IiwianRpIjoiQjY5RkQzQzJCRkJBQzc2NzY3MzFFQTIzNkI5NTQxQTkifQ.wrnq0dSQIV6GuGXj9WcgydwHLlRoVCsMudzyHSqbEW9LAtXaZ-VPpMbGnNMJrX6nkxABHxEBlmPFgd1qPskXxnk0U3zVMT2TjcdLonNNe4YZUVcklaNfsnmaWsE_NFkSxmjElWuQChDTie1SNkUWEp7acgdZHo7YdMycSs3zyegkD2bci-uN4gS21dMTOUfcOtGGRXTyHJOzyrHfPAvJntRaAon53s1MKPYNXFVIdYcPmBciSp19YfVrnN9AJ0HZ27NynHkJh_9_nUYQlrCc0d9is4512FgN4nte8Tn8Po_yUzOqwircMkqG1eRaJsMiMLibf1SQSDza21oYpoIIKk-QsoMJVbwb5r3HmfzyeGYocJuOzjK3JtoCDN-uZTr-Ekh-8GlHiRqexQN48eK1OXf9wYEQaYoouVuo_AwAsozlidtewsWM2I3hJgN40mmqmnSqiLiaery75lljB7DpaPptVwU2FCUNk2aBZj6Pn9BwMS0SOjuugg31lRhCWXsnrgM8y1Rc2aC-ZSq90sssmxz3KvKKuiHBJl36QabCBKDkpAulVVse0Uvz3xH_eWnb8_AG8kxKCdQQSVWM9xVyz5-_rAQtOQhaPUcSuDVZ5HdFC9WiCpkVwqbn0iEqM3-oYYTFPqQVohi7ZUDuhNANXVO0ENOp_RCg4mRPtSH5pD4"
)

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