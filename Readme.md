## 🧠 Personality Prediction: Introvert vs Extrovert Classifier

This project uses behavioural traits to classify individuals as **Introverts** or **Extroverts** using Machine Learning. The dataset is sourced from Kaggle and explores correlations between social habits and personality types.

---

## 🔍 Problem Statement

Can we predict whether a person is an introvert or extrovert based on their responses to behavioural questions?

---

## 🧰 Tools & Technologies
- Python (pandas, seaborn, scikit-learn, xgboost)
- Jupyter Notebooks
- Streamlit (optional deployment)
- Matplotlib

---

## 📦 Dataset

- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)
- **Size**: 2,900 entries, 7 features + target label
- **Features**:
  - Time Spent Alone
  - Stage Fear
  - Social Event Attendance
  - Going Outside
  - Drained After Socializing
  - Friends Circle Size
  - Post Frequency

---

## 🔬 EDA Highlights

- The dataset is well-balanced between Extroverts (51.4%) and Introverts (48.6%)
- Extroverts tend to have larger friend circles and attend more social events
- Missing values were minimal and handled via median/mode imputation

---

## 🤖 Model Performance

| Model              | Accuracy | Precision | Recall | F1-Score |
|-------------------|----------|-----------|--------|----------|
| Logistic Regression (Unscaled) | 92% | 0.91–0.93 | 0.92–0.93 | 0.92 |
| Logistic Regression (Scaled)   | 92% | 0.91–0.93 | 0.92–0.93 | 0.92 |
| Random Forest       | 92% | 0.91–0.93 | 0.91–0.92 | 0.92 |
| XGBoost             | 92% | 0.90–0.93 | 0.91 | 0.91–0.92 |

---


## 🔧 Run Locally

# Clone the repo
git clone https://github.com/sonofgrace/extrovert-introvert-classifier
cd extrovert-introvert-classifier

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/app.py

---

## ✅ Conclusion

- All models performed consistently well
- Random Forest and Logistic Regression are ideal for deployment due to their balance and simplicity
- Feature importance shows `Friends Circle Size`, `Event Attendance`, and `Social Draining` are highly predictive

---

## 🚀 Future Work

- Expand the dataset with more demographic or psychometric features
- Try deep learning models or NLP integration for open-ended traits

---

 ## 🙋🏽‍♂️ Author

**Dr. Benedict Nweke  
Aspiring Data Scientist & Medical Doctor  
📫 [LinkedIn Profile]: https://www.linkedin.com/hephzyben 
📂 [Project Repository]: (https://github.com/sonofgrace/extrovert-introvert-classifier)
