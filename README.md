# Suicidal Intention Prediction
This project predicts whether a tweet indicates suicidal intention. It uses a machine learning model trained on a dataset of tweets that have been labeled as either suicidal or not suicidal.

The Dataset is contains twitter contents.
Dataset link: https://raw.githubusercontent.com/laxmimerit/twitter-suicidal-intention-dataset/master/twitter-suicidal_data.csv



## Requirements
Python 3.6 or later
NumPy
Pandas
Scikit-learn
FastAPI
Pydantic

## Installation
To install the project, run the following command:

` pip install -r requirements.txt `

## Usage

To use the project, first start the FastAPI server by running the following command:

Use code with caution. Learn more

uvicorn main:app --host 127.0.0.1 --port 8000

Code snippet

Then, you can use the following curl command to predict the suicidal intention of a tweet:

Use code with caution. Learn more

curl -X POST -H "Content-Type: application/json" -d '{ "text": "I'm feeling really down today and I don't know what to do." }' http://127.0.0.1:8000/predict

The response will be a JSON object with the following key:

prediction: The predicted suicidal intention, either 0 or 1.
Contributing
Contributions are welcome! Please open an issue or pull request if you have any ideas for improvements.

**License**
This project is licensed under the MIT License.
