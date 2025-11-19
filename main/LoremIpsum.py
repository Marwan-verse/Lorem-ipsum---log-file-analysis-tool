import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from ui import *
import os
import time

GRAPH_PATH = "reports/GraphReports/"
REPORTS_PATH = "reports/TextReports/"
MAIN_REPORT_PATH = "reports/_MainReport_/main.txt"

AUTH_GRAPH_FILE = "auth.png"
SQLI_GRAPH_FILE = "sqli.png"
LFI_GRAPH_FILE = "lfi.png"
CI_GRAPH_FILE = "ci.png"

AUTH_REPORT_FILE = "auth.txt"
BRUTE_REPORT_FILE = "brute.txt"
SQLI_REPORT_FILE = "sqli.txt"
LFI_REPORT_FILE = "lfi.txt"
CI_REPORT_FILE = "ci.txt"

TAB_TO_SPACE = 4

#ensure the directories exist
os.makedirs(GRAPH_PATH, exist_ok=True) #checks if graph directory exists
os.makedirs(REPORTS_PATH, exist_ok=True) #checks if text report directory exist
os.makedirs(os.path.dirname(MAIN_REPORT_PATH), exist_ok=True) #takes only directory path not the file name

def show_text_ui():
    text = "Main Report has been generated and added to: " + MAIN_REPORT_PATH
    while True:
        #MAIN UI generated with image to ascii image online
        print_logo()
        print_name()
        print_option_menu()
        print("\n \033[92m" + text.center(125) + "\n")
        choice = input("\033[92mEnter your choice (1/2/3): ").strip()
        if choice == "1":
            os.system('clear')  #clear the screen for better readability
            imageGraphUI()
        elif choice == "2":
            os.system('clear')  #clear the screen for better readability
            show_reports()
        elif choice.lower() == "3":
            os.system('clear')  #clear the screen for better readability
            print_bye_bye()
            time.sleep(1)
            exit()
        else:
            os.system('clear')  #clear the screen for better readability
            print("\033[92mInvalid choice. Try again.")
            time.sleep(1)
            os.system('clear')  #clear the screen for better readability

def show_reports(): #shows the reports menu
    print_text_reports_menu()   
    choice2 = input("Enter your choice (1/2/3/4/5/6): ").strip()
    if choice2 == "1":
        generate_all_reports(auth_dict, incidents, sqli_dict, lfi_dict, ci_dict, choice2)
        time.sleep(1)
        with open(REPORTS_PATH + AUTH_REPORT_FILE) as report:
            print("\n===== Failed Logins =====\n")
            print(report.read())
            print("Report saved at " + REPORTS_PATH + AUTH_REPORT_FILE)
            return_from_report_view()
                
    elif choice2 == "2": #brute force
        generate_all_reports(auth_dict, incidents, sqli_dict, lfi_dict, ci_dict, choice2)
        time.sleep(1)
        with open(REPORTS_PATH + BRUTE_REPORT_FILE) as report:
            print("\n===== Possible Brute Force Attacks =====\n")
            print(report.read())
            print("Report saved at " + REPORTS_PATH + BRUTE_REPORT_FILE)
            return_from_report_view()
                
    elif choice2 == "3":#sql injection
        generate_all_reports(auth_dict, incidents, sqli_dict, lfi_dict, ci_dict, choice2)
        time.sleep(1)
        with open(REPORTS_PATH + SQLI_REPORT_FILE) as report:
            print("\n===== SQL Injection =====\n")
            print(report.read())
            print("Report saved at " + REPORTS_PATH + SQLI_REPORT_FILE)
            return_from_report_view()

    elif choice2 == "4":#lfi
        generate_all_reports(auth_dict, incidents, sqli_dict, lfi_dict, ci_dict, choice2)
        time.sleep(1)
        with open(REPORTS_PATH + LFI_REPORT_FILE) as report:
            print("\n===== Local File Inclusion =====\n")
            print(report.read())
            print("Report saved at " + REPORTS_PATH + LFI_REPORT_FILE)
            return_from_report_view()

    elif choice2 == "5":#command injection
        generate_all_reports(auth_dict, incidents, sqli_dict, lfi_dict, ci_dict, choice2)
        time.sleep(1)
        with open(REPORTS_PATH + CI_REPORT_FILE) as report:
            print("\n===== Command Injection =====\n")
            print(report.read())
            print("Report saved at " + REPORTS_PATH + CI_REPORT_FILE)
            return_from_report_view()

    elif choice2.lower() == "6": #quit
        os.system('clear')  #clear the screen for better readability
        show_text_ui()    
    else:
        os.system('clear')  #clear the screen for better readability
        print("\033[92mInvalid choice. try again.")
        time.sleep(2)
        os.system('clear')  #clear the screen for better readability
        show_reports() #restart the report menu

