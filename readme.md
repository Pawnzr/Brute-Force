# PassGen
## A targeted password dictionary attack tool
## Examples:
### Basic Usage:
Generates a password list by replaceing the first character of the target password and appending an extra character to the end.
```
python passgen.py smith
```
### Passwords with numbers:
Generates a large number of potential passwords by replace the first character and appending a 4 digit number from 0-9999 to the end of the target password.
```
python passgen.py -n ftech
```

### Full password list:
Genearates a large number of potential passwords by generating a list of every combination of replacement passwords
```
python passgen.py -f ftech
```
432 password generated.

```
ftecH
ftec(h
ftE<h
...
F73<#
F73(H
F73cH
```
### Basic password list output to file
Create a basic password list and save it to a file.

```
python passgen.py -o outputFile.txt ftech
```

### Basic password list saved to clipboard
Create a basic password list and save it to your clipboard so you can paste it elsewhere.

```
python passgen.py -c ftech
```

### Dependencies:
- [Requests](http://docs.python-requests.org/en/latest/user/install/#install)
- [Pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)



