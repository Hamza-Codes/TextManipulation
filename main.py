import sys, pyperclip

print("Hello world")

PASSWORDS = {'email':'897asdmlaisd90329340@asdasnco.com',
            'blog':'asdascBCdfSCWEr23432SDVXC',
            'luggage':'12345'}

if len(sys.argv) < 2:
    print("Usage: main.py [account] - copy account password ")
    sys.exit()
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named '+account)