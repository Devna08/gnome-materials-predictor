import urllib.request

url = "https://storage.googleapis.com/gnome_materials_data/gnome_predictions_csv/gnome_predictions_stable.csv"
output_path = "gnome_predictions_stable.csv"

urllib.request.urlretrieve(url, output_path)
print("✅ 다운로드 완료:", output_path)