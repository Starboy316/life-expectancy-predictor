# data_preparation.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_clean_data():
    # Load dataset
    df = pd.read_csv('data/Life Expectancy Data.csv')

    # Drop rows with missing values
    df = df.dropna()

    # Encode 'Status' column (Developed = 1, Developing = 0)
    df['Status'] = df['Status'].map({'Developed': 1, 'Developing': 0})

    # Select only the 10 features used in the app
    selected_features = [
    'Adult Mortality',
    'infant deaths',
    'Alcohol',
    ' BMI ',  # with spaces
    'under-five deaths ',  # with space
    'Polio',
    'Total expenditure',
    'Status',
    'Income composition of resources',
    'Schooling'
]

    df = df[selected_features + ['Life expectancy ']]

    # Define features and target
    X = df[selected_features]
    y = df['Life expectancy ']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, scaler
