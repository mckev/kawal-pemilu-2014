@echo off
for /l %%x in (1, 1, 5000) do (
    python main.py
    timeout /t 5
)
