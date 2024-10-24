# PHISHING-WEBSITES-DETECTION
PHISHING WEBSITES DETECTION SYSTEM USING MACHINE LEARNING BASED MODEL

Phishing Website Detection Using Machine Learning
This project aims to detect phishing websites using machine learning techniques. The model uses a variety of URL-based features and webpage characteristics to determine whether a given URL is legitimate or phishing. The project is implemented using Python, with a focus on a streamlined deployment using Streamlit for the frontend.

Table of Contents
Overview
Features
Dataset
Technologies Used
Model
Frontend Deployment
Results
Setup and Installation
Usage
Contributing
License
References
Overview
Phishing attacks are a common type of cyber threat, where attackers disguise malicious websites as legitimate ones to steal sensitive information. This project develops a machine learning model that can classify a given URL as phishing or legitimate based on various URL and webpage features.

Features
Automatic Feature Extraction: Extracts features from a given URL such as length, number of special characters, presence of keywords, domain age, and more.
Machine Learning Models: Uses models like Random Forest and AdaBoost to classify URLs.
Streamlit Frontend: Provides a user-friendly interface where users can input a URL and receive a prediction.
Data Preprocessing: Handles missing values and balances classes using SMOTE for better model performance.
Dataset
The dataset used in this project consists of various features extracted from URLs, including:
length_url: Length of the URL.
nb_dots: Number of dots in the URL.
length_hostname: Length of the hostname.
https_token: Presence of HTTPS tokens.
domain_registration_length: Duration of domain registration.
web_traffic: Traffic rank of the website.
google_index: Google indexing status.
and many more.
status: Target variable indicating whether the website is phishing or legitimate.
A subset of 5000 rows from the dataset is used for training and testing the models.

Technologies Used
Python: Core programming language for implementing the model.
Pandas & NumPy: Data manipulation and analysis.
scikit-learn: Machine learning library for model training and evaluation.
Streamlit: Framework for deploying a web-based interface.
Jupyter Notebook/VS Code: For developing and testing the code.
Model
The model utilizes:

Random Forest: For robust classification based on ensemble learning.
AdaBoost: To improve the accuracy by boosting weaker models.
Feature Engineering: Automatically extracts key URL-based features for better prediction.
Frontend Deployment
The model is deployed using Streamlit, allowing users to enter a URL through a web interface. The model extracts necessary features, processes the input, and outputs a prediction indicating whether the URL is phishing or legitimate.

Results
Achieved high accuracy in distinguishing phishing URLs from legitimate ones.
Reduced false positives by using a combination of Random Forest and AdaBoost models.
Streamlit interface simplifies user interactions, making it easy for users to check URLs.


Setup and Installation

To run this project locally, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/dishankjain14/PHISHING-WEBSITES-DETECTION.git
cd phishing-website-detection

Create and activate a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required packages:
bash
Copy code
pip install -r requirements.txt

Run the Streamlit app:
bash
Copy code
streamlit run main.py
Access the app in your browser at http://localhost:8501.

Usage
Open the Streamlit web interface.
Enter the URL you want to test in the provided input field.
Click "Check" to get the prediction.
The app will display whether the URL is classified as Phishing or Legitimate.
