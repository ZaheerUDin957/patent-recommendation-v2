import streamlit as st
import pandas as pd
import requests
import json

endpoint="https://patent-recommendation-542808340038.us-central1.run.app/query"

st.set_page_config(layout="centered")

st.title("Trademark System")

text = st.text_area("Search query")

# Create a container to center the button
col1, col2, col3 = st.columns([2.3,2,1])

with col2:
    # Centered submit button
    submit_button = st.button('Submit')

if submit_button:
    with st.spinner('Generating Response..'):
        # Prepare the payload
        payload = {"query": text}
        
        # Make the POST request
        response = requests.post(endpoint, json=payload)
        data = response.content
        
        data_str = data.decode('utf-8')

        data = json.loads(data_str)
        data = data["data"]
        
        # Prepare lists for DataFrame
        class_names = []
        class_ids = []
        
        # Iterate through the data dictionary
        for class_name, class_data in data.items():
            class_names.append(class_name)
            class_ids.append(class_data["class id"])  # Access the "class id" field
        
        # Create a DataFrame with Class Name and Class ID
        df = pd.DataFrame({
            "Class Name": class_names,
            "Class ID": class_ids
        })
        st.dataframe(df.reset_index(drop=True), use_container_width=True)
