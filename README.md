# 🌍 Life Expectancy & Sleep Duration Predictor

A Machine Learning web app built with **Streamlit** to predict an individual's life expectancy and estimate total lifetime sleep hours based on healthcare and lifestyle indicators.

---

## 📊 Features

- Predict life expectancy based on 10 key health & economic factors
- Calculate total lifetime sleep based on average 8 hours/day
- Clean and interactive Streamlit interface
- Preprocessed data using `StandardScaler`
- Model built with `Linear Regression` from scikit-learn

---

## 📁 Project Structure

```
life_expectancy_project/
│
├── app/
│   ├── main.py           # Streamlit UI app
│   └── utils.py          # Helper function for sleep calculation
│
├── data/
│   └── Life Expectancy Data.csv   # Dataset
│
├── models/
│   ├── model.pkl         # Trained ML model
│   └── scaler.pkl        # Scaler used for preprocessing
│
├── data_preparation.py   # Loads and preprocesses data
├── train_model.py        # Trains and saves the ML model
├── requirements.txt      # Project dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/life-expectancy-predictor.git
cd life-expectancy-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the Dataset

Ensure the file `Life Expectancy Data.csv` is placed inside the `data/` folder.

---

## 🚀 Train the Model

If you want to retrain the model:

```bash
python train_model.py
```

This will generate:

- `models/model.pkl` – trained Linear Regression model
- `models/scaler.pkl` – data scaler for consistent input

---

## 🖥️ Run the Streamlit App

```bash
python -m streamlit run app/main.py
```

---

## 📸 App Preview

> Input sliders collect health/lifestyle indicators, and output displays:
>
> - 📈 **Predicted Life Expectancy (years)**
> - 🛌 **Total Lifetime Sleep (hours)**

---

## 🛠️ Built With

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 📌 Future Enhancements

- Add age, gender, and country filters
- Use XGBoost or RandomForest for better accuracy
- Deploy on Streamlit Cloud / HuggingFace Spaces

---

## 📬 Contact

Developed by **[Rohan Suryawanshi]**\
📧 [[rohansurya316@gmail.com](mailto\:rohansurya316@gmail.com)]\
🌐 [[https://www.linkedin.com/in/rohan-suryawanshi-0980792a3/](https://www.linkedin.com/in/rohan-suryawanshi-0980792a3/)]

---

## ⭐ License

This project is licensed under the [MIT License](LICENSE).

