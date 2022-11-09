@echo off

call python twomaxonRelease.py
call python twomaxonTense.py

call python motorTestTCPserver8006double.py

pause
