def detect_anomalies(model, features):
    predictions = model.predict(features)

    results = []
    for i, pred in enumerate(predictions):
        if pred == -1:
            results.append((i, "ANOMALY"))

    return results
