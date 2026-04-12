import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

def train_and_save_xgb(csv_file, model_name, encoder_name):
    print(f"Training XGBoost model for {csv_file}...")
    
    # 1. Load the data
    df = pd.read_csv(csv_file)
    
    # 2. Separate Features (X) and Target (y)
    X = df.drop(columns=['risk_level'])
    y = df['risk_level']
    
    # 3. XGBoost needs numbers, so convert 'Low', 'Medium', 'High' to 0, 1, 2
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    print("Class Mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
    
    # 4. Split into Training and Testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    # 5. Initialize and Train the XGBoost Model
    model = xgb.XGBClassifier(eval_metric='mlogloss', random_state=42)
    model.fit(X_train, y_train)
    
    # 6. Check the Model's Accuracy
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy for {model_name}: {accuracy * 100:.2f}%\n")
    
    # 7. Save the Model and the Encoder (so you can use them in your web app later)
    joblib.dump(model, f'{model_name}.pkl')
    joblib.dump(le, f'{encoder_name}.pkl')
    print(f"Saved {model_name}.pkl and {encoder_name}.pkl\n")

# Run the function on both datasets
train_and_save_xgb('vehicle_insurance_data.csv', 'vehicle_xgb_model', 'vehicle_encoder')
train_and_save_xgb('health_insurance_data.csv', 'health_xgb_model', 'health_encoder')
