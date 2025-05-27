from markitdown import MarkItDown

markitdown=MarkItDown()

# Path to the input PDF file
pdf_path = "D:\Converted\Python Crash Course, 3rd Edition A Ha... (Z-Library).pdf"

# Path to the output Markdown file
md_output_path = "D:\Converted\Python Crash Course, 3rd Edition A Ha... (Z-Library).md"

# Convert PDF to Markdown
markdown_text = markitdown.convert(pdf_path)

# # Save the Markdown to a file
with open(md_output_path, "w", encoding="utf-8") as f:
    f.write(markdown_text.text_content)
 
     

# print(markdown_text.text_content)