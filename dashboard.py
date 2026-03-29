import plotly.express as px
from flask import Flask, render_template
import pandas as pd
from src.parser import parse_auth_log
from src.features import create_features
from src.model import train_model
from src.detector import detect_anomalies

app = Flask(__name__)

@app.route("/")
def index():
    try:
        logs = parse_auth_log("logs/auth.log")
        features = create_features(logs)

        model = train_model(features)
        anomalies = detect_anomalies(model, features)

        df = pd.DataFrame(logs)

        failed_logins = df['failed_login'].sum()
        success_logins = df['success_login'].sum()
        sudo_usage = df['sudo_usage'].sum()

        # Graph
        fig = px.line(df['failed_login'], title="Failed Login Trend")
        graph_html = fig.to_html(full_html=False)

        return render_template(
            "index.html",
            failed=failed_logins,
            success=success_logins,
            sudo=sudo_usage,
            anomalies=len(anomalies),
            anomaly_list=anomalies[:20],
            graph=graph_html
        )

    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
