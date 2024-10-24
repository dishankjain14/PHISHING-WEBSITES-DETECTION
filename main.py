import streamlit as st
import joblib
import pandas as pd
from urllib.parse import urlparse

# Load the trained model
model = joblib.load('phishing_model.pkl')

# Function to extract features from a given URL
def extract_url_features(url):
    features = {}
    features['length_url'] = len(url)
    features['nb_dots'] = url.count('.')
    features['nb_hyphens'] = url.count('-')
    features['length_hostname'] = len(urlparse(url).netloc)
    features['nb_qm'] = url.count('?')
    features['nb_and'] = url.count('&')
    features['nb_eq'] = url.count('=')
    features['https_token'] = 1 if 'https' in url else 0
    features['ratio_digits_url'] = sum(c.isdigit() for c in url) / len(url)
    features['ratio_digits_host'] = sum(c.isdigit() for c in urlparse(url).netloc) / len(urlparse(url).netloc)
    features['domain_registration_length'] = 0  # Placeholder (adjust if domain info is available)
    features['domain_age'] = 0  # Placeholder (adjust if domain info is available)
    features['web_traffic'] = 0  # Placeholder (adjust if traffic data is available)
    features['dns_record'] = 0  # Placeholder (adjust if DNS info is available)
    features['google_index'] = 1 if 'google' in url else 0
    features['page_rank'] = 0.5  # Placeholder (adjust if page rank data is available)
    features['phish_hints'] = 1 if 'phish' in url.lower() else 0
    features['suspecious_tld'] = 1 if url.endswith('.xyz') else 0  # Example for suspicious TLDs
    features['external_favicon'] = 0  # Placeholder (adjust if favicon info is available)
    return features

# Streamlit app interface
st.title("Phishing Website Detector")
url = st.text_input("Enter the URL of the website:")

if st.button("Check"):
    if url:
        # Extract features from the input URL
        features = extract_url_features(url)
        features_df = pd.DataFrame([features])
        
        # Make prediction
        prediction = model.predict(features_df)[0]
        
        # Display the result
        if prediction == 1:  # Assuming '1' means phishing
            st.error("This website is likely a phishing website.")
        else:
            st.success("This website is likely legitimate.")
    else:
        st.warning("Please enter a URL to check.")
