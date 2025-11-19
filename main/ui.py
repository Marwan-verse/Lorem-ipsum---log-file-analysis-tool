def print_logo(): #shows the main menu
    print("""\033[91m
                                     .                                                   .
                                   .n                  .                 .                n.
                          .       .dP                dP                   9b              9b.     .
                         4      qXb         .       dX                     Xb     .        dXp      t
                         dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
                         9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
                         9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
                             `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b0Xd8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
                              `9XXXXXXXXXXP' `9XX'  \033[92mLOREM\033[91m   `98v8P'  \033[92mIPSUM\033[91m   `XXP' `9XXXXXXXXXXXP' 
                                 ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                                                 )b.  .dbo.dP'`v'`9b.odb.  .dX(
                                               ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                                              dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                                             dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                                             9XXb'  `XXXXXXb.dX|Xb.dXXXXX'   `dXXP
                                              `'     9XXXXXXX(   )XXXXXXP      `'
                                                       XXXX X.`v'.X XXXX
                                                       XP^X'`b   d'`X^XX
                                                       X. 9  `   '  P )X
                                                       `b  `       '  d'
                                                         `           ' """) #code in eyes to make the loren ipsum green where if you put the code \033[92m it makes
                                                                         #any text green and to change ot back after you put the code \033[91m
def print_name(): #shows the report menu
    print("""\033[94m                                                                                                                                     
                   ██╗      ██████╗ ██████╗ ███████╗███╗   ███╗    ██╗██████╗ ███████╗██╗   ██╗███╗   ███╗
                   ██║     ██╔═══██╗██╔══██╗██╔════╝████╗ ████║    ██║██╔══██╗██╔════╝██║   ██║████╗ ████║
                   ██║     ██║   ██║██████╔╝█████╗  ██╔████╔██║    ██║██████╔╝███████╗██║   ██║██╔████╔██║
                   ██║     ██║   ██║██╔══██╗██╔══╝  ██║╚██╔╝██║    ██║██╔═══╝ ╚════██║██║   ██║██║╚██╔╝██║
                   ███████╗╚██████╔╝██║  ██║███████╗██║ ╚═╝ ██║    ██║██║     ███████║╚██████╔╝██║ ╚═╝ ██║
                   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝    ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝""") #blue text
def print_option_menu(): #shows the graph menu     
    print("""\033[93m
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+ 
    |      \033[97m1. Generate Graph Reports\033[93m      | |           \033[97m2. View Reports\033[93m           | |             \033[97m3. Quit\033[93m                 | 
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+""") 
def print_text_reports_menu(): #shows the attack menu
    print("""\033[93m 
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+ 
    |          \033[97m1. Failed Logins  \033[93m         | |          \033[97m2. Brute Force\033[93m             | |          \033[97m3. SQL Injection\033[93m           | 
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+ 
    |       \033[97m4. Local File Inclusion\033[93m       | |         \033[97m5. Command Injection\033[93m        | |             \033[97m6. Quit\033[93m                 | 
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+""")
def print_graph_menu(): #shows the image and graph menu
    print("""\033[93m 
                      +-------------------------------------+  +-------------------------------------+ 
                      |        \033[97m1. Failed Logins Graph  \033[93m     |  |       \033[97m2. SQL Injection Graph\033[93m        | 
                      +-------------------------------------+  +-------------------------------------+
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+ 
    |    \033[97m3. Local File Inclusion Graph\033[93m    | |      \033[97m4. Command Injection Graph\033[93m     | |             \033[97m5. Quit\033[93m                 | 
    +-------------------------------------+ +-------------------------------------+ +-------------------------------------+""")
def print_bye_bye(): #shows the goodbye message
    print("""
    ▄▄▄▄ ▓██   ██▓▓█████     ▄▄▄▄ ▓██   ██▓▓█████ 
    ▓█████▄▒██  ██▒▓█   ▀    ▓█████▄▒██  ██▒▓█   ▀ 
    ▒██▒ ▄██▒██ ██░▒███      ▒██▒ ▄██▒██ ██░▒███   
    ▒██░█▀  ░ ▐██▓░▒▓█  ▄    ▒██░█▀  ░ ▐██▓░▒▓█  ▄ 
    ░▓█  ▀█▓░ ██▒▓░░▒████▒   ░▓█  ▀█▓░ ██▒▓░░▒████▒
    ░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░
    ▒░▒   ░▓██ ░▒░  ░ ░  ░   ▒░▒   ░▓██ ░▒░  ░ ░  ░
    ░    ░▒ ▒ ░░     ░       ░    ░▒ ▒ ░░     ░   
    ░     ░ ░        ░  ░    ░     ░ ░        ░  ░
        ░░ ░                     ░░ ░            """) #goodbye message in green ascii art