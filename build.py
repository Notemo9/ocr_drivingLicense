import os
import sys
from PyInstaller.__main__ import run

if __name__ == '__main__':
    # 设置要打包的文件
    script_name = 'ocr_service.py'  # 你的 Flask 应用文件名
    if not os.path.isfile(script_name):
        print(f"{script_name} 文件不存在!")
        sys.exit(1)

    # 获取 mklml.dll 文件路径
    mklml_dll_path = os.path.join(sys.prefix, 'Lib', 'site-packages', 'paddle', 'libs', 'mklml.dll')
    if not os.path.isfile(mklml_dll_path):
        print(f"未找到 mklml.dll 文件: {mklml_dll_path}")
        sys.exit(1)

    # 需要添加的模块和依赖
    hidden_imports = [
        'shapely',
        'pyclipper',
        'skimage',
        'skimage.morphology',
        'imgaug',
        'requests',
        'tools',  # 假设你有这个模块
        'flask',
        'flask_cors',
        'paddleocr',
        'PIL',
        'numpy'
    ]

    # 添加模块到打包配置
    hidden_import_args = []
    for mod in hidden_imports:
        hidden_import_args.append('--hidden-import')
        hidden_import_args.append(mod)

    # 获取 PIL 和 PaddleOCR 的路径并添加数据
    pil_path = os.path.join(sys.prefix, 'Lib', 'site-packages', 'PIL')
    paddleocr_path = os.path.join(sys.prefix, 'Lib', 'site-packages', 'paddleocr')

    if not os.path.isdir(pil_path):
        print(f"未找到 PIL 目录: {pil_path}")
        sys.exit(1)

    if not os.path.isdir(paddleocr_path):
        print(f"未找到 PaddleOCR 目录: {paddleocr_path}")
        sys.exit(1)

    # 打包命令
    run([
        script_name,
        '--clean',
        '-F',
        # '--onefile',  # 打包成一个单独的 EXE 文件
        '--windowed',  # 不显示控制台窗口（可以去掉，如果需要查看输出）
        '--add-binary', f'{mklml_dll_path};.',  # 将 mklml.dll 添加到打包文件中
        '--add-data', f'{pil_path};PIL',  # 添加 PIL 依赖
        '--add-data', f'{paddleocr_path};PaddleOCR',  # 添加 PaddleOCR 依赖
        '--clean',  # 清理临时文件
        *hidden_import_args  # 添加所有 hidden-import
    ])
