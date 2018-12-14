# Introduction
## functionality
This project mainly focus on thing as follows:
- extract data from the SQL server
- export the data into a excel or txt or csv file(actually, whatever you want.)
- and pack the data file into a encrypted zip file with a given password
- send a email which contains the encrypted zip file and a correlated messages.
- full suport logging for every detail.
## environment requirement
- python 3.6.
- a existed SQL server
- 7z(open source packing/unpacking software **which support cmd calling**)
- a email server(like gmail,hotmail,even your company email server.)
## python module requirement
- `datetime` for a clock which controls send the email or not.
- `cx_Oracle` or `pymysql` or.....to fetch the data.
- `os` which calling the system shell language which can handle the packing functionality
- `logging` which writes the logging into files carefully
- `smtplib` which signs in the email server
- `email` which manages the structure of one email
- `pandas` which reads the parameters from a excel(we take the excel sheet as the configuration table) 