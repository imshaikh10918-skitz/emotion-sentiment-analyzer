# SETUP Instructions for the Streamlit Application

## Installation Steps
1. **Clone the repository**: 
   ```bash
   git clone https://github.com/imshaikh10918-skitz/emotion-sentiment-analyzer.git
   cd emotion-sentiment-analyzer
   ```
2. **Create a virtual environment**:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install required packages**:  
   ```bash
   pip install -r requirements.txt
   ```

## Training Instructions
1. **Prepare your dataset**: Ensure that you have your dataset ready in the correct format.
2. **Run the training script**: Execute the training script to train the model.
   ```bash
   python train.py
   ```

## Deployment to Streamlit Cloud
1. **Sign in to Streamlit Cloud**: Go to [Streamlit Cloud](https://streamlit.io/cloud) and create an account if you don’t have one.
2. **Connect your GitHub account**: Link your GitHub account to Streamlit Cloud.
3. **Deploy your app**:
   - Click on the **New App** button.
   - Select the repository and branch where your app is located.
   - Click **Deploy**.

## Troubleshooting Guide
- **Common Errors**:
  - Check the logs in Streamlit Cloud for error messages.
  - Ensure all dependencies are listed in `requirements.txt`.
- **Model Not Training**: 
  - Verify the dataset format and the training script configurations.

## File Structure
```
emotion-sentiment-analyzer/
├── app.py                  # Main Streamlit application
├── train.py                # Model training script
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

## Features List
- Emotion Analysis
- Sentiment Analysis
- User-friendly interface with Streamlit
- Visualizations for insights

## Support Information
For support, please raise an issue in this repository or contact the author.
