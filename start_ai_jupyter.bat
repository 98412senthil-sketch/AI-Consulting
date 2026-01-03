@echo off
REM ---------------------------------------------
REM Script to start Anaconda Prompt, activate env,
REM and launch Jupyter Notebook
REM ---------------------------------------------

REM Update this path if Anaconda is installed elsewhere
call "C:\ProgramData\anaconda3\Scripts\activate.bat"

REM Activate your environment
call conda activate ai_env

REM Launch Jupyter Notebook
jupyter notebook

REM Keep the window open
cmd /k
