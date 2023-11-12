import json

tabs= {}
open_tabs = []

def open_tab():
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    tab = {"title": title, "url": url}
    open_tabs.append(tab)
    print(title, "opened successfully.")

def close_tab():
    index = input("Enter the index of the tab you wish to close: ")
    if index == '':
        closed_tab = open_tabs.pop()
        print("Last opened tab was closed. Closed", closed_tab["title"])
    elif index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(open_tabs):
            closed_tab = open_tabs.pop(index)
            print("Closed", closed_tab["title"])
        else:
            print("Invalid Tab selection. No tab closed. \nCheck the current opened tabs by selecting Display all tabs!")
    else:
        print("No tabs to close.")#If the input is neither empty nor a valid digit.
    
def switch_tab():
    index = input("Enter the index of the tab you wish to switch to: ")
    if index == "":
        current_tab = open_tabs[-1]#If the input is empty set the current tab to the last tab in the list
    else:
        current_tab = open_tabs[int(index)]#Set the current tab to the tab at the index provided by the user
    print(current_tab["title"])
    print(current_tab["url"]) 
    
def display_all_tabs(): #resource: https://realpython.com/python-enumerate/
    for i, t in enumerate(open_tabs):#used enumerate to be able to use 
        print("Tab", i + 1)          #count and displaying the items
        print("Title:", t["title"])
        print("URL:", t["url"])
        print("Nested Tabs:")
        for j, k in enumerate(t["tabs"]):
            print("Tab", j + 1)
            print("Title:", k["title"])
            print("URL:", k["url"])

def nested_tab():
    index = input("Enter index of parent tab where nested tab will be inserted: ")
    title = input("Enter title: ")
    url = input("Enter URL: ")
    tab = {"title": title, "url": url, "tabs": []}
    open_tabs[int(index)]["tabs"].append(tab)
    
def clear_all_tabs():
    open_tabs.clear()

def save_tabs(): #https://stackoverflow.com/questions/7771011/how-can-i-parse-read-and-use-json-in-python
    #https://www.geeksforgeeks.org/json-with-python/
    file_path = input("Enter file path to save tabs: ")
    
    # Open the specified file in write mode ("w")
    # and use the 'with' statement to ensure proper handling of the file
    with open(file_path, "w") as file:
        json.dump(open_tabs, file)#giving me an error every time I run it
        #"PermissionError: [Errno 13] Permission denied: 'C:\\Users\\malek\\Desktop\\GitHub\\foundations-cs-python\\Midterm'"
    
def import_tabs():
    print(" ")
    
def main():
    while True:
        print("1. Open Tab")
        print("2. Close Tab")
        print("3. Switch Taab")
        print("4. Displat all tabs")
        print("5. Open nested tabs")
        print("6. Clear All Tabs")
        print("7. Save Tabs")
        print("8. Import Tabs")
        print("9. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            open_tab()
        elif choice == '2':
            close_tab()
        elif choice == '3':
            switch_tab()
        elif choice == '4':
            display_all_tabs()
        elif choice == '5': 
            nested_tab()
        elif choice == '6':
            clear_all_tabs()
        elif choice == '7':
            save_tabs()
        elif choice == '8':
            import_tabs()
        elif choice == '9':
            print("End of the Program! \nBye!")
            break
        else:
            print("This number is out of range! \nPlease enter a valid number from 1 to 9.")
               
main()
