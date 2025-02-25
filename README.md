# 📧 Spam Email Classification App
This is a Machine Learning Web Application built with Streamlit to classify emails as Spam or Ham. The app uses a Naive Bayes classifier trained on a labeled dataset and allows users to input email content to check whether it is spam or not.

## ✨ Features
- 🌟 **Real-time Spam Detection**: Classifies emails as spam or ham instantly.
- 📊 **Visualization**: Displays spam vs ham distribution.
- 📚 **Inputs**: Text area for user input with placeholder text.
## 🏃 How to Run the App
1. **Clone the Repository**:
git clone https://github.com/your-username/your-repo.git
cd your-repo
2. **Install the Required Libraries**:
Ensure you have Python installed, then run:
pip install -r requirements.txt
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

## 📦 Project Structure
📁 EMAIL-SPAM-DETECTION
│-- spam.csv                  # Dataset used for training
│-- spam.pkl                  # Trained Naive Bayes model
│-- vectorizer.pkl            # Fitted CountVectorizer
│-- spamDetector.py           # Streamlit app
│-- email-spamDetector.ipynb # Jupyter notebook for model training
│-- requirements.txt          # Required libraries
│-- README.md                 # Project documentation
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
