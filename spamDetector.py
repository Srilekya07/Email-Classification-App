import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 # Load the trained model and vectorizer
@st.cache_data #to load the model and dataset once for better performance.
def load_model():
    model = pickle.load(open('spam.pkl','rb'))
    vectorizer = pickle.load(open('vectorizer.pkl','rb'))
    return model,vectorizer

# Load and preprocess the spam dataset.
@st.cache_data
def preprocess_data():
    data = pd.read_csv("spam.csv", encoding="latin-1")
    data = data.iloc[:, [0, 1]]  # Keep only 'class' and 'message'
    data.columns = ['class', 'message']
    data['class'] = data['class'].map({'ham': 0, 'spam': 1})
    return data

# Spam vs Ham Distribution
def plot_distribution(data):
    st.subheader("📊 Spam vs Ham Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='class', data=data, palette='pastel', ax=ax)
    ax.set_xticklabels(['Ham', 'Spam'])
    ax.set_xlabel('Email Class')
    ax.set_ylabel('Count')
    st.pyplot(fig)


# Main Streamlit app
def main():
    st.title("📧 Spam Email Classification App")
    st.write("This is a Machine Learning application using Naive Bayes to classify emails as spam or ham.")

    # Load model, vectorizer, and data
    model, vectorizer = load_model()
    data = preprocess_data()

    # Sidebar
    st.sidebar.header("About")
    st.sidebar.write("Built using Streamlit, Scikit-learn, and Pandas.")
    st.sidebar.title("Options")
    
    if st.sidebar.checkbox("Show Dataset Preview"):
        st.subheader("Dataset Preview")
        st.write(data.head(10))

    if st.sidebar.checkbox("Show Spam vs Ham Distribution"):
        plot_distribution(data) 

    st.sidebar.markdown("---")
    

    # Classify user input
    st.subheader("Email Classification")
    user_input = st.text_area("Enter the email content to classify:", height=200)
    
    if st.button("Classify"):
        if user_input.strip() != "":
            vectorized_data = vectorizer.transform([user_input]).toarray()
            result = model.predict(vectorized_data)[0]

            # Display result
            st.subheader("📢 Classification Result")
            if result == 1:
                st.error("🚨 The email is **Spam**.")
            else:
                st.success("✅ The email is **Not Spam (Ham)**.")
        else:
            st.warning("⚠️ Please enter some email text for classification.")
    st.sidebar.markdown("---")
    st.sidebar.info("📬 This app uses a trained Naive Bayes classifier to detect spam emails.")

if __name__ == "__main__":
    main()

    
   

