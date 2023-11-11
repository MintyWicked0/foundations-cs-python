def open_tab(tabs):
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    tab = {"title": title, "url": url}
    tabs.append(tab)
    print(title, "opened successfully.")

def close_tab(tabs):
    index = input("Enter the index of the tab you wish to close: ")
    if index == '':
        closed_tab = tabs.pop()
        print("Last opened tab was closed. Closed", closed_tab['title'])
    elif index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(tabs):
            closed_tab = tabs.pop(index)
            print("Closed ", closed_tab['title'])
        else:
            print("Invalid Tab selection. No tab closed. \nCheck the current opened tabs by selecting Display all tabs! ")
    
def switch_tab():
    print(" ")
    
def display_all_tabs():
    print(" ")

def nested_tab():
    print(" ")
    
def clear_all_tabs():
    print(" ")

def save_tabs():
    print(" ")
    
def import_tabs():
    print(" ")
    
def main():
    tabs= []
    
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
            open_tab(tabs)
        elif choice == '2':
            close_tab(tabs)
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
