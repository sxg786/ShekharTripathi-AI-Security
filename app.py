from src.parser import parse_auth_log
from src.features import create_features
from src.model import train_model
from src.detector import detect_anomalies

# Load logs
logs = parse_auth_log("logs/auth.log")

# Feature creation
features = create_features(logs)

# Train model
model = train_model(features)

# Detect anomalies
anomalies = detect_anomalies(model, features)

print("Detected Anomalies:")
for a in anomalies[:20]:
    print(a)
