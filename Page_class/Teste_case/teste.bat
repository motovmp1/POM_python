@ECHO OFF
ECHO Congratulations! Your batch file executed successfully.
ECHO Your test will running now...
ls
cd..
cd C:\Users\elsys\Documents\pycharm_robot\POM_python
ls
pip install html-testRunner
python -m Page_class.Teste_case.Teste_case

