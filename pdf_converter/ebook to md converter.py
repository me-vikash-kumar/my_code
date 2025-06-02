import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import shutil # For checking if pandoc is installed

try:
    import pypandoc
    PANDOC_AVAILABLE = True
    try:
        # Further check if pandoc executable is actually working
        pypandoc.get_pandoc_version()
    except OSError: # pypandoc.get_pandoc_version() raises OSError if pandoc is not found
        PANDOC_AVAILABLE = False
except ImportError:
    PANDOC_AVAILABLE = False
except FileNotFoundError: # Can also be FileNotFoundError if pandoc is not in PATH
    PANDOC_AVAILABLE = False


class EbookToMarkdownConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Ebook to Markdown (.md) Converter (using Pandoc)")
        master.geometry("700x550") # Adjusted window size

        self.input_files = []
        self.output_folder = ""

        # --- UI Elements (Create these FIRST) ---

        # File Selection Frame
        file_frame = tk.Frame(master, pady=10)
        file_frame.pack(fill=tk.X)

        self.select_files_button = tk.Button(file_frame, text="Select Ebook Files (.epub, .pdf, etc.)", command=self.select_files, width=30)
        self.select_files_button.pack(side=tk.LEFT, padx=10)

        self.selected_files_label = tk.Label(file_frame, text="No files selected.", anchor="w", justify=tk.LEFT)
        self.selected_files_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        # Output Folder Selection Frame
        output_frame = tk.Frame(master, pady=10)
        output_frame.pack(fill=tk.X)

        self.select_output_button = tk.Button(output_frame, text="Select Output Folder", command=self.select_output_folder, width=30)
        self.select_output_button.pack(side=tk.LEFT, padx=10)

        self.output_folder_label = tk.Label(output_frame, text="No output folder selected.", anchor="w", justify=tk.LEFT)
        self.output_folder_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        # Convert Button
        self.convert_button = tk.Button(master, text="Convert to Markdown", command=self.convert_files, state=tk.DISABLED, width=30, pady=5)
        self.convert_button.pack(pady=10)

        # Status/Log Area
        log_label = tk.Label(master, text="Log:", anchor="w")
        log_label.pack(fill=tk.X, padx=10, pady=(5,0))

        self.log_area = scrolledtext.ScrolledText(master, height=15, wrap=tk.WORD, state=tk.DISABLED)
        self.log_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # NOW check Pandoc status (after log_area is created)
        self.pandoc_is_ready = self._check_pandoc_on_startup()

        # Pandoc Status Label (create after checking status)
        pandoc_status_text = "Pandoc Status: Ready" if self.pandoc_is_ready else "Pandoc Status: NOT FOUND/ACCESSIBLE. Please install Pandoc."
        pandoc_status_color = "green" if self.pandoc_is_ready else "red"
        self.pandoc_status_label = tk.Label(master, text=pandoc_status_text, fg=pandoc_status_color, pady=5)
        self.pandoc_status_label.pack(fill=tk.X, before=file_frame)  # Insert at top
        
        if not self.pandoc_is_ready:
            self.pandoc_warning_label = tk.Label(master, text="Conversion will likely fail. See console/README for Pandoc installation.", fg="red")
            self.pandoc_warning_label.pack(fill=tk.X, before=file_frame)  # Insert at top

        self.update_convert_button_state()

    def _check_pandoc_on_startup(self):
        """Checks if pandoc is installed and accessible."""
        global PANDOC_AVAILABLE # Use the globally determined status
        if not PANDOC_AVAILABLE:
            self.log_message("--- IMPORTANT ---")
            self.log_message("Pandoc library (pypandoc) was imported, but Pandoc executable might be missing or not in PATH.")
            self.log_message("Please ensure Pandoc is correctly installed on your system.")
            self.log_message("Download from https://pandoc.org/installing.html")
            self.log_message("Conversion will likely fail without Pandoc.")
            self.log_message("-------------------")
            return False
        else:
            try:
                version = pypandoc.get_pandoc_version()
                self.log_message(f"Pandoc version {version} found and accessible.")
                return True
            except Exception as e: # Catch any error during version check
                self.log_message(f"Error checking Pandoc version: {e}")
                self.log_message("Pandoc might not be correctly configured even if pypandoc imported.")
                PANDOC_AVAILABLE = False # Update global status
                return False

    def log_message(self, message):
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END) # Scroll to the end
        self.log_area.config(state=tk.DISABLED)
        self.master.update_idletasks() # Ensure UI updates immediately

    def select_files(self):
        # Supported file types for Pandoc (common ones)
        filetypes = (
            ("Ebook files", "*.epub *.pdf *.mobi *.azw3 *.fb2 *.html *.docx *.odt"),
            ("EPUB files", "*.epub"),
            ("PDF files", "*.pdf"),
            ("MOBI files", "*.mobi"),
            ("HTML files", "*.html *.htm"),
            ("Word files", "*.docx"),
            ("OpenDocument Text", "*.odt"),
            ("All files", "*.*")
        )
        selected = filedialog.askopenfilenames(
            title="Select Ebook files",
            filetypes=filetypes
        )
        if selected:
            self.input_files = list(selected) # Store as a list
            if len(self.input_files) == 1:
                self.selected_files_label.config(text=os.path.basename(self.input_files[0]))
            else:
                self.selected_files_label.config(text=f"{len(self.input_files)} files selected.")
            self.log_message(f"Selected {len(self.input_files)} file(s).")
        else:
            if not self.input_files:
                self.selected_files_label.config(text="No files selected.")
        self.update_convert_button_state()

    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Select Output Folder for .md files")
        if folder:
            self.output_folder = folder
            self.output_folder_label.config(text=self.output_folder)
            self.log_message(f"Output folder set to: {self.output_folder}")
        else:
            if not self.output_folder:
                self.output_folder_label.config(text="No output folder selected.")
        self.update_convert_button_state()

    def update_convert_button_state(self):
        if self.input_files and self.output_folder and self.pandoc_is_ready:
            self.convert_button.config(state=tk.NORMAL)
        else:
            self.convert_button.config(state=tk.DISABLED)

    def convert_files(self):
        if not self.pandoc_is_ready:
            messagebox.showerror("Pandoc Error", "Pandoc is not available or not configured correctly. Please install or check Pandoc.")
            self.log_message("Conversion aborted: Pandoc not ready.")
            return

        if not self.input_files:
            messagebox.showerror("Error", "No input files selected.")
            return
        if not self.output_folder:
            messagebox.showerror("Error", "No output folder selected.")
            return
        if not os.path.isdir(self.output_folder):
            messagebox.showerror("Error", f"Output directory not found: {self.output_folder}")
            self.log_message(f"Error: Output directory not found: {self.output_folder}")
            return

        self.log_message("\n--- Starting Conversion to Markdown ---")
        self.convert_button.config(state=tk.DISABLED)

        conversion_successful_count = 0
        conversion_failed_count = 0

        for full_path in self.input_files:
            filename = os.path.basename(full_path)
            file_base, file_ext = os.path.splitext(filename)
            input_format = file_ext.lstrip('.').lower() # Determine format from extension

            if not input_format: # Should not happen if file has extension
                self.log_message(f"Skipping file with no extension: {filename}")
                conversion_failed_count += 1
                continue

            self.log_message(f"Processing: {filename} (Detected format: {input_format})")
            try:
                md_filename = file_base + ".md"
                output_md_path = os.path.join(self.output_folder, md_filename)

                # Pandoc arguments for good Markdown output for AI
                # 'markdown' is Pandoc's extended markdown.
                # 'gfm' (GitHub Flavored Markdown) is also a good option.
                # --wrap=none: Prevents Pandoc from hard-wrapping lines, good for AI processing.
                # --strip-comments: Removes HTML/XML comments.
                extra_args = ['--wrap=none', '--strip-comments', '--markdown-headings=atx']

                self.log_message(f"Converting with Pandoc to: {output_md_path}")
                pypandoc.convert_file(
                    source_file=full_path,
                    to='markdown',  # Target general Markdown, or 'gfm' for GitHub Flavored
                    format=input_format, # Let Pandoc infer or specify if needed e.g. 'epub', 'pdf'
                    outputfile=output_md_path,
                    extra_args=extra_args
                )
                self.log_message(f"Successfully saved: {output_md_path}")
                conversion_successful_count +=1

            except RuntimeError as e: # pypandoc raises RuntimeError for Pandoc errors
                self.log_message(f"Pandoc Error processing file {filename}: {e}")
                self.log_message("Ensure Pandoc supports the input format and the file is not corrupted.")
                conversion_failed_count +=1
            except Exception as e:
                self.log_message(f"Unexpected error processing file {filename}: {e}")
                conversion_failed_count +=1

        self.log_message(f"\n--- Conversion Finished ---")
        self.log_message(f"Successfully converted: {conversion_successful_count} file(s).")
        if conversion_failed_count > 0:
            self.log_message(f"Failed to convert: {conversion_failed_count} file(s).")
        messagebox.showinfo("Process Complete", f"Finished processing files.\nSuccessful: {conversion_successful_count}\nFailed: {conversion_failed_count}")
        self.update_convert_button_state()

if __name__ == '__main__':
    root = tk.Tk()
    app = EbookToMarkdownConverterApp(root)
    root.mainloop()