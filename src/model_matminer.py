# model_matminer.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from pymatgen.core import Composition
from matminer.featurizers.composition import ElementProperty

def main():
    # 데이터 로딩 및 전처리
    df = pd.read_csv("materials_data.csv")
    df = df.dropna(subset=["formula", "density"])
    df["composition"] = df["formula"].apply(lambda x: Composition(x))

    # 특성 추출
    ep_feat = ElementProperty.from_preset("magpie")
    features = ep_feat.featurize_dataframe(df, col_id="composition", ignore_errors=True)

    X = features[ep_feat.feature_labels()]
    y = df["density"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"📊 MAE: {mae:.4f}")
    print(f"📈 R² Score: {r2:.4f}")

    # 시각화
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.xlabel("Actual Density (g/cm³)")
    plt.ylabel("Predicted Density (g/cm³)")
    plt.title("Matminer Features: Actual vs Predicted Density")
    plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='gray')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 🔒 요놈이 핵심!!
if __name__ == "__main__":
    main()