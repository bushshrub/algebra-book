main:
	latexmk
clean:
	latexmk -c
build:
	latexmk -bibtex-cond1

build-gh-page:
	mkdir -p gh-pages/files
	cp output/*.pdf gh-pages/files/
	python3 generate_gh_page.py
	tar -czf gh-pages.tar.gz gh-pages/
	tar -ztvf gh-pages.tar.gz

clean-gh-page:
	rm -rf gh-pages
	rm -f gh-pages.tar.gz
