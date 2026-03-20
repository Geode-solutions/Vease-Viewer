# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_all
import sys

datas = []
binaries = []
hiddenimports = []
datas += collect_data_files('opengeodeweb_viewer')
datas += collect_data_files('vease_viewer')
tmp_ret = collect_all('vtkmodules')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['src/vease_viewer/app.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
if sys.platform.startswith('linux'):
    exclude_patterns = [
        'libX11', 'libXext', 'libXrender', 'libXcursor', 'libXfixes', 'libXi',
        'libXinerama', 'libXrandr', 'libXcomposite', 'libXdamage', 'libXxf86vm',
        'libxcb', 'libxkbcommon', 'libwayland', 'libEGL', 'libGLESv2',
        'libGL', 'libGLX', 'libz.so', 'libbz2.so', 'libstdc++.so', 'libgcc_s.so'
    ]

    a.binaries = [entry for entry in a.binaries
                  if not any(pat.lower() in entry[0].lower() for pat in exclude_patterns)]

elif sys.platform.startswith('win'):
    exclude_patterns_win = [
        'opengl32.dll',
        'libEGL.dll',
        'libGLESv2.dll',
        'd3dcompiler_*.dll',     # often not needed if using system DirectX
        'libcrypto-*.dll',       # ← only if you provide your own OpenSSL
        'libssl-*.dll',
    ]

    a.binaries = [entry for entry in a.binaries
                  if not any(pat.lower() in entry[0].lower() for pat in exclude_patterns_win)]
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='vease-viewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
