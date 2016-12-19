# -*- mode: python -*-

block_cipher = None


a = Analysis(['Duo.py'],
             pathex=['C:\\Users\\PC\\Desktop\\FILES\\Works\\2D_GP\\Works\\Final_Work\\TheQ-master\\TheQ-master'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Duo',
          debug=False,
          strip=False,
          upx=True,
          console=True )
