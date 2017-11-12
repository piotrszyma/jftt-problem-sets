### YATS - Yet Another Testing Suite

Small testing suite for JFTT problem set no 2.

Written and tested using Python 3.6

### Setup
1. install packages from file `requirements.txt` (file in root dir of  project) with `pip install -r requirements.txt`
2. install package `entr` in your linux environment (http://entrproject.org/) tu use watch script
3. check if `run` & `watch` files are executables `sudo chmod +x watch & sudo chmod +x run`

### Usag

If you want to run tests of task:
1. go to task dir, for example `/lexers/task-1/` 
2. run test script by typing  `./run`

If you want to run all tests each time you change `lexer.lex` file, run "watch" script by typing `./watch`