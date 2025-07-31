
import pandas
import lightgbm as lgb
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from pandas import ExcelWriter

# Load data
excelDF = pandas.ExcelFile('STATION1.xlsx')
X1 = pandas.read_excel(excelDF, 'TRAINING', usecols='AL')
Y1 = pandas.read_excel(excelDF, 'TRAINING', usecols='AM')
X2 = pandas.read_excel(excelDF, 'VALIDATION', usecols='AL')
Y2 = pandas.read_excel(excelDF, 'VALIDATION', usecols='AM')

x_train, x_test = X1, X2
y_train, y_test = Y1, Y2

params = {
    'task': 'train',
    'boosting': 'gbdt',
    'objective': 'regression',
    'num_leaves': 100,
    'learning_rate': 0.1,
    'metric': ['l2', 'l1'],
    'verbose': 1
}

lgb_train = lgb.Dataset(x_train, y_train)
lgb_eval = lgb.Dataset(x_test, y_test, reference=lgb_train)

model = lgb.train(params, train_set=lgb_train, valid_sets=lgb_eval, verbose_eval=False)

# Predictions
y1_pred = model.predict(x_train)
y2_pred = model.predict(x_test)

# Evaluation
R2_train = r2_score(y_train, y1_pred)
R2_test = r2_score(y_test, y2_pred)
MAE_train = mean_absolute_error(y_train, y1_pred)
MAE_test = mean_absolute_error(y_test, y2_pred)
MSE_train = mean_squared_error(y_train, y1_pred)
MSE_test = mean_squared_error(y_test, y2_pred)
RMSE_train = MSE_train**0.5
RMSE_test = MSE_test**0.5

print(f'R2_train: {R2_train:.3f}, R2_test: {R2_test:.3f}')
print(f'MAE_train: {MAE_train:.3f}, MAE_test: {MAE_test:.3f}')
print(f'RMSE_train: {RMSE_train:.3f}, RMSE_test: {RMSE_test:.3f}')

# Export predictions
df11 = pandas.DataFrame(y1_pred)
df12 = pandas.DataFrame(y2_pred)
with ExcelWriter('LightGBM01.xlsx') as writer:
    df11.to_excel(writer, sheet_name='LightGBM', startrow=3, startcol=2, header=False, index=False)
    df12.to_excel(writer, sheet_name='LightGBM', startrow=3, startcol=3, header=False, index=False)
