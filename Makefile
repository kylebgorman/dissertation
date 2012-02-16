TARGET=gorman_diss.pdf
COMMAND=xelatex

pdf: 
	$(COMMAND) gorman_diss

bib: $(TARGET)
	bibtex gorman_diss
	$(COMMAND) gorman_diss
	$(COMMAND) gorman_diss

clean:
	rm -f *.aux *.toc *.log *.lot *.bbl *.blg

show: $(TARGET)
	pdf $(TARGET) & open $(TARGET) &

.PHONY: clean show
