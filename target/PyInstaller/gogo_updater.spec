# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\peera\\Documents\\Work\\LIL\\GoGo Firmware Updater\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\peera\\Documents\\Work\\LIL\\GoGo Firmware Updater\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\program files (x86)\\python37-32\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\peera\\AppData\\Local\\Temp\\tmp5bdqa1cx\\fbs_pyinstaller_hook.py'],
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
          exclude_binaries=True,
          name='gogo_updater',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\peera\\Documents\\Work\\LIL\\GoGo Firmware Updater\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='gogo_updater')
