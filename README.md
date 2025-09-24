selenium==4.35.0
pytest==7.4.2
pytest-html==4.3.1
live-server==0.4.1

for execute test_calculadora open a terminal in /Calculadora folder and run:
python -m pytest -v

for execute only exception tests open a terminal in /Calculadora folder and run:
python -m pytest -m exception

for execute only smoke tests open a terminal in /Calculadora folder and run:
python -m pytest -m smoke

for generate html report open a terminal in /Calculadora folder and run:
python -m pytest --html=reports/report_calculadora.html

To open the report go to /Calculadora/reports folder and open report_calculadora.html with live server

