# 📧 Spam Email Classification App
## 🚀 Overview
The Email Spam Classification App is a machine learning project designed to classify emails as Spam or Ham (Not Spam) using a Naive Bayes Classifier. Built with Streamlit, the app provides a simple and interactive interface for users to input email content and receive instant classification results.

## ✨ Features
- 🌟 **Real-time Spam Detection**: Classifies emails as spam or ham instantly.
- 📊 **Visualization**: Displays a bar plot showing the distribution of spam vs ham emails.
- 📄 **Dataset Preview**: Offers a quick look at the raw dataset used for training.
- 🎨 **Interactive UI** — Built with Streamlit for a smooth user experience.
  
## 🏃 How to Run the App
1. **Clone the Repository**:
- git clone https://github.com/your-username/your-repo.git
- cd your-repo
2. **Install the Required Libraries**:
Ensure you have Python installed, then run:
- pip install -r requirements.txt
3. **Run the Streamlit App**:
streamlit run spamDetector.py
4. **View the App**:
The app will open automatically in your browser at:
http://localhost:8501

## 🧪 Dataset
The app uses a Spam/Ham Dataset (spam.csv), which contains labeled email data:
- ham — Non-spam emails (label = 0)
- spam — Spam emails (label = 1)
The preprocessing steps include:
- Dropping unnecessary columns
- Converting labels (ham/spam) to numeric values (0/1)
  
## ⚡ Model Used
- Naive Bayes Classifier (from Scikit-learn)
- The trained model (spam.pkl) and vectorizer (vectorizer.pkl) are loaded using pickle.

## 🏗️ Project Structure
```
📁 EMAIL-SPAM-DETECTION
│-- 📊 spam.csv                  # Dataset used for training and testing
│-- 📦 spam.pkl                  # Trained Naive Bayes model
│-- 📦 vectorizer.pkl            # Fitted CountVectorizer for text transformation
│-- 🏃 spamDetector.py           # Streamlit app for email classification
│-- 📓 email-spamDetector.ipynb # Jupyter notebook for model training and evaluation
│-- 📜 requirements.txt          # List of required libraries for the project
│-- 📄 README.md                 # Project documentation and usage instructions
```
## 🚀 Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- Matplotlib & Seaborn (for visualization)
## 🏷️ How to Use the App
- Input email text in the text area under Email Classification.
- Click on the Classify button.
- The app will display whether the email is Spam or Ham.
- Use the sidebar to view the dataset and plot the spam vs ham distribution.
 ## 🤝 Contributing
Feel free to fork the project, create feature branches, and submit pull requests.
