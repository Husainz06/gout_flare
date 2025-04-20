import streamlit as st

st.title("Neural Network Approach (Pytorch)")
st.write("A neural network is a machine learning model that makes decisions \
         in a manner similar to the human brain, using processes that emulate \
         the way biological neurons interact to recognize patterns, evaluate options, and reach conclusions.\
         Each neural network is composed of layers of nodes, or artificial neurons: an \
         input layer, one or more hidden layers, and an output layer. Nodes \
         are interconnected, and each has an associated weight and threshold. When the output \
         of a node exceeds its threshold, the node is activated and transmits data to the next \
         layer. If the threshold is not met, no data is passed forward. Below is an illustration of the basic idea of neural networks.")
st.image("Media/nn_illusration.png", width=550)

st.write("Neural networks depend on training data to learn and refine their accuracy over time. \
         Once optimized, they serve as powerful tools in computer science and artificial intelligence, \
         capable of rapidly classifying and clustering data. [12] We used the Pytorch library to implement \
         the neural network model. Below are the results we got from the neural network model.")
st.image("Media/pytorch_report.png", width=450)
st.image("Media/pytorch_cm.png", width=450)