import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import shutil
import tempfile
from markitdown import MarkItDown # Assuming markitdown is installed

class PdfToMarkdownConverterApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("PDF to Markdown Converter with Pre-processing")
        self.root.geometry("700x550") # Increased size for additional options
        self.root.configure(bg="#f0f0f0") # Light gray background

        self.pdf_files = []
        self.output_folder = ""
        self.markitdown_converter = MarkItDown()
        
        # Check for available preprocessing tools
        self.available_tools = self.check_preprocessing_tools()

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

        # Pre-processing options frame
        preprocess_frame = tk.LabelFrame(
            self.root,
            text="PDF Pre-processing Options",
            bg="#f0f0f0",
            fg="#333",
            font=("Arial", 11, "bold"),
            pady=10,
            padx=10
        )
        preprocess_frame.pack(fill=tk.X, padx=20, pady=10)

        # Enable preprocessing checkbox
        self.enable_preprocessing = tk.BooleanVar(value=True)
        self.preprocess_checkbox = tk.Checkbutton(
            preprocess_frame,
            text="Enable PDF Pre-processing (improves conversion quality)",
            variable=self.enable_preprocessing,
            bg="#f0f0f0",
            fg="#333",
            font=("Arial", 10),
            command=self.toggle_preprocessing_options
        )
        self.preprocess_checkbox.pack(anchor=tk.W, pady=(0,10))

        # Tool selection frame
        tool_frame = tk.Frame(preprocess_frame, bg="#f0f0f0")
        tool_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            tool_frame,
            text="Pre-processing tool:",
            bg="#f0f0f0",
            fg="#333",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0,10))

        self.preprocessing_tool = tk.StringVar()
        self.tool_combobox = ttk.Combobox(
            tool_frame,
            textvariable=self.preprocessing_tool,
            state="readonly",
            font=("Arial", 10),
            width=25
        )
        self.tool_combobox.pack(side=tk.LEFT)

        # Tool status label
        self.tool_status_label = tk.Label(
            preprocess_frame,
            text="",
            bg="#f0f0f0",
            fg="#666",
            font=("Arial", 9),
            wraplength=600
        )
        self.tool_status_label.pack(anchor=tk.W, pady=(5,0))

        # Populate tool options based on availability
        self.update_tool_options()

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

        # Progress bar
        self.progress = ttk.Progressbar(
            self.root,
            mode='determinate',
            length=400
        )
        self.progress.pack(pady=(0,10))

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

        # Initialize UI state
        self.toggle_preprocessing_options()

    def check_preprocessing_tools(self):
        """Check which preprocessing tools are available on the system."""
        tools = {}
        
        # Check for qpdf
        try:
            result = subprocess.run(['qpdf', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                tools['qpdf'] = True
            else:
                tools['qpdf'] = False
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            tools['qpdf'] = False

        # Check for Ghostscript (gs)
        try:
            result = subprocess.run(['gs', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                tools['ghostscript'] = True
            else:
                tools['ghostscript'] = False
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            tools['ghostscript'] = False

        return tools

    def update_tool_options(self):
        """Update the tool combobox based on available tools."""
        options = []
        
        if self.available_tools.get('qpdf', False):
            options.append("qpdf (recommended)")
        
        if self.available_tools.get('ghostscript', False):
            options.append("Ghostscript")
        
        if not options:
            options.append("No tools available")
            self.tool_status_label.config(
                text="⚠️ No preprocessing tools found. Install qpdf or Ghostscript for better results.",
                fg="#d32f2f"
            )
        else:
            available_tools_text = []
            if self.available_tools.get('qpdf', False):
                available_tools_text.append("qpdf")
            if self.available_tools.get('ghostscript', False):
                available_tools_text.append("Ghostscript")
            
            self.tool_status_label.config(
                text=f"✓ Available tools: {', '.join(available_tools_text)}",
                fg="#2e7d32"
            )

        self.tool_combobox['values'] = options
        if options and options[0] != "No tools available":
            self.tool_combobox.current(0)

    def toggle_preprocessing_options(self):
        """Enable/disable preprocessing options based on checkbox state."""
        if self.enable_preprocessing.get():
            self.tool_combobox.config(state="readonly")
        else:
            self.tool_combobox.config(state="disabled")

    def preprocess_pdf(self, input_path, temp_dir):
        """Pre-process a PDF file using the selected tool."""
        if not self.enable_preprocessing.get():
            return input_path

        selected_tool = self.preprocessing_tool.get()
        
        if "No tools available" in selected_tool:
            return input_path

        # Create a temporary file for the cleaned PDF
        base_name = os.path.basename(input_path)
        temp_output_path = os.path.join(temp_dir, f"cleaned_{base_name}")

        try:
            if "qpdf" in selected_tool and self.available_tools.get('qpdf', False):
                # Use qpdf for linearization and cleaning
                cmd = ['qpdf', '--linearize', input_path, temp_output_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                
                if result.returncode != 0:
                    raise subprocess.SubprocessError(f"qpdf error: {result.stderr}")

            elif "Ghostscript" in selected_tool and self.available_tools.get('ghostscript', False):
                # Use Ghostscript for cleaning
                cmd = [
                    'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    f'-sOutputFile={temp_output_path}', input_path
                ]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                
                if result.returncode != 0:
                    raise subprocess.SubprocessError(f"Ghostscript error: {result.stderr}")

            # Verify the output file was created and is valid
            if os.path.exists(temp_output_path) and os.path.getsize(temp_output_path) > 0:
                return temp_output_path
            else:
                raise FileNotFoundError("Pre-processed file was not created properly")

        except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError) as e:
            # If preprocessing fails, return the original file
            self.status_label.config(text=f"Pre-processing failed for {base_name}, using original")
            return input_path

    def select_pdf_files(self):
        """Opens a dialog to select multiple PDF files."""
        try:
            files = filedialog.askopenfilenames(
                title="Select PDF Files",
                filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
            )
            if files:
                self.pdf_files = list(files)
                if len(self.pdf_files) == 1:
                    self.selected_files_label.config(text=os.path.basename(self.pdf_files[0]))
                else:
                    self.selected_files_label.config(text=f"{len(self.pdf_files)} files selected")
                self.status_label.config(text=f"{len(self.pdf_files)} PDF file(s) selected.")
            else:
                if not self.pdf_files:
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

        # Setup progress bar
        self.progress['maximum'] = len(self.pdf_files)
        self.progress['value'] = 0

        self.status_label.config(text="Starting conversion...")
        self.root.update_idletasks()

        converted_count = 0
        error_count = 0

        # Create a temporary directory for preprocessing
        with tempfile.TemporaryDirectory() as temp_dir:
            for i, pdf_path in enumerate(self.pdf_files):
                try:
                    base_name = os.path.basename(pdf_path)
                    
                    # Pre-processing step
                    if self.enable_preprocessing.get():
                        self.status_label.config(text=f"Pre-processing: {base_name}...")
                        self.root.update_idletasks()
                        processed_pdf_path = self.preprocess_pdf(pdf_path, temp_dir)
                    else:
                        processed_pdf_path = pdf_path

                    # Conversion step
                    self.status_label.config(text=f"Converting: {base_name}...")
                    self.root.update_idletasks()

                    # Convert PDF to Markdown using markitdown
                    markdown_obj = self.markitdown_converter.convert(processed_pdf_path)
                    markdown_text = markdown_obj.text_content

                    # Determine output file path
                    file_name_without_ext = os.path.splitext(base_name)[0]
                    md_output_path = os.path.join(self.output_folder, f"{file_name_without_ext}.md")

                    # Save the Markdown to a file
                    with open(md_output_path, "w", encoding="utf-8") as f:
                        f.write(markdown_text)
                    
                    converted_count += 1
                    self.status_label.config(text=f"Successfully converted: {base_name}")
                    
                    # Update progress bar
                    self.progress['value'] = i + 1
                    self.root.update_idletasks()

                except Exception as e:
                    error_count += 1
                    messagebox.showerror(
                        "Conversion Error",
                        f"Failed to convert {os.path.basename(pdf_path)}:\n{str(e)[:200]}..."
                    )
                    self.status_label.config(text=f"Error converting {os.path.basename(pdf_path)}.")
                    
                    # Update progress bar even on error
                    self.progress['value'] = i + 1
                    self.root.update_idletasks()

        final_message = f"Conversion complete. {converted_count} file(s) converted successfully."
        if error_count > 0:
            final_message += f" {error_count} file(s) failed."
        
        messagebox.showinfo("Conversion Complete", final_message)
        self.status_label.config(text=final_message)
        
        # Reset progress bar
        self.progress['value'] = 0


if __name__ == "__main__":
    main_window = tk.Tk()
    app = PdfToMarkdownConverterApp(main_window)
    main_window.mainloop()