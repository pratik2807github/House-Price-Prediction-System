# 🏡 House Price Prediction System

### Machine Learning | Python | Scikit-learn | Pandas | NumPy | Streamlit

## 📌 Project Overview

The **House Price Prediction System** is a Machine Learning project designed to predict house prices based on various property features. The project uses historical housing data to train a predictive model and provides an interactive web application where users can enter property details and receive an estimated house price.

The goal of this project is to demonstrate the practical application of data preprocessing, exploratory data analysis (EDA), feature engineering, Machine Learning, and model deployment using Streamlit.

## 🎯 Project Objectives

* Analyze housing data to understand the factors influencing house prices.
* Perform data cleaning and preprocessing.
* Explore relationships between property features and house prices.
* Prepare numerical and categorical features for Machine Learning.
* Train a Machine Learning model to predict house prices.
* Evaluate model performance using appropriate metrics.
* Build an interactive web application using Streamlit.

## ✨ Key Features

* **House Price Prediction:** Predicts estimated property prices using a trained Machine Learning model.
* **Interactive Web Interface:** Allows users to enter property details through a Streamlit application.
* **Property Features:** Uses information such as bedrooms, bathrooms, lot size, floors, waterfront status, property condition, and other housing attributes.
* **Location-Based Features:** Incorporates location-related features from the dataset.
* **Pre-trained Model:** Loads a saved Machine Learning model for predictions.
* **Real-Time Interaction:** Generates predictions based on the user's inputs without requiring the model to be trained again every time.

## 🛠️ Technologies Used

| Technology       | Purpose                                                      |
| ---------------- | ------------------------------------------------------------ |
| Python           | Core programming language                                    |
| Pandas           | Data manipulation and analysis                               |
| NumPy            | Numerical computations                                       |
| Matplotlib       | Data visualization                                           |
| Seaborn          | Exploratory data analysis and statistical visualization      |
| Scikit-learn     | Machine Learning and model evaluation                        |
| Jupyter Notebook | Data analysis, experimentation, and model development        |
| Streamlit        | Interactive web application                                  |
| Pickle           | Saving and loading the trained model and feature information |
| Git & GitHub     | Version control and project hosting                          |

## 📂 Project Structure

```text
House-Price-Prediction-System/
│
├── app.py
├── house_price_prediction.ipynb
├── house_price_model.pkl
├── features.pkl
├── modified_data.csv
├── requirements.txt
└── README.md
```

**File descriptions:**

* `app.py` — Contains the Streamlit application for predicting house prices.
* `house_price_prediction.ipynb` — Contains data analysis, preprocessing, feature engineering, and Machine Learning development.
* `house_price_model.pkl` — Stores the trained Machine Learning model.
* `features.pkl` — Stores the feature information required by the application.
* `modified_data.csv` — Contains the processed dataset used in the project.
* `requirements.txt` — Lists the Python libraries required to run the project.
* `README.md` — Provides project documentation and setup instructions.

*Note: Update the file structure to match the files you actually upload to GitHub.*

## 📊 Dataset Description

The project uses housing data containing property characteristics and location-related information.

The features used in the prediction process include:

| Feature           | Description                                          |
| ----------------- | ---------------------------------------------------- |
| Bedrooms          | Number of bedrooms                                   |
| Bathrooms         | Number of bathrooms                                  |
| Sqft Lot          | Total lot area in square feet                        |
| Floors            | Number of floors                                     |
| Waterfront        | Indicates whether the property has waterfront access |
| View              | Property view rating                                 |
| Condition         | Overall property condition                           |
| Sqft Above        | Above-ground living area in square feet              |
| Sqft Basement     | Basement area in square feet                         |
| Year Built        | Year the property was constructed                    |
| Year Renovated    | Year of renovation, where applicable                 |
| Location Features | Encoded city and state ZIP code information          |
| Price             | Target variable representing the house price         |

