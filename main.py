import pandas as pd
import numpy as np
import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import preprocess_kgptalkie as ps
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

df = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/twitter-suicidal-intention-dataset/master/twitter-suicidal_data.csv')

def get_clean(x):
    x = str(x).lower().replace('\\', '').replace('_', ' ')
    x = ps.cont_exp(x)
    x = ps.remove_emails(x)
    x = ps.remove_urls(x)
    x = ps.remove_html_tags(x)
    x = ps.remove_rt(x)
    x = ps.remove_accented_chars(x)
    x = ps.remove_special_chars(x)
    x = re.sub("(.)\\1{2,}", "\\1", x)
    return x

df['tweet'] = df['tweet'].apply(lambda x: get_clean(x))

tfidf = TfidfVectorizer(max_features=20000, ngram_range=(1,3), analyzer='char')
X = tfidf.fit_transform(df['tweet'])
y = df['intention']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

clf = LinearSVC()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Save the model object using joblib
joblib.dump(clf, 'model.joblib')

# Load the model object using joblib
clf = joblib.load('model.joblib')

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict_label(input_text: InputText):
    text = input_text.text
    tfidf_text = tfidf.transform([text])
    prediction = int(list(clf.predict(tfidf_text))[0])
    return {"prediction": prediction}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)