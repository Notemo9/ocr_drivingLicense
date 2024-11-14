# from paddleocr import PaddleOCR, draw_ocr

# # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
# img_path = './img/sjps.jpg'
# data = []
# result = ocr.ocr(img_path, cls=True)
# for idx in range(len(result)):
#     res = result[idx]
#     for line in res:
#         data.append(line[1][0])

# print(data)
# # 显示结果
# # from PIL import Image
# # result = result[0]
# # image = Image.open(img_path).convert('RGB')
# # boxes = [line[0] for line in result]
# # txts = [line[1][0] for line in result]
# # scores = [line[1][1] for line in result]
# # im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# # im_show = Image.fromarray(im_show)
# # im_show.save('result.jpg')
from flask import Flask, request, jsonify
from flask_cors import CORS
from paddleocr import PaddleOCR
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
CORS(app)  # 启用 CORS
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # 加载模型

@app.route('/ocr', methods=['POST'])
def ocr_service():
    if 'file' not in request.files:
        return jsonify({"error": "未提供文件"}), 400

    file = request.files['file']
    try:
        img = Image.open(file.stream).convert('RGB')  # 转换为 RGB 格式
        img_array = np.array(img)  # 转换为 NumPy 数组
        
        print(f"Image type: {type(img_array)}, Shape: {img_array.shape}")  # 打印调试信息
        
        result = ocr.ocr(img_array, cls=True)  # 使用 NumPy 数组直接识别
        
        if not result:
            return jsonify({"error": "OCR 识别失败，未检测到文字"}), 500
        
        data = [line[1][0] for res in result for line in res]

        return jsonify(data)

    except Exception as e:
        print(f"Error: {e}")  # 在日志中打印具体的错误
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