def return_from_report_view():
    user_input = input("Press enter to return to the reports ").strip() 
    #if user_input is not None:
    show_reports()

def imageGraphUI(): #shows the image and graph menu
    print_graph_menu()
    choice2 = input("Enter your choice (1/2/3/4/5): ").strip()
    if choice2 == "1": #failed logins/authentication
        os.system('clear') #clear the screen for better readability
        print("Generating Top Offending IPS Graph...")
        generate_graph(auth_dict, "1")
        print("Generated Top Offending IPS Graph at " + GRAPH_PATH + AUTH_GRAPH_FILE)
        imageGraphUI() #return to image graph menu
    
    elif choice2 == "2":#sql injection
        os.system('clear')  #clear the screen for better readability
        print("Generating SQL Injection Graph...")
        generate_graph(sqli_dict, "2") #2 is the choice for sqli
        print("Generated SQL Injection Graph at " + GRAPH_PATH + SQLI_GRAPH_FILE)
        imageGraphUI() #return to image graph menu

    elif choice2 == "3":#lfi
        os.system('clear')  #clear the screen for better readability
        print("Generating Local File Inclusion Graph...")
        generate_graph(lfi_dict, "3")
        print("Generated Local File Inclusion Graph at " + GRAPH_PATH + LFI_GRAPH_FILE)
        imageGraphUI() #return to image graph menu

    elif choice2 == "4":#command injection
        os.system('clear')  #clear the screen for better readability
        print("Generating Command Injection Graph...")
        generate_graph(ci_dict, "4")
        print("Generated Command Injection Graph at " + GRAPH_PATH + CI_GRAPH_FILE)
        imageGraphUI() #return to image graph menu

    elif choice2 == "5": 
        os.system('clear')
        show_text_ui() #return to main menu

    else:
        os.system('clear')
        print("Invalid choice, try again.") 
        time.sleep(1) 
        imageGraphUI() #restart image graph menu


#------------------------------------------------------BACKEND------------------------------------------------------
#parsing SSH auth lines
def parse_auth_line(line):
    parts = line.split()
    # timestamp: first 3 tokens 'Mar 10 13:58:01'
    ts_str = " ".join(parts[0:3])
    try:
        ts = datetime.strptime(f"2025 {ts_str}", "%Y %b %d %H:%M:%S")
    except Exception:
        ts = None
    ip = None
    event_type = "other"
    if "Failed password" in line:
        event_type = "failed"
    elif "Accepted password" in line or "Accepted publickey" in line:
        event_type = "accepted"
    if " from " in line:
        try:
            idx = parts.index("from")
            ip = parts[idx+1]
        except (ValueError, IndexError):
            ip = None
    return ts, ip, event_type

#parsing Apache and SSH no auth lines
#SSH no auth lines will just get discarded in main
def parse_other_line(line):
    command_injection_list = ["cmd", "cat", "ls" ]
    sqli_list = ["%20OR%20", "%27"]
    lfi_list = ["../", "%2e%2e%2f"]

    parts = line.split() #split by whitespace
    
    ip = parts[0] #first part is always the IP

    sqli_check = False
    lfi_check = False
    ci_check = False

    #when any() spots any trues, it returns true right away
    ci_check   = any(ci in line for ci in command_injection_list) 
    sqli_check = any(sqli in line for sqli in sqli_list)
    lfi_check  = any(lfi in line for lfi in lfi_list)

    return sqli_check, lfi_check, ci_check, ip

def sort_dict_by_value(dictionary):
    #auth dictionary holds timestamps, because it is used by brute-force detection
    #here the timestamps need to be converted to counts, checked by dictionary type
    if dictionary.default_factory == list:
        #turn timestamps to counts
        counts_dic = ((ip, len(times)) for ip, times in dictionary.items())
    else:
        counts_dic = dictionary.items()

    #sort by count descending and assemble new dictionary with IP key and int value
    return dict(sorted(counts_dic, key=lambda item: item[1], reverse=True))    
    
