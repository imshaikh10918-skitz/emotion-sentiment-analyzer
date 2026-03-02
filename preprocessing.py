# Text Preprocessing Utilities

Here are some common text preprocessing utilities for sentiment analysis tasks:

## Functions:

### 1. Convert to Lowercase
```python
def to_lowercase(text):
    return text.lower()
```

### 2. Remove Punctuation
```python
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
```

### 3. Remove Stopwords
```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = text.split()
    return ' '.join([word for word in words if word not in stop_words])
```

### 4. Tokenization
```python
from nltk.tokenize import word_tokenize

def tokenize(text):
    return word_tokenize(text)
```

### 5. Lemmatization
```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def lemmatize(word):
    return lemmatizer.lemmatize(word)
```

### Usage Example
```python
if __name__ == '__main__':
    sample_text = "This is a sample text for preprocessing!"
    print(to_lowercase(sample_text))
    print(remove_punctuation(sample_text))
    print(remove_stopwords(sample_text))
    print(tokenize(sample_text))
    print(lemmatize('running'))
```