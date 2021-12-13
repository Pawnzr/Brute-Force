# PassGen
## A targeted password dictionary attack tool

PassGen is a security tool intended to generate a potential password list for a target using different combinations of capital 
letters and common substitutions.  It can also be used to make HTTP requests to see if any passwords from the list are valid.  

**It is intended to be used for internal security testing to identify any weak passwords that might be in use and 
should never be used against a target without their full consent.**

Complete list of options:
- no options : generates a password list by replaceing the first character of the password and appending an extra character to the end.
- -f : generate a full password list.  This can make the password list quite lengthy.
- -n : generate a password list the appends 4 digit numbers to the end of the target password.
- -o : output file name
- -t : HTTP request target (example: http://myTestSite.com/login)
- -d : HTTP parameters (example: email=abe@test.com,password={0}).  The {0} specifies where the password will be inserted into the data.
- -g : Text to search for in the HTTP response.  Use this to determine when a password has worked.
- -n : Append numbers flag.  Appends the numbers 0-9999 to the end of all passwords
- -c : Copy to clipboard flag.  Copys results to the clipboard

## Examples:
### Basic Usage:
Generates a password list by replaceing the first character of the target password and appending an extra character to the end.

```
python passgen.py smith
```
### Passwords with numbers:
Generates a large number of potential passwords by replace the first character and appending a 4 digit number from 0-9999 to the end of the target password.

```
python passgen.py -n smith
```

### Full password list:
Genearates a large number of potential passwords by generating a list of every combination of replacement passwords

```
python passgen.py -f smith
```

Generates 76 passwords like so:

```
smith1
smith2
smith3
...
5mith&
5mith*
5mith?
```

### Basic password list output to file
Create a basic password list and save it to a file.

```
python passgen.py -o outputFile.txt smith
```

### Basic password list saved to clipboard
Create a basic password list and save it to your clipboard so you can paste it elsewhere.

```
python passgen.py -c smith
```


### Dependencies:
- [Requests](http://docs.python-requests.org/en/latest/user/install/#install)
- [Pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)



