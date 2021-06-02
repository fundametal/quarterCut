# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\sweet\\PycharmProjects\\pythonProject',
             'C:\\Users\\sweet\\.conda\\envs\\opencv\\Lib\\site-packages\\PySidce2',
             'C:\\Users\\sweet\\.conda\\envs\\opencv\\Lib\\site-packages\\PyQt5\\Qt5\\bin',
             'C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x64',
             'C:\\Users\\sweet\\.conda\\envs\\opencv\\Lib\\site-packages\\numpy',
             'C:\\Users\\sweet\\.conda\envs\\pyinstaller\\Lib\\site-packages\\PySide2',
             'C:\\Users\\sweet\\.conda\\envs\\pyinstaller\\Lib\\site-packages\\shiboken2',
             'C:\\Users\\sweet\\.conda\\envs\\pyinstaller\\Lib\\site-packages\\pkg'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5', 'pkg', 'numpy'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=False,
          name='main',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
