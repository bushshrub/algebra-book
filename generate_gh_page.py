import os

if __name__ == "__main__":
    # List all pdf files in "gh-pages/files"
    pdf_files = list(filter(os.listdir("gh-pages/files"), lambda x: x.endswith(".pdf")))
    # Generate the index.html file
    with open("gh-pages/index.html", "w") as f:
        f.write("<html><body>")
        f.write("<h1>PDF files</h1>")
        for pdf_file in pdf_files:
            f.write(f'<a href="files/{pdf_file}">{pdf_file}</a><br>')
        f.write("</body></html>")

