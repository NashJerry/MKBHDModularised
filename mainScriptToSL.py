import warnings
# Suppress all warnings
warnings.filterwarnings('ignore')
from processVideos.getVideoDetails import videoMetaData
from transcriptProcessing.transcript import punctuate_transcripts_in_dataframe
from sentimentXthemes.reviewTheme import getThemeAndSentiment, flattenPredictions

def assessLinks(linkOrLinks, Brand=None, Phone=None):
    print("Evidently I am assessing.")
    metadata = videoMetaData(linkOrLinks)
    punctuatedTranscript = punctuate_transcripts_in_dataframe(metadata)
    punctuatedTranscript['semantically_replaced_transcript']  = punctuatedTranscript['semantically_replaced_transcript'].astype(str)
    punctuatedTranscript['predictions'] = punctuatedTranscript['semantically_replaced_transcript'].apply(getThemeAndSentiment)
    finalDF = flattenPredictions(punctuatedTranscript)
    print(finalDF)
    if Brand and Phone is None:
        pass    
    else :
        finalDF['Brand'] = Brand
        finalDF['Phone'] = Phone
    #finalDF.to_excel(r'C:\Users\panas\OneDrive\Desktop\DataScience\PersonalProjects\MKBHDModularised\output.xlsx')
    print("I gave the label bills bills bills.")
    return finalDF

#assessLinks('https://www.youtube.com/watch?v=vZr18_aOY6I', Brand='iPhone', Phone ='x')

import streamlit as st

linkColumn, brandColumn, makeColumn = st.columns(3)

with linkColumn:
    linkInput = st.text_input(
        "Enter some text 👇",
        placeholder= "Insert Your Link To An MKBHD Video Here!"
    )

with brandColumn:
    brandInput = st.text_input(
        "Enter some text 👇",
        key="Brand",
        placeholder= "Whats the phone brand?"
    )
with makeColumn:
    makeInput = st.text_input(
        "Enter some text 👇",
        key="make",
        placeholder= "Whats the make??"
    )

# Button to trigger the function
if st.button('Assess Link'):
    # Call your function with the user inputs
    assessLinks(linkInput, Brand=brandInput, Phone=makeInput)

#assessLinks('https://www.youtube.com/watch?v=vZr18_aOY6I', Brand='iPhone', Phone ='x')

