import streamlit as st

st.title("Naïve Bayes")
st.write("This is a supervised machine learning algorithm that is used for classification. \
         It uses the concepts of probability to perform classification tasks. Naïve Bayes is \
         part of a family of generative learning algorithms, meaning that it seeks to model \
         the distribution of inputs of a given class or category. Unlike discriminative \
         classifiers, like logistic regression, it does not learn which features are most \
         important to differentiate between classes. [8]. Below are the results of Naïve Bayes model.")
st.image("Media/naive_bayes_report.png", width=450)
st.image("Media/naive_bayes_cm.png", width=450)
