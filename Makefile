main:
	latexmk
clean:
	latexmk -c
build:
	latexmk -bibtex-cond1

build-gh-page:
	mkdir -p gh-pages/files
	cp output/*.pdf gh-pages/files/
	touch gh-pages/index.html
	python3 generate_gh_page.py
	tar -czf gh-pages.tar.gz gh-pages
