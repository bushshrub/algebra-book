import os
import pathlib

if __name__ == "__main__":
    pdf_files = list(filter(lambda x: x.endswith(".pdf"), os.listdir("gh-pages/files")))
    pathlib.Path("gh-pages/index.html").touch()

    
    with open("gh-pages/index.html", "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write('''
                <html>
                <head>
                <style>
                
        body {
            font-size: 20pt;
        }
        @media (prefers-color-scheme: dark) {
            body {
                background-color: black;
                color: #fdfdfd;
            }
            a {
                color: #ffe666;
                text-decoration: none;
            }
            a:hover {
                background: #424242;
                color: #fdfdfd;
                text-decoration: underline;
            }
        }

                </style>
                </head>
                ''')
        f.write("<body>\n")
        f.write("<h1>Algebra Book Build Files</h1>\n")
        current_git_commit_hash = os.popen("git rev-parse --short HEAD").read().strip()
        last_commit_dt = os.popen('git log -1 --date=format:"%Y/%m/%d %T" --format="%ad"').read().strip()
        f.write(f"<p>Current git commit hash: {current_git_commit_hash}</p>\n")
        f.write(f"<p>Last commit time: {last_commit_dt}</p>\n")

        f.write('<h2>Download</h2>\n')
        f.write('<a href="files/main.pdf">Main Document</a>\n')
        f.write('<h2>Other files</h2>\n')
        f.write('<ul>')
        for pdf_file in pdf_files:
            f.write(f'<li><a href="files/{pdf_file}">{pdf_file}</a></li>\n')
        f.write('</ul>')
        f.write("</body>\n</html>")

