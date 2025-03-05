import tkinter as tk
from tkinter import scrolledtext

class TextEditorWithLineNumbers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)

        # Create the main frame
        self.text_frame = tk.Frame(self)
        self.text_frame.pack(fill=tk.BOTH, expand=True)

        # Line numbers text widget
        self.line_numbers = tk.Text(self.text_frame, width=4, padx=5, wrap="none", bg="lightgray", state="disabled")
        self.line_numbers.pack(side="left", fill=tk.Y)

        # Main text area with scroll
        self.text_area = scrolledtext.ScrolledText(self.text_frame, wrap="none")
        self.text_area.pack(side="right", fill=tk.BOTH, expand=True)

        # Bind event to update line numbers
        self.text_area.bind("<KeyRelease>", self.update_line_numbers)
        self.text_area.bind("<MouseWheel>", self.update_line_numbers)
        self.text_area.bind("<FocusIn>", self.update_line_numbers)

        # Initialize line numbers
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", tk.END)

        # Get number of lines in text widget
        num_lines = self.text_area.index("end-1c").split(".")[0]
        line_numbers_string = "\n".join(str(i) for i in range(1, int(num_lines) + 1))

        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.config(state="disabled")

# Create the Tkinter window
root = tk.Tk()
root.title("ScrolledText with Line Numbers")
editor = TextEditorWithLineNumbers(root)
root.mainloop()
