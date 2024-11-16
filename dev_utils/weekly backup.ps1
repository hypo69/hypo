## \file hypotez/dev_utils/weekly backup.ps1
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: dev_utils """
MODE = 'debug'
wbadmin start backup -backupTarget:E: -include:C: -allCritical -quiet