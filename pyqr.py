from kittyscript import *
URL = input("Input URL\n:")
Namefi = input("Input name of file\n:")
Generateqrcode(URL, f"{Namefi}.png")

Metadata = ["""
License :: MIT :: https://github.com/Iwertyuiop123653/PyQr/blob/main/LICENSE
More Meta :: TOML :: https://github.com/Iwertyuiop123653/PyQr/blob/main/Pyqr.toml
    """]