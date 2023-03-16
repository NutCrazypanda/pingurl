# import requirement modules
import requests 
import time
from rich import print


webTarget = input("Enter website target : ")
# Making a get request 
delayTest = input("Time delay for each test (s) : ")
while True:
    try:
        response = requests.get(webTarget) 
        if response.ok:
            http_status = "[bold green]Successful[/bold green]"
        else:
            http_status = "[bold red]Some Problem[/bold red]"
        print(webTarget,"->",http_status,response.elapsed) 
        response.close()
    except:
        print("[yellow]Not found website. Try again..[/yellow]")
        exit()
    
    try:
        time.sleep(int(delayTest))
    except KeyboardInterrupt:
        print()
        print("[deep_pink1]Closing cPanda Ping web... Thank you.[/deep_pink1]")
        exit()
