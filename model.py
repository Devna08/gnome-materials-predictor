import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

# CSV 읽기
df = pd.read_csv("materials_data.csv")

# 결측치 제거
df = df.dropna(subset=["formula", "density"])

# 🔹 1. One-hot encoding (formula → 숫자화)
encoder = OneHotEncoder(sparse_output=False)
X = encoder.fit_transform(df[["formula"]])
y = df["density"]

# 🔹 2. 학습/테스트 셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 3. 모델 학습
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔹 4. 예측 및 평가
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📊 MAE (Mean Absolute Error): {mae:.4f}")
print(f"📈 R² Score: {r2:.4f}")

# 🔹 5. 예측 vs 실제값 시각화
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual Density (g/cm³)")
plt.ylabel("Predicted Density (g/cm³)")
plt.title("Actual vs Predicted Density")
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='gray')
plt.grid(True)
plt.tight_layout()
plt.show()
