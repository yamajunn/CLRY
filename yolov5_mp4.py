import torch
from pathlib import Path
import cv2

# モデルをロード
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')  # 'best.pt' のパスを指定

# 入力動画のパスと出力動画のパス
input_video_path = 'inputs/input.mp4'  # 入力動画のパス
output_video_path = 'outputs/output.mp4'  # 出力動画のパス

# 動画を読み込む
cap = cv2.VideoCapture(input_video_path)

# 動画のプロパティを取得
fps = int(cap.get(cv2.CAP_PROP_FPS))  # フレームレート
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # フレームの幅
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # フレームの高さ
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4形式のエンコーダ

# 出力動画のライターを作成
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# フレームごとに処理
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # フレームを推論
    results = model(frame)

    # 推論結果を取得
    annotated_frame = results.render()[0]  # 推論結果を描画したフレーム

    # フレームを動画に書き込む
    out.write(annotated_frame)

# リソースを解放
cap.release()
out.release()

print(f"推論結果の動画を保存しました: {output_video_path}")
