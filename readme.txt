Initial Python Script

Monitored stream gauge data from an XML feed.
Basic logic to read and process water level data.
Flood Detection Logic

Added gauge-specific tolerances and thresholds.
Script now detects when water levels indicate possible flooding.
Alert Integration

Connected to the Konexus API.
Implemented OAuth2.0 client credentials flow for secure authentication.
Automated sending of flood alerts to Konexus when thresholds are exceeded.
Code Modularization

Split code into modules for clarity and maintainability:
main.py: Orchestrates the app.
api.py: Handles API communication and authentication.
alerts.py: Contains flood detection logic.
storage.py: Manages persistent alert state in a JSON file.
config.py: Centralizes configuration and environment variables.
Packaging for GitHub

Cleaned up code and requirements.
Created a requirements.txt for dependencies.
Set up SSH keys and pushed the project to GitHub.
Cloud Deployment (Render)

Created a new Render service, connected to GitHub.
Set environment variables for secrets.
Added a persistent disk for the JSON file.
Deployed the app, ensuring alerts and state persist across restarts.