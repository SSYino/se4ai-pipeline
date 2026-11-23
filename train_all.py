# train_all.py -- the home-value model, as it grew out of a notebook.
# Run from the repository root:  python train_all.py
#
# Everything happens in one file, top to bottom: load, clean, encode,
# train, evaluate, save. It works... for the data we had last year.

import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# ---- 1. collect ---------------------------------------------------------

# ---- 2. clean -----------------------------------------------------------


# ---- 3. features --------------------------------------------------------

# experiment from March: log-transformed price. Didn't help? Not sure. Keep for now.
USE_LOG_PRICE = False
if USE_LOG_PRICE:
    import numpy as np
    y = np.log(y)

# ---- 4. train -----------------------------------------------------------

# ---- 5. evaluate --------------------------------------------------------
mae = mean_absolute_error(y_test, model.predict(X_test))
print(f"MAE: ${mae:,.0f}")

# ---- 6. save ------------------------------------------------------------
Path("out").mkdir(exist_ok=True)
joblib.dump(model, "out/model.joblib")
print("saved out/model.joblib")
