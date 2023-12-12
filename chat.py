from tkinter import *
import customtkinter 
import openai 

import os 
import pickle

# Read the API key from the file
api_key_filename = "api_key"

if os.path.isfile(api_key_filename):
    with open(api_key_filename, "rb") as api_key_file:
        api_key = pickle.load(api_key_file)
else:
    api_key = None

# Initialize the OpenAI client with the API key
openai.api_key = api_key



# iniatitation of the app 
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry("600x500")
root.iconbitmap("ai_lt.ico")

# set color scheme 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# function to submit the entry_frame to chatGPT
# function to submit the entry_frame to chatGPT
def speak_with_GPT():
    if entry_frame.get():
        try:
            # Query the API ChatGPT
            response = openai.Completion.create(
                engine="text-davinci-002",  # Choose the appropriate engine
                prompt=entry_frame.get(),
                max_tokens=150,
            )

            # Display the response in the text widget
            text.insert(END, f"\n\nChatGPT: {response['choices'][0]['text']}")
        except Exception as e:
            text.insert(END, f"\n\nThere was an error \n\n {e}")
    else:
        text.insert(END, "\n\n Hey! :) Please submit a message to ChatGPT ! ")


    


# Clear the screens 
def clear():
    # Clear the main text box
    text.delete(1.0, END)
    # Clear the query entry box 
    entry_frame.delete(0, END)

# Call API 
def update_api():
    # Define our filename
    filename = "api_key"

    try:
        # Check to see if the file exists
        if os.path.isfile(filename):
            # Open the file
            input_file = open(filename, "rb")

            # Load the data from the file into a variable
            variable = pickle.load(input_file)

            # Output variable to entry box
            api_entry.insert(END, variable)
        else:
            # Create the file
            input_file = open(filename, "wb")
            #close the file
            input_file.close()
    except Exception as e:
        text.insert(END, f"\n\nThere was an error \n\n {e}")

    # Resize the window
    root.geometry("600x600")
    # Reshow the API frame
    api_frame.pack(pady=20)



# Save API key
def save_api_key():
    # Define our filename
    filename = "api_key"

    try:
        # Open the file
        output_file = open(filename, "wb")

        # Add the data to the file
        pickle.dump(api_entry.get(), output_file)

        # Delete the entry box
        api_entry.delete(0, END)

        #hide API frame
        api_frame.pack_forget()
        # Resize the window
        root.geometry("600x500")
    except Exception as e:
        text.insert(END, f"\n\nThere was an error \n\n {e}")


# create a frame for the text
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)


# add text widget to get chat GPT response
text = Text(text_frame, bg="#343638", width=80, bd=1, fg="#d6d6d6", relief="flat", height=20, font=("Arial", 12), wrap="word")
text.grid(row=0, column=0)

# add scrollbar to the text widget
text_scroll = Scrollbar(text_frame, troughcolor="#343638", bg="#343638", bd=0, highlightthickness=0, activebackground="#343638")
text_scroll.grid(row=0, column=1, sticky="ns")

# configure the text widget to use the scrollbar
text.config(yscrollcommand=text_scroll.set)
text_scroll.config(command=text.yview)

# create a frame for the entry box
entry_frame = customtkinter.CTkEntry(root, placeholder_text="Enter your message to ChatGPT here...", width=580, height=50, border_width=1)
entry_frame.pack(pady=20)

# button frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=20)

# button to submit the entry to chat GPT
submit_button = customtkinter.CTkButton(button_frame, text="Submit to ChatGPT", command=speak_with_GPT)
submit_button.grid(row=0, column=0, padx=25)

# button to clear the screen
clear_button = customtkinter.CTkButton(button_frame, text="Clear Response", command=clear)
clear_button.grid(row=0, column=1, padx=35)

# button to update the API
api_button = customtkinter.CTkButton(button_frame, text="Update the API", command=update_api)
api_button.grid(row=0, column=2, padx=25)


# add API key frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=20)

# add API entry widget
api_entry = customtkinter.CTkEntry(api_frame, placeholder_text="Enter your API key here...", width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=10, pady=10)

#  API save button
api_save_button = customtkinter.CTkButton(api_frame, text="Save API Key", command=save_api_key)
api_save_button.grid(row=0, column=1, padx=10)

# main loop
root.mainloop()