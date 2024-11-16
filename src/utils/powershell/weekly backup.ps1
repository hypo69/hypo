## \file hypotez/src/utils/powershell/weekly backup.ps1
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.utils.powershell """
MODE = 'debug'
wbadmin start backup -backupTarget:E: -include:C: -allCritical -quiet