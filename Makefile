TARGET=ms2
#TARGET=gorman_diss
BIBTEX=bibtex
COMMAND=xelatex -halt-on-error

$(TARGET).pdf: *.tex
	$(COMMAND) $(TARGET)

bib: *.tex gorman_diss.bib
	$(BIBTEX) $(TARGET)
	sed -e 's!?\\/}\.!?\\/}!' < $(TARGET).bbl > TEMP; mv TEMP $(TARGET).bbl
	$(COMMAND) -interaction=batchmode -no-pdf $(TARGET)
	$(COMMAND) -interaction=batchmode $(TARGET)
 
clean:
	latexmk -C
	$(RM) $(TARGET).bbl $(TARGET).xdv

show: $(TARGET).pdf
	open $(TARGET).pdf

.PHONY: clean show