The dataset is processed before being passed to the Machine Learning model.

## ⚙️ Project Workflow

The project follows an end-to-end Machine Learning workflow.

### 1. Data Collection

Load the housing dataset into a Jupyter Notebook for analysis.

### 2. Data Cleaning and Preprocessing

Inspect the dataset, handle data quality issues, and prepare the features for analysis and model training.

### 3. Exploratory Data Analysis (EDA)

Analyze housing prices and investigate relationships between property characteristics and the target variable using statistical summaries and visualizations.

### 4. Feature Engineering

Prepare numerical and categorical variables for the Machine Learning model. Location-related categorical features are encoded to make them suitable for prediction.

### 5. Model Training

Train a Machine Learning regression model using the prepared dataset.

### 6. Model Evaluation

Evaluate the model using appropriate regression metrics to understand how well it predicts house prices.

### 7. Model Saving

Save the trained model and required feature information using Pickle.

### 8. Web Application Development

Build an interactive interface using Streamlit to collect property details and display the predicted price.

### 9. Prediction

Load the saved model, process the user's inputs into the expected feature format, and generate a house price estimate.

## 🚀 Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Install the following:

* Python 3.10 or a compatible Python version
* Git
* Jupyter Notebook (for model development)
* Visual Studio Code or another Python editor

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd House-Price-Prediction-System
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### Step 2: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

If your repository contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the main libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit jupyter
```

### Step 4: Run the Application

Ensure that `app.py`, `house_price_model.pkl`, and `features.pkl` are available in the appropriate project directory.

Run:

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to access the application.

## 💻 How to Use the Application

1. Start the Streamlit application.
2. Enter the required property details.
3. Provide the available property characteristics, such as bedrooms, bathrooms, lot size, floors, and other supported features.
4. Submit the inputs using the application's prediction control.
5. View the estimated house price.

**Note:** The prediction is an estimate based on the trained model and dataset. It should not be treated as a professional property valuation.

## 📈 Model Performance

The model's performance should be reported using evaluation metrics calculated on data that was not used to train the model.

| Evaluation Metric              | Description                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| R² Score                       | Measures how much of the variation in the target variable is explained by the model |
| Mean Absolute Error (MAE)      | Measures the average absolute difference between actual and predicted prices        |
| Mean Squared Error (MSE)       | Measures the average squared prediction error                                       |
| Root Mean Squared Error (RMSE) | Measures prediction error in the target variable's units                            |

**Important:** Add your final test-set evaluation results here after confirming the metrics from your notebook. Do not report training results as test results.

## 🔍 Skills Demonstrated

This project demonstrates practical skills in:

* Python programming
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization
* Feature engineering
* Categorical feature encoding
* Regression-based Machine Learning
* Model evaluation
* Model serialization using Pickle
* Streamlit application development
* Integrating a trained model into a web application
* GitHub project documentation

## 🔮 Future Improvements

Potential improvements include:

* Compare multiple regression algorithms.
* Optimize model performance through hyperparameter tuning.
* Improve model evaluation and error analysis.
* Add interactive visualizations for housing trends.
* Improve input validation and application error handling.
* Deploy the application to a cloud hosting platform.
* Add automated testing and continuous integration.
* Improve the user interface and prediction explanations.

## ⚠️ Limitations

* Prediction accuracy depends on the quality and representativeness of the training dataset.
* The model may not generalize well to locations or property types that are poorly represented in the data.
* House prices change over time, so the model may require retraining with newer data.
* Predicted prices are estimates and are not guaranteed to match actual market values.

## 👨‍💻 Author

**Pratik Gurav**

Aspiring Data Scientist | Machine Learning Enthusiast

Interested in Data Science, Machine Learning, Python, and building practical data-driven applications.

## 📄 License

This project is intended for educational and portfolio purposes. If you plan to distribute or reuse the project, add an appropriate license after confirming that the dataset and other project materials permit your intended use.
