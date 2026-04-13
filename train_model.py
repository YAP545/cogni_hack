import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder

print("🚀 Starting SureScore AI Training Pipeline...")

# 1. Load Data (Replace with your actual CSV file name)
df = pd.read_csv('health_insurance_data.csv')

# 2. Preprocess
le = LabelEncoder()
df['risk_level_encoded'] = le.fit_transform(df['risk_level'])
X = df.drop(columns=['risk_level', 'risk_level_encoded', 'Customer ID'], errors='ignore')
y = df['risk_level_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Hyperparameter Tuning
xgb_model = XGBClassifier(eval_metric='mlogloss')
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2]
}

print("⚙️ Tuning model parameters. Please wait...")
random_search = RandomizedSearchCV(xgb_model, param_grid, n_iter=10, scoring='accuracy', cv=3, random_state=42)
random_search.fit(X_train, y_train)

best_model = random_search.best_estimator_
print(f"✅ Best Accuracy Achieved: {random_search.best_score_:.4f}")

# 4. Save the Final Models
joblib.dump(best_model, 'optimized_health_risk_model.pkl')
joblib.dump(le, 'health_label_encoder.pkl')
print("💾 Models successfully saved as .pkl files!")
