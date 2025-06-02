import epub2txt
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class EpubConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("EPUB to TXT Converter")
        master.geometry("600x450") # Adjusted window size

        self.epub_files = []
        self.output_folder = ""

        # --- UI Elements ---

        # File Selection Frame
        file_frame = tk.Frame(master, pady=10)
        file_frame.pack(fill=tk.X)

        self.select_files_button = tk.Button(file_frame, text="Select EPUB Files", command=self.select_files, width=20)
        self.select_files_button.pack(side=tk.LEFT, padx=10)

        self.selected_files_label = tk.Label(file_frame, text="No files selected.", anchor="w", justify=tk.LEFT)
        self.selected_files_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)


        # Output Folder Selection Frame
        output_frame = tk.Frame(master, pady=10)
        output_frame.pack(fill=tk.X)

        self.select_output_button = tk.Button(output_frame, text="Select Output Folder", command=self.select_output_folder, width=20)
        self.select_output_button.pack(side=tk.LEFT, padx=10)

        self.output_folder_label = tk.Label(output_frame, text="No output folder selected.", anchor="w", justify=tk.LEFT)
        self.output_folder_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)


        # Convert Button
        self.convert_button = tk.Button(master, text="Convert Files", command=self.convert_files, state=tk.DISABLED, width=20, pady=5)
        self.convert_button.pack(pady=10)


        # Status/Log Area
        log_label = tk.Label(master, text="Log:", anchor="w")
        log_label.pack(fill=tk.X, padx=10, pady=(5,0))

        self.log_area = scrolledtext.ScrolledText(master, height=10, wrap=tk.WORD, state=tk.DISABLED)
        self.log_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.update_convert_button_state()

    def log_message(self, message):
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END) # Scroll to the end
        self.log_area.config(state=tk.DISABLED)
        self.master.update_idletasks() # Ensure UI updates immediately

    def select_files(self):
        # Ask for multiple .epub files
        selected = filedialog.askopenfilenames(
            title="Select EPUB files",
            filetypes=(("EPUB files", "*.epub"), ("All files", "*.*"))
        )
        if selected:
            self.epub_files = list(selected) # Store as a list
            if len(self.epub_files) == 1:
                self.selected_files_label.config(text=os.path.basename(self.epub_files[0]))
            else:
                self.selected_files_label.config(text=f"{len(self.epub_files)} files selected.")
            self.log_message(f"Selected {len(self.epub_files)} EPUB file(s).")
        else:
            # If selection was cancelled or empty
            if not self.epub_files: # Only update if no files were previously selected
                self.selected_files_label.config(text="No files selected.")
        self.update_convert_button_state()

    def select_output_folder(self):
        # Ask for a directory
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder = folder
            self.output_folder_label.config(text=self.output_folder)
            self.log_message(f"Output folder set to: {self.output_folder}")
        else:
            # If selection was cancelled or empty
            if not self.output_folder: # Only update if no folder was previously selected
                self.output_folder_label.config(text="No output folder selected.")
        self.update_convert_button_state()

    def update_convert_button_state(self):
        if self.epub_files and self.output_folder:
            self.convert_button.config(state=tk.NORMAL)
        else:
            self.convert_button.config(state=tk.DISABLED)

    def convert_files(self):
        if not self.epub_files:
            messagebox.showerror("Error", "No EPUB files selected.")
            return
        if not self.output_folder:
            messagebox.showerror("Error", "No output folder selected.")
            return
        if not os.path.isdir(self.output_folder):
            messagebox.showerror("Error", f"Output directory not found: {self.output_folder}")
            self.log_message(f"Error: Output directory not found: {self.output_folder}")
            return

        self.log_message("\n--- Starting Conversion ---")
        self.convert_button.config(state=tk.DISABLED) # Disable button during conversion

        conversion_successful_count = 0
        conversion_failed_count = 0

        for full_path in self.epub_files:
            filename = os.path.basename(full_path)
            self.log_message(f"Converting: {filename}")
            try:
                # --- Step 1: Extract text from EPUB ---
                res = epub2txt.epub2txt(full_path)

                # --- Step 2: Determine the output TXT filename ---
                base_filename_without_ext = os.path.splitext(filename)[0]
                txt_filename = base_filename_without_ext + ".txt"
                output_txt_path = os.path.join(self.output_folder, txt_filename)

                # --- Step 3: Save the extracted text to the TXT file ---
                self.log_message(f"Saving to: {output_txt_path}")
                with open(output_txt_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(res['title'] + "\n\n") # Include title if available
                    for chapter in res['chapters']:
                        f_out.write(chapter['title'] + "\n\n")
                        f_out.write(chapter['text'] + "\n\n")
                conversion_successful_count +=1

            except Exception as e:
                self.log_message(f"Error processing file {filename}: {e}")
                conversion_failed_count +=1

        self.log_message(f"\n--- Conversion Finished ---")
        self.log_message(f"Successfully converted: {conversion_successful_count} file(s).")
        if conversion_failed_count > 0:
            self.log_message(f"Failed to convert: {conversion_failed_count} file(s).")
        messagebox.showinfo("Process Complete", f"Finished processing all files.\nSuccessful: {conversion_successful_count}\nFailed: {conversion_failed_count}")
        self.update_convert_button_state() # Re-enable or keep disabled based on current selections

if __name__ == '__main__':
    root = tk.Tk()
    app = EpubConverterApp(root)
    root.mainloop()