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
	$(RM) -f *.aux *.toc *.log *.lot *.bbl *.blg *.fls *.lof $(TARGET)

show: $(TARGET)
	open $(TARGET)

.PHONY: clean rmpdf show
