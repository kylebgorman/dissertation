SOURCE=gorman_diss
TARGET=gorman_diss.pdf
COMMAND=xelatex -halt-on-error

pdf: 
	$(COMMAND) $(SOURCE)

bib: $(TARGET)
	bibtex $(SOURCE)
	$(COMMAND) $(SOURCE)
	$(COMMAND) $(SOURCE)

clean:
	rm -f *.aux *.toc *.log *.lot *.bbl *.blg $(TARGET)

rmpdf:
	rm $(TARGET)

show: $(TARGET)
	pdf $(TARGET) & open $(TARGET) &

.PHONY: clean rmpdf show
