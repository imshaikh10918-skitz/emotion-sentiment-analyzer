# Configuration settings for Emotion Sentiment Analyzer

# Model Configuration
MODEL_TYPE = 'transformer'  # Example: 'LSTM' or 'CNN'
MODEL_NAME = 'emotion_model'

# Data Paths
TRAINING_DATA_PATH = './data/training_data.csv'
VALIDATION_DATA_PATH = './data/validation_data.csv'
TEST_DATA_PATH = './data/test_data.csv'

# Training Parameters
BATCH_SIZE = 32
EPOCHS = 20
LEARNING_RATE = 0.001
DROPOUT_RATE = 0.5

# Emotion Labels
EMOTION_LABELS = ['joy', 'anger', 'sadness', 'surprise', 'fear']
