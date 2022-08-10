import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter","mysql.connector","init"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Coffe_reeBão",
    version="0.1",
    description="Cafeina",
    options={'build_exe': {'include_files': ['img/menu.png', 'img/alter.png','img/alterar.png', 'img/alterprodbt1.png', 'img/botao_produto.png','img/btn1.png','img/cadastrar.png',
    'img/cadFabr.png','img/cadProdt.png','img/clearbt.png','img/codigo_produtobt.png','img/delbt1.png','img/delprod.png','img/excluir.png','img/excluirBt.png',
    'img/fabricbt1.png','img/lmenu.png','img/menu.png','img/prodbt1.png','img/search.png',
    'img/searchbt1.png','img/voltar.png','img/sub.png','img/soma.png','img/menu_select.png','img/estqopen.png','img/confirm2.png']}},
    executables=[Executable("main.py", base=base)]
)