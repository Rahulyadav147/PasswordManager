import getpass
import tkinter as tk

def store_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    info_file = open('info.txt', 'a')
    info_file.write(f'{website},{username},{password}\n')
    info_file.close()
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    status_label.config(text='Information stored successfully!')

def retrieve_info():
    website = website_entry.get()
    info_file = open('info.txt', 'r')
    found = False
    for line in info_file:
        if website in line:
            values = line.strip().split(',', 2)
            if len(values) == 3:
                website, username, password = values
                found = True
                break
    info_file.close()
    if found:
        # Create a new window to display the username and password
        info_window = tk.Toplevel(root)
        info_window.title('Information for ' + website)
        username_label = tk.Label(info_window, text='Username: ' + username)
        username_label.pack(padx=10, pady=10)
        password_label = tk.Label(info_window, text='Password: ' + password)
        password_label.pack(padx=10, pady=10)
    else:
        status_label.config(text=f'Error: no information found for {website}')
    website_entry.delete(0, tk.END)



root = tk.Tk()
root.title('Password Manager')

website_label = tk.Label(root, text='Website:')
website_label.grid(row=0, column=0, sticky='e')
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=5, pady=5)

username_label = tk.Label(root, text='Username:')
username_label.grid(row=1, column=0, sticky='e')
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(root, text='Password:')
password_label.grid(row=2, column=0, sticky='e')
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=2, column=1, padx=5, pady=5)

store_button = tk.Button(root, text='Store', command=store_info)
store_button.grid(row=3, column=0, padx=5, pady=5)

retrieve_button = tk.Button(root, text='Retrieve', command=retrieve_info)
retrieve_button.grid(row=3, column=1, padx=5, pady=5)

status_label = tk.Label(root, text='', fg='green')
status_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

