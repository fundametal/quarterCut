# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\sweet\\PycharmProjects\\pythonProject',
             'C:\\Users\\sweet\.conda\envs\opencv\Lib\site-packages\PySide2',
             'C:\\Users\\sweet\\.conda\\envs\\opencv\\Lib\\site-packages\\PyQt5\\Qt5\\bin',
             'C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x64',
             'C:\\Users\\sweet\\Desktop\\dlls'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
