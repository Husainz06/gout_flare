import streamlit as st

st.title("Datasets")
st.write("We used multiple data files. Each of these data files contained a part that is necessary for the analysis. \
         We used blood samples data, significant genes data, gene expression counts for each sample, and then we \
         created a processed data file out of these to be used for our analysis.")
st.subheader("Patient Blood Samples")
st.write("Samples are withdrawn from participants who were originally participating to research the efficacy \
         of some gout medication. This dataset originally has data for patients who were randomly assigned \
         to allopurinol or febuxostat in this 72-week trial, with doses titrated to target serum urate. The \
         trial had three phases: titration (weeks 0 to 24), maintenance (weeks 25 to 48), and observation \
         (weeks 49 to 72). The original purpose of this was to check the efficacy effects of these medications \
         on gout flares. A sample of the dataset is shown in the figure below.")
st.image("Media/blood_samples.png", width=450)
st.subheader("Gene Expression Data")
st.write("The raw data has sample IDs, gene IDs and gene expression counts for all samples that are analyzed. \
         The organization of the original raw data file had columns to denote samples, rows for genes and the \
         cells contain normalized gene expression count. A sample of the raw data file is shown below.")
st.image("Media/gene_expression.png", width=650)
st.subheader("Significant Genes Datasdet")
st.write("One of the data files that we have contains an analysis of the genes that uses p-value to determine \
         the significance of the gene in determining flare or no flare. This file helps us eliminate the \
         unnecessary genes during our computation. The file simply has all gene IDs along with p-values for \
         those IDs denoting the significance of the gene in gout flare determination.")
st.subheader("Processed Data")
st.write("For our research, we have only selected the data on week 48 as at that time, almost all patients \
    were not on any medication as per the researchers who originally collected the data. The first step was to \
    transform the raw dataset to have columns representing gene IDs and rows representing sample IDs. \
    The next step was to filter the samples based on the week in which they were collected. For that, we \
    combined data from the metadata file and the raw data file and extracted week 48’s data. The next step \
        was to filter out the gene IDs that have very small count after normalization as these will not help \
        in the prediction. We set up a threshold of 5, meaning if the count is under 5, we removed that \
        gene ID. We also removed genes that have a constant count across all samples as these do not \
        contribute to out analysis. To accomplish this, we checked columns with zero standard deviation \
        and removed those columns. Before performing this filtration, we had 62,754 gene IDs. This \
        number became 26,707 gene IDs after filtration. A sample of the processed dataset is shown below.")
st.image('Media/processed_data.png', width=750)