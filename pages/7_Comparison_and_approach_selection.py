import streamlit as st

st.title("Comparison and Approach Selection")
st.write("We compared the neural network to the other approaches we implemented as baselines to get the most accurate approach.\
         We used confusion matirces to evaluate and compare the performance of the models. \
         The confusion matrix is a summary of prediction results on a classification problem. \
         It is a table with four different combinations of predicted and actual values. \
         It is a useful tool for visualizing the performance of a classification model \
         as it allows us to see how many instances were classified correctly and how many were misclassified. \
         It is a great way to evaluate the performance of a classification model, \
         and provides a clear picture of how well the model is performing and where it is making mistakes.\
         Below is a figure that shows the confusion matices of the different approaches we implemented.")
st.image("Media/cm_all.png", width=800)

st.write("As we can see from the figure above, the neural network model outperformed all the other models we implemented. \
         Therefore, we selected the neural network model as our final model. ")