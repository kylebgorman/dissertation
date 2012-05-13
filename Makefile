SOURCE=gorman_diss
TARGET=gorman_diss.pdf
BIBTEX=bibtex
COMMAND=xelatex -halt-on-error

pdf: 
	$(COMMAND) $(SOURCE)

bib: $(TARGET)
	$(BIBTEX) $(SOURCE)
	$(COMMAND) $(SOURCE)
	$(COMMAND) $(SOURCE)

clean:
	latexmk -c

show: $(TARGET)
	open $(TARGET)

.PHONY: clean rmpdf show
