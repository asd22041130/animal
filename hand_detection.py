import sys
from ultralytics import YOLO
import os
import cv2

def main():
    # ✅ 載入模型（使用官方預訓練權重）
    model = YOLO("yolov8n-seg.pt")  # 可換成 yolov8s-seg.pt、yolov8m-seg.pt...

    # ✅ 推論圖片
    image_path = "images/raw/animal.jpg"
    results = model(image_path)

    # ✅ 取出結果
    result = results[0]

    # ✅ 顯示結果（跳出視窗）
    result.show()

    # ✅ 儲存圖片（含遮罩）
    result.save(filename="images/results/animal_yolo.jpg")
    img_with_boxes = result.plot()
    cv2.imwrite("images/results/animal_yolo.jpg", img_with_boxes)
    print(f"結果儲存於：images/results/animal_yolo.jpg")

    # ✅ 印出物件資訊
    for box in result.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = result.names[cls_id]
        print(f"發現 {label}，信心值 {conf:.2f}")

    # ✅ 顯示遮罩資訊
    if result.masks is not None:
        print(f"共有 {result.masks.data.shape[0]} 個遮罩")
        print(f"遮罩形狀：{result.masks.data.shape}")  # (N, H, W)
    else:
        print("⚠️ 無遮罩資料")

if __name__ == "__main__":
    main()
