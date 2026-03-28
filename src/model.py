from sklearn.ensemble import IsolationForest

def train_model(features):
    model = IsolationForest(contamination=0.05)
    model.fit(features)
    return model
