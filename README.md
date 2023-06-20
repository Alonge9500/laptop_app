# Laptop Price Estimation
* This project aims to estimate the price of laptops based on their specifications using machine learning techniques.


By *Alonge Daniel*, a Data Scientist, passionate about data and technology.

- GitHub: [Alonge 9500](https://github.com/Alonge9500)
- LinkedIn: [Alonge Daniel](https://www.linkedin.com/in/alonge-daniel-27b4b4139/)
- Email: [Alonge Daniel](mailto:alongedaniel19@gmail.com)
- Streamlit App[Laptop APP](https://alonge9500-laptop-app-app-x8dzj1.streamlit.app/)

I' will appreciate any comment and correction on this work 


## Dataset
* The project uses a dataset containing information about various laptops, including their specifications and corresponding prices. The dataset is not included in this repository, but you can obtain a similar dataset from a reliable source or use your own dataset.

## Notebooks
* The project is organized into multiple Jupyter Notebooks:

### Data Exploration: This notebook explores the dataset, performs data cleaning and preprocessing, and prepares the data for training the machine learning model.

### Model Training: This notebook trains a machine learning model using the preprocessed data from the previous notebook. It applies various regression algorithms, evaluates their performance, and selects the best-performing model.

### Model Evaluation: This notebook further evaluates the selected model, performs additional analysis, and provides insights into the model's predictions and features.

### Streamlit Integration: This notebook integrates the trained machine learning model into a Streamlit web application, allowing users to input laptop specifications and obtain estimated prices.

## Dependencies
* To run the notebooks and the Streamlit application, you need the following dependencies:

- Python (version 3.6 or later)
- Jupyter Notebook
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- Joblib
- JSON
You can install the required dependencies by running the following command:

      `pip install -r requirements.txt`
## Usage
1. Start by running the Data Exploration notebook to understand and preprocess the dataset. Ensure that the dataset is available in the expected format.

2. Move on to the Model Training notebook to train and evaluate the machine learning model. Adjust the notebook according to your dataset and requirements.

3. Run the Model Evaluation notebook to analyze the model's performance and gain insights into its predictions.

4. Finally, integrate the trained model into the Streamlit application by following the steps in the Streamlit Integration notebook. Customize the application as needed and ensure that the required resources (model file and property dictionary) are available.

### Resources
The following resources are included in the repository:

1. model.pkl: The trained machine learning model serialized using Joblib. This file is required for running the Streamlit application.

2. propertydict.json: A dictionary that maps property names to numerical values for the laptop specifications. This file is used in the Streamlit application to display dropdown menus for selecting laptop features.


Contact
For any questions or inquiries, please contact alongedaniel19@gmail.com
