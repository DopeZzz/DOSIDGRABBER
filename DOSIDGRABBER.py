import requests
from bs4 import BeautifulSoup
import getpass

#Thanks Yuuki for showing me how to do this with requests!!! <33333

def fancy_print():
    ascii_art = """
██████╗  ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ███████╗██╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██╔════╝╚══███╔╝╚══███╔╝╚══███╔╝    ██╔════╝██║██╔══██╗
██║  ██║██║   ██║██████╔╝█████╗    ███╔╝   ███╔╝   ███╔╝     ███████╗██║██║  ██║
██║  ██║██║   ██║██╔═══╝ ██╔══╝   ███╔╝   ███╔╝   ███╔╝      ╚════██║██║██║  ██║
██████╔╝╚██████╔╝██║     ███████╗███████╗███████╗███████╗    ███████║██║██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝╚══════╝    ╚══════╝╚═╝╚═════╝ 
                                                                                    
    """
    print(ascii_art)

def get_user_input():
    fancy_print()
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    password_asterisks = '*' * len(password)
    print(f"Password: {password_asterisks}")
    return username, password

def obtain_sid(username, password):
    session = requests.Session()
    url = "https://darkorbit.com"
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    login_form = soup.find("form", {"name": "bgcdw_login_form"})
    action_url = login_form.get("action")
    payload = {
        "username": username,
        "password": password
    }
    login_response = session.post(action_url, data=payload)
    cookie_dosid = login_response.cookies.get("dosid")
    sid = None
    if cookie_dosid:
        sid = cookie_dosid
    current_url = login_response.url
    server = current_url.split("//")[1].split(".")[0]
    return sid, server


def main():
    username, password = get_user_input()
    sid, server = obtain_sid(username, password)
    print(f"SID: {sid}")
    print(f"Server: {server}")
    input("Press any key and then 'Enter' to close...")

if __name__ == "__main__":
    main()

