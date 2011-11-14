TARGET?=kgorman.pdf

pdf: 
	pdflatex kgorman

bib: kgorman.pdf
	bibtex kgorman
	pdflatex kgorman
	pdflatex kgorman

clean:
	rm -f *.aux *.toc *.log *.lot *.pdf

show: kgorman.pdf
	pdf kgorman.pdf & 
