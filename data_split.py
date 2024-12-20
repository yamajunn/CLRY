# import os
# import shutil
# import random

# # データセットのパス
# base_dir = "C:/Users/Owner/Desktop/CLRY/Clash_royale/train"
# image_dir = os.path.join(base_dir, "images")
# label_dir = os.path.join(base_dir, "labels")

# output_base = "C:/Users/Owner/Desktop/CLRY/Clash_royale"
# val_image_dir = os.path.join(output_base, "valid/images")
# val_label_dir = os.path.join(output_base, "valid/labels")
# test_image_dir = os.path.join(output_base, "test/images")
# test_label_dir = os.path.join(output_base, "test/labels")

# # 分割比率
# val_ratio = 0.2  # 検証用データの割合（20%）
# test_ratio = 0.1  # テスト用データの割合（10%）

# # フォルダを作成
# os.makedirs(val_image_dir, exist_ok=True)
# os.makedirs(val_label_dir, exist_ok=True)
# os.makedirs(test_image_dir, exist_ok=True)
# os.makedirs(test_label_dir, exist_ok=True)

# # 画像リストの取得
# images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
# random.shuffle(images)

# # 分割用のインデックスを計算
# total_images = len(images)
# val_count = int(total_images * val_ratio)
# test_count = int(total_images * test_ratio)

# val_images = images[:val_count]
# test_images = images[val_count:val_count + test_count]

# # データを移動
# def move_files(image_list, src_image_dir, src_label_dir, dest_image_dir, dest_label_dir):
#     for img in image_list:
#         # 画像を移動
#         shutil.move(os.path.join(src_image_dir, img), os.path.join(dest_image_dir, img))
#         # 対応するラベルファイルを移動
#         label_file = os.path.splitext(img)[0] + ".txt"
#         if os.path.exists(os.path.join(src_label_dir, label_file)):
#             shutil.move(os.path.join(src_label_dir, label_file), os.path.join(dest_label_dir, label_file))

# # 検証用データを移動
# move_files(val_images, image_dir, label_dir, val_image_dir, val_label_dir)

# # テスト用データを移動
# move_files(test_images, image_dir, label_dir, test_image_dir, test_label_dir)

# print(f"データ分割完了:")
# print(f"  検証用: {len(val_images)} 枚 -> {val_image_dir}, {val_label_dir}")
# print(f"  テスト用: {len(test_images)} 枚 -> {test_image_dir}, {test_label_dir}")
# print(f"  学習用: {len(images) - val_count - test_count} 枚 残存")
import torch
import torchvision

print("PyTorch Version:", torch.__version__)
print("Torchvision Version:", torchvision.__version__)
print("CUDA Available:", torch.cuda.is_available())
print("CUDA Device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None")

from torchvision.ops import nms
boxes = torch.rand((10, 4)).cuda()
scores = torch.rand(10).cuda()
iou_threshold = 0.5
keep = nms(boxes, scores, iou_threshold)
print(keep)
