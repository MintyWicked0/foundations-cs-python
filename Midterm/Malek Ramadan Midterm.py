tabs= {}
open_tabs = []

def open_tab():
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    tabs = {"title": title, "url": url}
    open_tabs.append(tabs)
    print(title, "opened successfully.")

def close_tab():
    index = input("Enter the index of the tab you wish to close: ")
    if index == '':
        closed_tab = open_tabs.pop()
        print("Last opened tab was closed. Closed", closed_tab['title'])
    elif index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(open_tabs):
            closed_tab = open_tabs.pop(index)
            print("Closed", closed_tab['title'])
        else:
            print("Invalid Tab selection. No tab closed. \nCheck the current opened tabs by selecting Display all tabs!")
    else:
        print("No tabs to close.")
    
def switch_tab():
    index = input("Enter the index of the tab you wish to switch to: ")
    if index == "":
        current_tab = open_tabs[-1]
    else:
        current_tab = open_tabs[int(index)]
    print(current_tab["title"])
    print(current_tab["url"]) 
    
def display_all_tabs():
    print(" ")

def nested_tab():
    print(" ")
    
def clear_all_tabs():
    open_tabs.clear()

def save_tabs():
    print(" ")
    
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
