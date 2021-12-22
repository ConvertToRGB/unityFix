 ![APM](https://img.shields.io/badge/python-2.7-green)  ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# unityFix

I had problems with Unity 2019.4. It couldn't open projects because some problems with layout. 
I found sulution on the web and to solve my problem I needed to replace or remove corrypted  `CurrentLayout-default.dwlt`
That's whay I created this script to automate this process.

Script must be in the unity project directory. Then you can give path to your working `*.dwlt` file or do nothing and corrupted file will be removed and Unity will create new `*.dwlt` file on the next start.

