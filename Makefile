TARGET?=kgorman.pdf

pdf: 
	xelatex kgorman

bib: pdf
	bibtex kgorman
	xelatex kgorman
	xelatex kgorman

clean:
	rm -f *.aux *.toc *.log *.lot *.pdf

show: kgorman.pdf
	pdf kgorman.pdf & 
