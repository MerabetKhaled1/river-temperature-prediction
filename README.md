# River Water Temperature Prediction and Signal Decomposition

This repository provides implementations for predicting river water temperature using boosting algorithms in Python, along with MATLAB scripts for signal decomposition analysis of hydrological time series.  

The combination of machine learning models and signal decomposition techniques enables both accurate prediction and deeper understanding of the underlying dynamics in river temperature data.

---

## Python Models

Python implementations of four boosting algorithms are included for river water temperature prediction:

- **AdaBoost**
- **CatBoost**
- **LightGBM**
- **XGBoost**

### Requirements

Install the dependencies using:

```bash
pip install pandas numpy scikit-learn xgboost catboost lightgbm
```

### Data

The dataset `STATION1.xlsx` must be placed in the project root directory.  
It includes two sheets:

- **TRAINING**: Training data  
- **VALIDATION**: Testing data  

### Usage (Python)

Run each model separately:

```bash
python adaboost_model.py
python catboost_model.py
python lightgbm_model.py
python xgboost_model.py
```

Each script outputs performance metrics and exports predictions to Excel.

---

## MATLAB Codes

This repository also provides MATLAB scripts for **signal decomposition**, such as:

- **EMD Empirical Mode Decomposition)**  
- **EEMD (Ensemble Empirical Mode Decomposition)**  
- **CEEMDAN (Complete Ensemble Empirical Mode Decomposition with Adaptive Noise)**   
- Additional helper scripts for plotting and analysis  

These methods are useful for analyzing non-linear and non-stationary hydrological signals prior to model training.

### Usage (MATLAB)

1. Open MATLAB.  
2. Navigate to the `Matlab_Code_Signal_Decomposition` directory.  
3. Run the desired script, for example:

```matlab
EMD_decomposition
EEMD_decomposition
CEEMDAN_decomposition
```

Each script performs signal decomposition and saves the results (plots or data files) in the output folder.

---

## Project Structure

```
river-temperature-prediction/
│
├── python_models/
│   ├── adaboost_model.py
│   ├── catboost_model.py
│   ├── lightgbm_model.py
│   └── xgboost_model.py
│
├── matlab_code/
│   ├── EMD_decomposition.m
│   ├── EEMD_decomposition.m
│   ├── CEEMDAN_decomposition.m
│   └── signal_plot.m
│
├── data/
│   └── STATION1.xlsx
│
└── README.md
```
