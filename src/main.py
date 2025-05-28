from google import genai as genai
from config import api_key
import tkinter as tk
from tkinter import ttk

client = genai.Client(api_key=api_key)

# function for text summarization
def summarize_text(text):
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Summarize the following text: {text}"
    )
    return res.text


# function for creating the basic GUI using Tkinter
def create_gui():
    root = tk.Tk()
    root.title("Content Summarizer")
    
    # To position the window at the center of the screen
    window_width = 900
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    
    # Configuration of the grid layout
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    
    text_label = ttk.Label(root, text="Enter the text to summarize:")
    text_label.grid(row=0, column=0, padx=20, pady=20, sticky='e')
    
    text_entry = ttk.Entry(root, width=50)
    text_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    
    summary_label = ttk.Label(root, text="Summary:")
    summary_label.grid(row=1, column=0, padx=10, pady=10, sticky='ne')
    
    summary_text = tk.Text(root, width=50, height=20, wrap=tk.WORD)
    summary_text.grid(row=1, column=1, padx=10, pady=10, sticky='nw')
    
    text_word_count_label = ttk.Label(root, text="Original Text's Word Count: 0")
    text_word_count_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    
    summary_word_count_label = ttk.Label(root, text="Summarized Text's Word Count: 0")
    summary_word_count_label.grid(row=2, column=1, padx=10, pady=10, sticky='e')
    
    
    # function to display the summarized text on the window
    def summarize():
        text = text_entry.get()
        
        summary = "Summarized text will appear here:"
        summary = summarize_text(text)
        summary_text.delete(1.0, tk.END)
        summary_text.insert(tk.END, summary)
        
        text_word_count = len(text.split())
        summary_word_count = len(summary.split())
        text_word_count_label.config(text=f"Original Text's Word Count: {text_word_count}")
        summary_word_count_label.config(text=f"Summarized Text's Word Count: {summary_word_count}")
    
    
    summarize_button = ttk.Button(root, text="Summarize", command=summarize)
    summarize_button.grid(row=3, column=0, columnspan=2, pady=20)
    
    root.mainloop()


if __name__ == "__main__":
    create_gui()