TARGET?=kgorman.pdf

pdf: 
	xelatex kgorman

bib: kgorman.pdf
	bibtex kgorman
	xelatex kgorman
	xelatex kgorman

clean:
	rm -f *.aux *.toc *.log *.lot *.pdf *.bbl *.blg

show: kgorman.pdf
	pdf kgorman.pdf

.PHONY: clean show
