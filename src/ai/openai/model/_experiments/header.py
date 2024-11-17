

""" Модуль управления моделью OpenAI 
"""


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
ffmpeg: Path = Path( __root__ , 'bin' , 'ffmpeg' , 'bin' , 'ffmpeg.exe') 
sys.path.append (__root__)   
sys.path.append (ffmpeg)