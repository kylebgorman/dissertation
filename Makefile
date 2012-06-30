SOURCE=gorman_diss
TARGET=gorman_diss.pdf
BIBTEX=bibtex
COMMAND=xelatex -halt-on-error

all:
	$(COMMAND) $(SOURCE)

bib: $(TARGET)
	$(BIBTEX) $(SOURCE)
	sed -e 's!?\\/}\.!?\\/}!' < $(SOURCE).bbl > TEMP; mv TEMP $(SOURCE).bbl
	$(COMMAND) -interaction=batchmode -no-pdf $(SOURCE)
	$(COMMAND) -interaction=batchmode $(SOURCE)

clean:
	latexmk -C
	$(RM) $(SOURCE).bbl $(SOURCE).xdv

show: $(TARGET)
	open $(TARGET)

.PHONY: clean show