def generate_graph(dictionary, choice):
    big_yaxis_jump = 10 #controls the jump between points on Y axis
    small_yaxis_jump = 5 #controls the jump between points on Y axis

    title, filename = assign_graph_properties(choice)
    
    #x and y label are the same for each graph
    xlabel = "IP"
    ylabel = "attempts"


    plt.figure(figsize=(15,5))

    #if "directory" argument is list of dictonaries (only one case => bruteforce)
    if isinstance(dictionary, list):
        key_names = [item["ip"] for item in dictionary]
        values = [item["count"] for item in dictionary]
    #if "directory" argument is dictionary
    else:
        key_names = list(dictionary.keys())
        values = list(dictionary.values())

    #check how the y axis should be scaled
    if values[0] >= 50:
        graph_yaxis_jump = big_yaxis_jump
    else: 
        graph_yaxis_jump = small_yaxis_jump

    #show top 10
    plt.bar(key_names[0:10], values[0:10])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(graph_yaxis_jump)) 
    plt.tight_layout()
    plt.savefig(GRAPH_PATH + filename)
    plt.show()

def assign_graph_properties(choice):
    
    #auth
    if choice == "1":
        title = "Failed logins"
        filename = AUTH_GRAPH_FILE
    #sqli
    elif choice == "2":
        title = "SQL Injection attacks"
        filename = SQLI_GRAPH_FILE
    #lfi
    elif choice == "3":
        title = "Local File Inclusion attacks"
        filename = LFI_GRAPH_FILE
    #ci
    elif choice == "4": 
        title = "Command Injection attacks"
        filename = CI_GRAPH_FILE
    else:
        title = None
        filename = None

    return title, filename

def generate_all_reports(auth_dict, incidents, sqli_dict, lfi_dict, ci_dict, choice="0"):
    #expandtabs are needed because report is show in the terminal and in the txt file as well
    #terminal and txt see tab differently but see space the same
    header = "\nIP\t\t\t\tcount".expandtabs(TAB_TO_SPACE) 
    brute_header = "\nIP\t\t\t\tcount\tfirst failed login\t\tlast failed login".expandtabs(TAB_TO_SPACE)
    
    indentation = "\n\n" #two enters between main report sections
    auth_title = "Most failed logins:"
    brute_title = "Possible brute-force attacks record:"
    sqli_title = "SQL Injection attempts:"
    lfi_title = "Local File Inclusion attempts:"
    ci_title = "Command Injection Attempts:"

    write_mode = 'w'  #used to overwrite the main report each time
    append_mode = 'a' #used to append to the main report after the first write

    #0 generates main report
    if choice == "0":
        generate_simple_report(auth_dict, MAIN_REPORT_PATH, write_mode, auth_title, header)
        generate_simple_report(incidents, MAIN_REPORT_PATH, append_mode, indentation + brute_title, brute_header, True)
        generate_simple_report(sqli_dict, MAIN_REPORT_PATH, append_mode, indentation + sqli_title, header)
        generate_simple_report(lfi_dict, MAIN_REPORT_PATH, append_mode, indentation + lfi_title, header)
        generate_simple_report(ci_dict, MAIN_REPORT_PATH, append_mode, indentation + ci_title, header)
    #failed logins/authentication
    elif choice == "1":
        generate_simple_report(auth_dict, REPORTS_PATH + AUTH_REPORT_FILE, write_mode, auth_title, header)
    #possible brute-force
    elif choice == "2":
        generate_simple_report(incidents, REPORTS_PATH + BRUTE_REPORT_FILE, write_mode, brute_title, brute_header, True)
    #SQLi
    elif choice == "3":
        generate_simple_report(sqli_dict, REPORTS_PATH + SQLI_REPORT_FILE, write_mode, sqli_title, header)
    #LFI
    elif choice == "4":
        generate_simple_report(lfi_dict, REPORTS_PATH + LFI_REPORT_FILE, write_mode, lfi_title, header)
    #CI
    elif choice == "5":
        generate_simple_report(ci_dict, REPORTS_PATH + CI_REPORT_FILE, write_mode, ci_title, header)


