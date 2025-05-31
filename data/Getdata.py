from mp_api.client import MPRester
import pandas as pd

API_KEY = "9xsM4n73eGZYklDw8B9XFU6HWBF3XIKA"

with MPRester(API_KEY) as m:
    docs = m.materials.search(
        elements=["Li", "Fe", "O"],
        num_elements=3,
        fields=["material_id", "formula_pretty", "density"],
        num_chunks=1
    )

# 각 항목을 객체에서 속성으로 꺼냄
rows = []
for doc in docs:
    rows.append({
        "material_id": doc.material_id,
        "formula": doc.formula_pretty,
        "density": doc.density
    })

df = pd.DataFrame(rows)
df.to_csv("materials_data.csv", index=False)

print("✅ 정상 포맷으로 저장 완료!")
print(df.head())
