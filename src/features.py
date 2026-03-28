import pandas as pd

def create_features(logs):
    df = pd.DataFrame(logs)

    features = pd.DataFrame()
    features['failed_login'] = df['failed_login']
    features['success_login'] = df['success_login']
    features['sudo_usage'] = df['sudo_usage']

    return features
