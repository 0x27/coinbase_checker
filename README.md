# coinbase_checker
utility script to check and log coinbase balances

see `requirements.txt` for required libs.

you will need to set up an API key/secret. put these in `creds.py`. they just need read-balance privs.

to run, just run `account_checker.py`. it dumps out date/total-euro-value to a csv.

example run:  
```
$ python account_checker.py 
[+] Current Datetime: 2017-09-11 15:19:44.097024
[+] You have [REDACTED] LTC valued at [REDACTED] euros
[+] You have [REDACTED] ETH valued at [REDACTED] euros
[+] You have [REDACTED] EUR valued at [REDACTED] euros
[+] You have [REDACTED] BTC valued at [REDACTED] euros
[+] Total euro worth is: [REDACTED] 
$
```
