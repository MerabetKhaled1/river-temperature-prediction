
# River Water Temperature Prediction using Boosting Algorithms

This repository includes Python implementations of four boosting algorithms to predict river water temperature:

- AdaBoost
- CatBoost
- LightGBM
- XGBoost

## Requirements

Install the dependencies using:

```bash
pip install pandas numpy scikit-learn xgboost catboost lightgbm
```

## Data

The dataset `STATION-S04-DUNAJEC.xlsx` must be placed in the project root. It includes two sheets:
- `TRAINING`: Training data
- `VALIDATION`: Testing data

Columns used:
- `AL`: Feature input
- `AM`: Target temperature

## Usage

Run each model separately:

```bash
python adaboost_model.py
python catboost_model.py
python lightgbm_model.py
python xgboost_model.py
```

Each script outputs performance metrics and exports predictions to Excel.
