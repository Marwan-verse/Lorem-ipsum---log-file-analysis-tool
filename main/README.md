Lorem Ipsum  

Log Analysis and Threat Detection Tool 

 

By 

Adam Pohořilský 
Dylan Twohig 
Marwan Fayad 

Introduction 

This project is a Python-based tool designed to detect and report on some of the common cybersecurity attacks based on system and web server log files. This tool focuses on identifying four specific types of attacks: Brute Force, SQL Injection (SQLi), Local File Inclusion (LFI), and Command Injection (CI). 

Lorem Ipsum works by scanning log files for suspicious patterns such as repeated failed logins or known exploit keywords. It uses time-based analysis to detect brute force attempts and signature checks for injection attacks.  

graph

Our text-based UI enable users to choose between viewing reports or generating graphs. Reports are saved in text format, while the graphs provide a visual summary of the top offending IP addresses for each threat type.  

Parsing 

The first thing we needed to program was parsing lines of the .log file. We discovered that there are two types of log lines: 

1) SSH authentication line example: 

Mar 10 13:45:10 host1 sshd[1933]: Failed password for invalid 	user ftpuser from 198.51.100.66 port 7722 ssh2 

2) Apache webserver messages example:  

198.51.100.66 - - [10/Mar/2025:13:45:12 +0000] "POST 			/images/logo.png HTTP/1.1" 200 1382 "https://example.com/" 		"Googlebot/2.1 (+http://www.google.com/bot.html)" 

Additionally, they’re SSH non-authentication lines, but they don’t interest us. We had already implemented the SSH auth lines parser in labs before, so we used that [1]. We then developed a parser function for Apache and any other SSH non-authentication lines. We used a similar method to the SSH line. In code, we extracted the dates and IP addresses by splitting the string and accessing the appropriate parts.  

We were scanning the Apache lines for three vulnerabilities – SQL injection, local file inclusion, and command injection. The SSH non-authentication logs just got discarded in the function. We reviewed the log file and identified the exploits, then constructed a blacklist for each of these vulnerabilities. The blacklists are short and made according to the log file.  

For real-world applications, the blacklist should be much longer. Or, in an ideal case, there should be no blacklists at all, as they are typically a bad practice [2]. Whitelists are much safer. Our task was not to fix the application, though, but to analyse the log files. 

During parsing, the line is already checked for the presence of the vulnerability and then directed to the corresponding dictionary in main. IPs and counts are being saved in the dictionaries. In the event of failed logins, timestamps are saved for later use in detecting possible brute-force attacks, which we also used from the labs [1]. 

Reports 

Lorem Ipsum generates two types of reports. Firstly, the main report, which contains all the gathered information, is generated every time the tool is launched. Secondly, users can also choose to generate a separate report showing only part of the main one. 

Before the dictionaries were ready for printing, they needed to be sorted first. We used the function sort_dict_by_value which sorted the dictionaries by descending order in number of attempts. In case of failed logins, it converted timestamps to counts as well. For recognition of type of dictionary, we used defaultdic’s attribute default_factory [7]. 

Then they are sent to generate_simple_report function. The dictionary used in the reports was simply IP addresses and the count of occurrences. In brute-force attacks, we utilized a list of dictionaries; timestamps were also printed in the reports for this particular attack. 

In the function generate_simple_report, the parts of reports are generated – failed logins, possible brute-force attacks, and SQL, LFI, and CI attacks based on the dictionaries, and in one case, a list of dictionaries made after parsing.  

In the generate_all_reports function, the previously mentioned function is used multiple times to generate the main report. The tool uses the same function to create single reports according to the user’s choice. We utilized the mode argument, which controls whether the file is being overwritten or appended to. 

We also wanted the user to see the smaller reports he asked to generate in the terminal. We encountered a challenge where the formatting differed between the .txt files and the terminal. 

We found that the .txt file and terminal display tabs were displayed differently [3], and they were used extensively in the formatting of the reports. We discovered that spaces are the same, so at the end of lines using tabs, we added the function expandtabs [4]. The view of reports in both terminals and .txt files was nice and neat. The tabs were replaced with four spaces. 

To draw graphs, we utilized the Matplotlib library and its submodules pyplot and ticker. The graphs are not generated until the user requests that the tool do so. Like the reports, the user can choose which graphs they want to develop. 

User Interface 

We optimized for speed and accuracy by designing a clear and attractive layout and interactive navigation, minimizing the time users spend manually searching for reports and graphs. Users can quickly create specific text reports or graph reports as needed, with the system only generating side reports and graphs when requested.  

This approach significantly reduces the overall execution time of the script, which when we calculated it was 153% faster to execute. 

Readability was a big factor in our programming of the UI as it shaped the entire UI system, we used functions like “os.system('clear')” from the OS library to clear the terminal from all the other unnecessary text or previous UI, to enchance the user experience and readability we also included sleep functions like “time.sleep(1)”  from the time library to allow the user to read important text like when the user inputs a wrong choice. 

This script checks if the user inputs a choice from one of the options in the if statements. If not, it clears the screen and prints “Invalid choice. Try again.” It then sleeps for 1 second to allow the user to read the error message, after which it clears the screen once again. The user can send another input that will hopefully work.   

Another feature that we added is sequences like \033[92m [6] in some areas of the text in the terminal to change the colour of the text to make it more readable and attractive. This is an example of how it can be used: print("\033[92mThis text is green!\033[0m")[6] 

We used this in the main UI and sections of the UI. We also used ASCII art [5] to enhance the visual effect of our project and coloured it using the same Python feature shown above.  

References 

[1] - MarkCummins-SETU (2025). GitHub - MarkCummins-SETU/Scripting-for-Cybersecurity: SETU Cybercrime and IT Security - Year 2 - Module Notes. [online] GitHub. Available at: https://github.com/MarkCummins-SETU/Scripting-for-Cybersecurity/tree/main  

[2] - Deri, L. and Fusco, F. (2023). Evaluating IP Blacklists Effectiveness. [online] Available at: https://arxiv.org/pdf/2308.08356. 

[3] - Stack Overflow. (2016). Tabs in txt file vs terminal. [online] Available at: https://stackoverflow.com/questions/39437725/tabs-in-txt-file-vs-terminal.  ‌ 

[4] - Vultr.com. (2024). expandtabs(). [online] Available at: https://docs.vultr.com/python/standard-library/str/expandtabs  

[5] - Image to ASCII: Free ASCII Art Converter. (n.d.). Image to ASCII: Free ASCII Art Converter. [online] Available at: https://www.asciiart.eu/image-to-ascii. 

[6] - Stack Overflow. (n.d.). python - colored text to the terminal [online] Available at: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal. 

[7] - rayo hauno (2012). How to obtain the type of the values in a defaultdict. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/9170855/how-to-obtain-the-type-of-the-values-in-a-defaultdict.  ‌  