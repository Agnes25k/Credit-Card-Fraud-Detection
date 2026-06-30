\# 💳 Credit Card Fraud Detection Using Machine Learning



\## 📌 Project Overview



This project focuses on detecting fraudulent credit card transactions using Machine Learning algorithms. The dataset is highly imbalanced, so multiple models and evaluation techniques were used to handle class imbalance and improve detection performance.



The goal is to correctly identify fraudulent transactions while minimizing false positives.



\---



\## 📊 Dataset Information



\- Dataset: PaySim / Credit Card Fraud Dataset

\- Type: Simulated financial transactions

\- Total Transactions: \~284,807

\- Fraud Cases: Very rare (\~0.1–0.2%)

\- Highly imbalanced dataset



> Note: Dataset is not included in this repository due to size limitations.



\---



\## 🔍 Statistical Analysis



\- The dataset is highly imbalanced with fraud cases forming a very small percentage.

\- Transaction amounts are highly skewed.

\- Fraud cases show different statistical behavior compared to legitimate transactions.

\- No single feature is enough to detect fraud effectively.



👉 Because of imbalance, accuracy is NOT a reliable metric. Instead, Precision, Recall, F1-score, and ROC-AUC are used.



\---



\## ⚙️ Project Workflow



1\. Data Loading

2\. Exploratory Data Analysis (EDA)

3\. Data Preprocessing

4\. Handling Class Imbalance

5\. Model Building

6\. Model Evaluation

7\. Hyperparameter Tuning

8\. Final Model Selection



\---



\## 🤖 Machine Learning Models Used



\- Logistic Regression

\- Random Forest

\- XGBoost

\- Tuned Random Forest

\- Tuned XGBoost



\---



\## 📈 Model Performance



| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |

|------|----------|-----------|--------|----------|----------|

| Logistic Regression | 95.40% | 2.62% | 95.80% | 5.10% | 99.17% |

| Random Forest | 99.58% | 23.01% | 96.47% | 37.16% | 99.89% |

| XGBoost | 99.39% | 17.47% | 99.57% | 29.73% | 99.98% |

| Tuned Random Forest | \*\*99.97%\*\* | \*\*96.02%\*\* | 79.31% | \*\*86.87%\*\* | 99.85% |

| Tuned XGBoost | 99.96% | 79.84% | \*\*88.44%\*\* | 83.92% | 99.90% |



\---



\## 🏆 Best Model



The \*\*Tuned Random Forest\*\* was selected as the final model because it achieved:



\- Highest Precision (96.02%)

\- Best F1 Score (86.87%)

\- Strong balance between precision and recall



\---



\## 🛠️ Technologies Used



\- Python 🐍

\- Pandas

\- NumPy

\- Scikit-learn

\- XGBoost

\- Matplotlib

\- Seaborn

\- Joblib

\- Git \& GitHub



\---



\## 📁 Project Structure



```

project/

│

├── app.py

├── fraud\_detection\_eda.ipynb

├── fraud\_detection\_model.ipynb

├── fraud\_detection\_pipeline.pkl

├── requirements.txt

├── README.md

└── .gitignore

```



\---



\## 🚀 How to Run This Project



\### 1. Clone the repository

```bash

git clone https://github.com/Agnes25k/Credit-Card-Fraud-Detection.git

```



\### 2. Move into project folder

```bash

cd Credit-Card-Fraud-Detection

```



\### 3. Install dependencies

```bash

pip install -r requirements.txt

```



\### 4. Run Jupyter notebooks or Python scripts

```bash

jupyter notebook

```



or



```bash

python app.py

```



\---



\## 📌 Key Insights



\- Dataset is extremely imbalanced → accuracy is misleading

\- Ensemble models perform better than simple models

\- Tuning significantly improves precision and recall balance

\- XGBoost achieved highest recall

\- Random Forest achieved best overall balance



\---



\## 🔮 Future Improvements



\- Deploy using Streamlit web app

\- Real-time fraud detection system

\- Feature engineering improvements

\- Deep learning models

\- Cloud deployment (AWS / Render / Streamlit Cloud)



\---



\## 👩‍💻 Author



\*\*Agnes\*\*



\---



\## ⭐ Support



If you like this project, give it a ⭐ on GitHub!

