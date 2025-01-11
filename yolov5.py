import torch
from torchvision import transforms
from PIL import Image

# モデルのパス
model_path = 'best.pt'

# 推論用画像のパス
image_path = 'sample.jpg'

# 推論用変換
transform = transforms.Compose([
    transforms.Resize((640, 640)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# YOLOv5 モデルのロード
model = torch.load(model_path, map_location=torch.device('cpu'))

# モデルの評価モードに設定
model.eval()

# 画像の読み込みと変換
image = Image.open(image_path).convert("RGB")
input_tensor = transform(image).unsqueeze(0)

# 推論
with torch.no_grad():
    outputs = model(input_tensor)

print(outputs)
