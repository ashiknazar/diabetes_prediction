# PIAM Diabetes Dataset

The **PIAM Diabetes Dataset** is commonly used in machine learning tasks to predict the likelihood of diabetes in individuals based on several health-related attributes. It contains various features associated with individuals' health, along with an outcome label indicating whether the individual has diabetes.

## Features:
1. **Pregnancies**: The number of times the individual has been pregnant.
2. **Glucose**: Plasma glucose concentration after a 2-hour oral glucose tolerance test.
3. **BloodPressure**: Diastolic blood pressure (in mm Hg).
4. **SkinThickness**: Thickness of the skinfold at the triceps (in mm).
5. **Insulin**: Serum insulin concentration (in mu U/ml) at 2 hours.
6. **BMI**: Body Mass Index (calculated as weight in kg divided by height in meters squared).
7. **DiabetesPedigreeFunction**: A score based on the family history of diabetes, indicating the likelihood of an individual being diagnosed with diabetes.
8. **Age**: Age of the individual in years.

## Target Variable:
- **Outcome**: A binary variable indicating whether the individual has diabetes. `1` means the person is diabetic, and `0` means they are not.

## Data Usage:
The dataset is typically used for:
- **Diabetes Prediction**: Predicting whether an individual will develop diabetes based on the given features.
- **Feature Selection**: Identifying the most relevant features for diabetes prediction.
- **Model Training**: Building and training machine learning models (like Logistic Regression, Random Forest, etc.) to predict diabetes.

## Dataset Example:

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome |
|-------------|---------|---------------|---------------|---------|------|---------------------------|-----|---------|
| 6           | 148     | 72            | 35            | 0       | 33.6 | 0.627                     | 50  | 1       |
| 1           | 85      | 66            | 29            | 0       | 26.6 | 0.351                     | 31  | 0       |
| 8           | 183     | 64            | 0             | 0       | 23.3 | 0.672                     | 32  | 1       |
| 1           | 89      | 66            | 23            | 94      | 28.1 | 0.167                     | 21  | 0       |

The dataset is widely used for research and education in the fields of health and machine learning, offering a great opportunity for exploring predictive models and understanding the relationships between health factors and diabetes.
