# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

# 需要打包的额外资源文件
added_files = []
assets_dir = Path('assets')
if assets_dir.is_dir():
    for f in assets_dir.rglob('*'):
        if f.is_file():
            # 格式: (源路径, 目标文件夹)
            added_files.append((str(f), str(f.parent.relative_to('.'))))

a = Analysis(
    ['main.py'],  # 入口文件
    pathex=[],
    binaries=[],
    datas=added_files,  # 包含assets中的所有文件
    hiddenimports=['pywin32', 'pythonnet'],  # 需要的隐藏导入
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ComfyLauncher',  # 生成的exe名称
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 不显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icons/app_icon.ico' if Path('assets/icons/app_icon.ico').is_file() else None,  # 如果有可执行文件图标，可添加
)