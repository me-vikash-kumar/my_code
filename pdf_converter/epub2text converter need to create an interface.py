import epub2txt
import os

# Define the directory containing the EPUB files
epub_dir = r"DIRECTORY e.g. c:\files\etc"

# Check if the directory exists
if not os.path.isdir(epub_dir):
    print(f"Error: Directory not found: {epub_dir}")
else:
    print(f"Processing files in: {epub_dir}")
    # Iterate through the items in the directory
    for filename in os.listdir(epub_dir):
        # Construct the full path to the potential EPUB file
        full_path = os.path.join(epub_dir, filename)

        # Check if it's an EPUB file (and not a directory)
        if filename.lower().endswith('.epub') and os.path.isfile(full_path):
            print(f"Converting: {filename}")
            try:
                # --- Step 1: Extract text from EPUB ---
                res = epub2txt.epub2txt(full_path)

                # --- Step 2: Determine the output TXT filename ---
                # Get the full path without the .epub extension
                base_path_without_ext = os.path.splitext(full_path)[0]
                # Create the new filename by adding .txt
                txt_filename = base_path_without_ext + ".txt"

                # --- Step 3: Save the extracted text to the TXT file ---
                print(f"Saving to: {txt_filename}")
                # Open the txt file in write mode ('w') with UTF-8 encoding
                with open(txt_filename, 'w', encoding='utf-8') as f_out:
                    # Write the extracted text content (stored in 'res') to the file
                    f_out.write(res)

            except Exception as e:
                # Print an error message if conversion or saving fails for a file
                print(f"Error processing file {filename}: {e}")
        # else:
            # Optional: uncomment the line below to see which items are skipped
            # print(f"Skipping non-epub file or directory: {filename}")

    print("\nFinished processing all files.")