import tkinter as tk
from tkinter import filedialog, messagebox
import os
from markitdown import MarkItDown # Assuming markitdown is installed

class PdfToMarkdownConverterApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("PDF to Markdown Converter")
        self.root.geometry("600x450") # Adjusted size for better layout
        self.root.configure(bg="#f0f0f0") # Light gray background

        self.pdf_files = []
        self.output_folder = ""
        self.markitdown_converter = MarkItDown()

        # --- UI Elements ---

        # Frame for file selection
        file_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        file_frame.pack(fill=tk.X, padx=20, pady=(20,10))

        self.select_files_button = tk.Button(
            file_frame,
            text="Select PDF Files",
            command=self.select_pdf_files,
            bg="#4CAF50", # Green
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.RAISED,
            borderwidth=2,
            padx=10,
            pady=5
        )
        self.select_files_button.pack(side=tk.LEFT, padx=(0,10))

        self.selected_files_label = tk.Label(
            file_frame,
            text="No files selected",
            bg="#f0f0f0",
            fg="#333",
            font=("Arial", 10),
            wraplength=380, # Wrap text if too long
            justify=tk.LEFT
        )
        self.selected_files_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Frame for output folder selection
        output_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        output_frame.pack(fill=tk.X, padx=20, pady=10)

        self.select_output_button = tk.Button(
            output_frame,
            text="Select Output Folder",
            command=self.select_output_folder,
            bg="#2196F3", # Blue
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.RAISED,
            borderwidth=2,
            padx=10,
            pady=5
        )
        self.select_output_button.pack(side=tk.LEFT, padx=(0,10))

        self.output_folder_label = tk.Label(
            output_frame,
            text="No output folder selected",
            bg="#f0f0f0",
            fg="#333",
            font=("Arial", 10),
            wraplength=350, # Wrap text
            justify=tk.LEFT
        )
        self.output_folder_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Convert button
        self.convert_button = tk.Button(
            self.root,
            text="Convert to Markdown",
            command=self.convert_files,
            bg="#FF9800", # Orange
            fg="white",
            font=("Arial", 14, "bold"),
            relief=tk.RAISED,
            borderwidth=2,
            padx=15,
            pady=10
        )
        self.convert_button.pack(pady=20)

        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#e0e0e0",
            fg="#333",
            font=("Arial", 10)
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def select_pdf_files(self):
        """Opens a dialog to select multiple PDF files."""
        try:
            # Ask for multiple files
            # Filetypes restricts selection to PDF files
            files = filedialog.askopenfilenames(
                title="Select PDF Files",
                filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
            )
            if files:
                self.pdf_files = list(files) # Store as a list
                if len(self.pdf_files) == 1:
                    self.selected_files_label.config(text=os.path.basename(self.pdf_files[0]))
                else:
                    self.selected_files_label.config(text=f"{len(self.pdf_files)} files selected")
                self.status_label.config(text=f"{len(self.pdf_files)} PDF file(s) selected.")
            else:
                # If no files were selected (e.g., user cancelled)
                if not self.pdf_files: # Only update if no files were previously selected
                    self.selected_files_label.config(text="No files selected")
                    self.status_label.config(text="File selection cancelled.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to select files: {e}")
            self.status_label.config(text="Error selecting files.")

    def select_output_folder(self):
        """Opens a dialog to select the output directory."""
        try:
            folder = filedialog.askdirectory(title="Select Output Folder")
            if folder:
                self.output_folder = folder
                self.output_folder_label.config(text=self.output_folder)
                self.status_label.config(text=f"Output folder: {self.output_folder}")
            else:
                # If no folder was selected
                if not self.output_folder:
                     self.output_folder_label.config(text="No output folder selected")
                     self.status_label.config(text="Output folder selection cancelled.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to select output folder: {e}")
            self.status_label.config(text="Error selecting output folder.")

    def convert_files(self):
        """Converts the selected PDF files to Markdown and saves them."""
        if not self.pdf_files:
            messagebox.showwarning("Input Missing", "Please select PDF files to convert.")
            self.status_label.config(text="Warning: No PDF files selected.")
            return

        if not self.output_folder:
            messagebox.showwarning("Output Missing", "Please select an output folder.")
            self.status_label.config(text="Warning: No output folder selected.")
            return

        self.status_label.config(text="Conversion in progress...")
        self.root.update_idletasks() # Update UI to show status message

        converted_count = 0
        error_count = 0

        for pdf_path in self.pdf_files:
            try:
                self.status_label.config(text=f"Converting: {os.path.basename(pdf_path)}...")
                self.root.update_idletasks()

                # Convert PDF to Markdown using markitdown
                markdown_obj = self.markitdown_converter.convert(pdf_path)
                markdown_text = markdown_obj.text_content

                # Determine output file path
                base_name = os.path.basename(pdf_path)
                file_name_without_ext = os.path.splitext(base_name)[0]
                md_output_path = os.path.join(self.output_folder, f"{file_name_without_ext}.md")

                # Save the Markdown to a file
                with open(md_output_path, "w", encoding="utf-8") as f:
                    f.write(markdown_text)
                
                converted_count += 1
                self.status_label.config(text=f"Successfully converted: {base_name}")
                self.root.update_idletasks()

            except Exception as e:
                error_count += 1
                messagebox.showerror(
                    "Conversion Error",
                    f"Failed to convert {os.path.basename(pdf_path)}:\n{e}"
                )
                self.status_label.config(text=f"Error converting {os.path.basename(pdf_path)}.")
                self.root.update_idletasks()
                # Optionally, log the error or skip the file

        final_message = f"Conversion complete. {converted_count} file(s) converted successfully."
        if error_count > 0:
            final_message += f" {error_count} file(s) failed."
        
        messagebox.showinfo("Conversion Complete", final_message)
        self.status_label.config(text=final_message)
        
        # Optionally, clear selections after conversion
        # self.pdf_files = []
        # self.selected_files_label.config(text="No files selected")
        # self.output_folder = ""
        # self.output_folder_label.config(text="No output folder selected")


if __name__ == "__main__":
    # This check ensures the GUI runs only when the script is executed directly
    # and not when imported as a module.
    main_window = tk.Tk()
    app = PdfToMarkdownConverterApp(main_window)
    main_window.mainloop()
