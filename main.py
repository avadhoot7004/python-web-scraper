from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Web Scraper")
root.geometry("500x300")

def save_webpage_content():
    url = entry.get().strip()
    if url:
        try:
            r = requests.get(url)
            r.raise_for_status()  # Raise exception for invalid response
            
            soup = BeautifulSoup(r.content, "html.parser")
            all_text = soup.get_text(separator='\n')  # Extract only text from url
            
            save_file_name = entry_1.get().strip()
            if save_file_name:
                with open(save_file_name, "w", encoding="utf-8") as file:
                    file.write(all_text)
                status_label.config(text=f"File '{save_file_name}' saved successfully!", fg="green")
            else:
                status_label.config(text="Please provide a valid file name.", fg="red")
        except requests.exceptions.RequestException as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")
    else:
        status_label.config(text="Please provide a valid URL.", fg="red")

# Entry and Label for URL input
url_label = Label(root, text="Enter URL:", font=('Arial', 14))
url_label.pack(pady=10)
entry = Entry(root, width=50)
entry.pack()

# Entry and Label for file name input
file_label = Label(root, text="File Name:", font=('Arial', 14))
file_label.pack(pady=10)
entry_1 = Entry(root, width=50)
entry_1.pack()

# Button to save content
save_button = Button(root, text="SAVE", command=save_webpage_content)
save_button.pack(pady=20)

# Status Label to show save status
status_label = Label(root, text="", font=('Arial', 12))
status_label.pack()

root.mainloop()
