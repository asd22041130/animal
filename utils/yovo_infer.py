# utils/yolo_infer.py
from ultralytics import YOLO

# 載入模型放在 module 全域，重複呼叫也不會一直重新載
_model = YOLO("yolov8n.pt")         # 你可換成 yolov8s.pt 或 best.pt

def infer(image_path: str):
    """
    用 YOLOv8 推論單張圖片，回傳 results 物件
    """
    results = _model(image_path)
    return results[0]               # 只回傳第一張（results 是 list）
