main:
	mkdir -p output/
	latexmk
	mv *.pdf output/
clean:
	latexmk -c
build:
	latexmk -bibtex-cond1
	mv *.pdf output/