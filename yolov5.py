import torch
from pathlib import Path
from PIL import Image

# モデルをロード
model = torch.hub.load(
    'ultralytics/yolov5',
    'custom',
    path=str(Path('best.pt')),  # pathlib.Pathでパスを処理
    force_reload=True
)

# 推論対象の画像パス
image_path = str(Path('image.png'))  # pathlib.Pathでパスを処理

# 推論の実行
results = model(image_path)

# 結果を保存
output_dir = Path('runs/detect/exp')  # デフォルト出力ディレクトリ
output_dir.mkdir(parents=True, exist_ok=True)
results.save(str(output_dir))  # Pathオブジェクトを文字列に変換して渡す

# 結果を表示 (ターミナルにテキスト出力)
print(results.pandas().xyxy[0])  # バウンディングボックス座標とクラス情報

# 結果画像を表示 (任意)
results.show()  # Matplotlibを使用して表示