TARGET=gorman_diss
BIBTEX=bibtex
COMMAND=xelatex -halt-on-error

$(TARGET).pdf: *.tex *.sty *.cls
	$(COMMAND) $(TARGET)

bib: *.tex gorman_diss.bib
	$(BIBTEX) $(TARGET)
	sed -e 's!?\\/}\.!?\\/}!' < $(TARGET).bbl > TEMP; mv TEMP $(TARGET).bbl
	$(COMMAND) -interaction=batchmode -no-pdf $(TARGET)
	$(COMMAND) -interaction=batchmode $(TARGET)
 
clean:
	latexmk -c
	$(RM) *.bbl *.xdv

show: $(TARGET).pdf
	open $(TARGET).pdf

.PHONY: show clean $(TARGET).pdf