def generate_simple_report(dictionary, filename, mode, title, headers, brute_force=False):
    tab_threshold = 11 #if IP is under or equal 11 chars in length, it needs one more tab after it 
                       #for nice formatting, used in report generating
    double_digit = 10  #if count is double digit, you need one more tab

    with open(filename, mode) as f:
        f.write(title)
        f.write(headers)

        #brute_force has different format, expandtabs secures the same format in txt file and terminal view
        if brute_force:
            for incident in dictionary:
                #these ifs are used for formatting, there cases when ip is short and need one more tab
                #and cases where count is double digit and needs one less tab
                if len(incident["ip"]) <= tab_threshold and incident["count"] >= double_digit: #both conditions met
                    f.write(f"\n{incident["ip"]}\t\t[{incident["count"]}]\t{incident["first"]}\t\t{incident["last"]}".expandtabs(TAB_TO_SPACE))

                elif len(incident["ip"]) <= tab_threshold: #only ip condition met
                    f.write(f"\n{incident["ip"]}\t\t[{incident["count"]}]\t\t{incident["first"]}\t\t{incident["last"]}".expandtabs(TAB_TO_SPACE))

                elif incident["count"] >= double_digit: #only count condition met
                    f.write(f"\n{incident["ip"]}\t[{incident["count"]}]\t{incident["first"]}\t\t{incident["last"]}".expandtabs(TAB_TO_SPACE))

                else: #no conditions met
                    f.write(f"\n{incident["ip"]}\t[{incident["count"]}]\t\t{incident["first"]}\t\t{incident["last"]}".expandtabs(TAB_TO_SPACE))
        #any other report
        else:
            for ip, count in dictionary.items():
                if len(ip) <= tab_threshold:
                    f.write(f"\n{ip}\t\t[{count}]".expandtabs(TAB_TO_SPACE))
                else:
                    f.write(f"\n{ip}\t[{count}]".expandtabs(TAB_TO_SPACE))

def bruteforce_sliding_window(auth_per_ip_timestamps):
    #sliding window technique, search for counts of incidents, record those where are five under 10 minutes
    incidents = []
    window = timedelta(minutes=10)
    for ip, times in auth_per_ip_timestamps.items():
        times.sort()
        n = len(times)
        i = 0
        while i < n:
            j = i
            while j + 1 < n and (times[j+1] - times[i]) <= window: #check 10 minute time window
                j += 1
            count = j - i + 1
            if count >= 5:
                incidents.append({
                    "ip": ip,
                    "count": count,
                    "first": times[i].isoformat(),
                    "last": times[j].isoformat()
                })
    # advance i past this cluster to avoid duplicate overlapping reports:
                i = j + 1
            else:
                i += 1                
    return incidents

if __name__ == "__main__":
    auth_per_ip_timestamps = defaultdict(list)
    sqli_per_ip_count = defaultdict(int)
    lfi_per_ip_count = defaultdict(int)
    ci_per_ip_count = defaultdict(int)

    while True: #keep asking for log file until a valid one is given
        #ask user if they want to enter a log name or use the default one
        file_choice = input("Do you want to enter a log name or use the default log (CA1_project.log)?\n1. Enter log name\n2. Use default log\nEnter your choice (1/2): ")
        if file_choice == "1": #custom log
            LOGFILE = input("Enter Log Name : ")
        elif file_choice == "2": #default log
            LOGFILE = "CA1_project.log"

        else: #invalid choice, use default
            print("Invalid choice, using default log (CA1_project.log).")
            LOGFILE = "CA1_project.log"

        try: #try to open the log file, if it does not exist, ask again
            with open(LOGFILE) as f:
                for line in f:
                    #" from " is only in the SSH auth log lines
                    if " from " in line:
                        ts, ip, event = parse_auth_line(line)
                        if ts and ip and event == "failed":
                            auth_per_ip_timestamps[ip].append(ts)
                    #Apache and non auth SSH lines will come here, later one will get discarded
                    else:
                        sqli, lfi, ci, ip = parse_other_line(line)
                        if sqli:
                            sqli_per_ip_count[ip] += 1
                        elif lfi:
                            lfi_per_ip_count[ip] += 1
                        elif ci:
                            ci_per_ip_count[ip] += 1
            break #exit the while loop if file was opened successfully
        except FileNotFoundError: #file does not exist, ask again
            os.system('clear')  #clear the screen for better readability
            print(f"No log file with the name '{LOGFILE}' was found. Please try again.\n")
            
    os.system('clear')  #clear the screen for better readability

    #detect brute-force attacks
    incidents = bruteforce_sliding_window(auth_per_ip_timestamps)

    #sort all the dictionaries
    auth_dict = sort_dict_by_value(auth_per_ip_timestamps)
    sqli_dict = sort_dict_by_value(sqli_per_ip_count)
    lfi_dict = sort_dict_by_value(lfi_per_ip_count)
    ci_dict = sort_dict_by_value(ci_per_ip_count)

    #generates main report, it is generated by default, user does not have a choice
    generate_all_reports(auth_dict, incidents, sqli_dict, lfi_dict, ci_dict)

    show_text_ui() #start the text UI after everything is done in the backend