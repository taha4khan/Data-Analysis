import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample dummy data
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [23, 45, 31, 35, 50, 23, 21, 30, 28, 40],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'ProductPurchased': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'A', 'C'],
    'PurchaseAmount': [120, 200, 150, 220, 300, 130, 250, 210, 170, 280],
    'PurchaseFrequency': [5, 3, 4, 2, 1, 6, 1, 2, 5, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Preprocessing
label_encoder_gender = LabelEncoder()
label_encoder_product = LabelEncoder()
df['Gender'] = label_encoder_gender.fit_transform(df['Gender'])
df['ProductPurchased'] = label_encoder_product.fit_transform(df['ProductPurchased'])

# Feature selection
features = ['Age', 'Gender', 'PurchaseAmount', 'PurchaseFrequency']
X = df[features]
y = df['ProductPurchased']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
report = classification_report(y_test, y_pred, target_names=label_encoder_product.classes_)
print(report)

# Sample prediction
new_customer = pd.DataFrame({
    'Age': [29],
    'Gender': label_encoder_gender.transform(['Female']),
    'PurchaseAmount': [180],
    'PurchaseFrequency': [3]
})

predicted_product = model.predict(new_customer)
predicted_product_label = label_encoder_product.inverse_transform(predicted_product)
print(f"The predicted product for the new customer is: {predicted_product_label[0]}")
