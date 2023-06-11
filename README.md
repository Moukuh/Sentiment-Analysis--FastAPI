# Suicidal Intention Prediction
This project predicts whether a tweet indicates suicidal intention. It uses a machine learning model trained on a dataset of tweets that have been labeled as either suicidal or not suicidal.

The Dataset is contains twitter contents.

Dataset link: https://raw.githubusercontent.com/laxmimerit/twitter-suicidal-intention-dataset/master/twitter-suicidal_data.csv



### Requirements
* Python 3.6 or later 
* NumPy
* Pandas
* Scikit-learn
* FastAPI
* Pydantic

### Installation
To install the project, run the following command:

` pip install -r requirements.txt `

### Usage
To use the project, 
* First run the `main.py` file.
* Visit FastAPI/SwaggerUI page: http://127.0.0.1:8000/docs
* Click on "Try it out" button on the `POST/predict Predict Label` section
* Replace the "string" with any of your tweet or any sentence
* On the `response` section it will display whether prediction 1 or 0

**This is how it will look:**

##### Input string:

<img width="1203" alt="Screenshot 2023-06-11 at 4 03 10 PM" src="https://github.com/Moukuh/Sentiment-Analysis--FastAPI/assets/72088794/ec6ebf8b-bb3a-4394-b81e-48ea88ec475a">


##### Response:

<img width="1203" alt="Screenshot 2023-06-11 at 4 03 32 PM" src="https://github.com/Moukuh/Sentiment-Analysis--FastAPI/assets/72088794/e07f3de4-f442-4696-9bba-04b797d558b1">


### Metrics scores

<img width="430" alt="Screenshot 2023-06-11 at 4 08 53 PM" src="https://github.com/Moukuh/Sentiment-Analysis--FastAPI/assets/72088794/088dae4f-7c2a-441d-bb01-2a1ce6d9755c">




### Contributing
Contributions are welcome! Please open an issue or pull request if you have any ideas for improvements.

### License
This project is licensed under the MIT License.
