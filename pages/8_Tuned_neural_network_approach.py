import streamlit as st

st.title("Final and Neural Network Approach")
st.write("We need to ensure that we get reliable predection results, first, we believe that we need to perform k-fold cross \
         validation to ensure that the results we got are reliable results. The second thing is that we believe that we need \
         to regenerate the significant genes set for each fold to ensure that the test set is not included when we determine \
         the significant genes. This will ensure that we only rely on the training set to train the model and that the test \
         set does not influence the learning process.")
st.subheader("K-fold cross validation")
st.write("We implemented a 10-fold cross validation so that we train, test, and validate 10 times and then take the \
         average of the accuracy as our final result. In each fold, we performed a t-test to determine the significant \
         genes for that fold based only on the training data for that fold. By doing so, although the performance \
         slowed down quite a bit, we were able to isolate test sets from training sets during the learning process \
         and during feature selection.")
st.subheader("Avoiding Overfitting")
st.write("To avoid overfitting, we introduced the validation curve and early stopping. The idea is to monitor the \
         learning loss and the validation error. As long as both are going down, then the model is making progress \
         in learning. When the model reaches a point where the loss curve is going down while the validation curve \
         starts going up, this indicates that the model started to overfit and that the learning needs to stop for \
         that fold. In our model, we set a patience of 50, meaning that the model will wait for 50 iterations to see \
         if the validation curve goes back down after starting to go up. If it does not, then the learning will stop, \
         and we will move to the next fold. A sample run is shown in the figure below:")
st.image("Media/cross_validation.png", width=550)
st.write("As can be seen from left plot on figure 8 above, at first, both curves were decreasing. However, around \
         iteration 660, the learning stopped, and the validation stopped since before that, the learning loss was \
         decreasing but the validation error curve stopped decreasing and it was about to go up. The validation error \
         increase is even more visible in the right plot at around iteration 248.")
st.subheader("Overall Accuracy")
st.write("After testing the enhanced model, we were able to get an accuracy of around 63.3% in terms of prediction \
         accuracy. This is a very good result considering the complexity of the problem and the validation folds we \
         have. The figures below show the prediction’s overall accuracy.")
st.image("Media/overall_cm.png", width=550)
st.image("Media/overall_bar.png", width=550)
st.write("As can be seen from the figures above, although the model has some false predictions, we can clearly see \
         that the number of correct predictions surpasses the number of incorrect ones. We wre able to achieve an accuracy\
         of 63.3% which is a very good result considering the complexity of the problem and the validation folds we \
         have. ")
st.write("For future work, we plan on tuning the network to achive even better results. We also plan on using HPCC to run\
         parllelized scripts with different hyperparameters to find the best hyperparameters for our model.")
