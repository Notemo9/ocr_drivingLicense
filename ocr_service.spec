# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ocr_service.py'],
    pathex=[],
    binaries=[('H:\\python\\Lib\\site-packages\\paddle\\libs\\mklml.dll', '.')],
    datas=[('H:\\python\\Lib\\site-packages\\PIL', 'PIL'), ('H:\\python\\Lib\\site-packages\\paddleocr', 'PaddleOCR')],
    hiddenimports=['shapely', 'pyclipper', 'skimage', 'skimage.morphology', 'imgaug', 'requests', 'tools', 'flask', 'flask_cors', 'paddleocr', 'PIL', 'numpy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ocr_service',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
