import streamlit as st

st.title("Gout Flare Prediction")

st.subheader("Background")
st.write("Gout flare is a form of arthritis that is a very common and complex \
         one and it can affect any individual. The symptoms include severe attacks \
         of pain, swelling, redness and tenderness in one or more joints.[1]\
          Gout symptoms are recurring episodes of severe pain affecting patients ( called gout flare ) \
         and mostly in the big toe but can affect other joints like knees, ankles, wrists, and elbows. \
         The main reason of that is the uric acid buildup in the body [2].  Uric acid is a product of \
         purine metabolism generated during the breakdown of nucleic acids (DNA and RNA) and ATP, and \
         uric acid can also be generated from proteins [3]. It is one of the most common types of arthritis \
         as it affects about 4% of adults and about 9,000,000 individuals in the United States alone[4] and \
         with that number doubling in the last 30 years ")

st.image("Media/gout.png", caption="Gout Flare",width=400)
st.write("Gout has strong associations with hypertension, obesity, diabetes, and renal and cardio-vascular \
         disease, in addition to accelerated mortality. Population data suggest that gout is significantly \
         under-treated, with urate-lowering therapy (the cornerstone of appropriate gout management) either \
         frequently not used or underdosed if used [6]. ")

st.subheader("Problem Statement")
st.write("This project is a part of a research project aiming at predicting and classifying gout flares based  \
on the gene expression counts in the patient’s blood sample. At the time of writing this report, there is no current  \
approach or method to accomplish this, which means that there is no current baseline to base this approach’s performance \
         on. For that reason, we implemented several other approaches and compared them to the neural network approach to \
         compare the accuracy in the prediction. \
Currently, we were able to create a neural network model using PyTorch that was able to predict gout flare \
         with a good accuracy compared to other regression and prediction methods. More information about the \
         neural network model and the other approaches is detailed in the following sections.\
")