file_name = kicchi_IPSJ201901

.PHONY: all
all:
	#platex $(file_name).tex
	#dvipdfmx $(file_name).dvi
	#pdflatex $(file_name).tex #横山さん使ってる方。slideの方で必要かも？
	platex $(file_name).tex #ずっと使ってたやつ
	#pbibtex $(file_name)
	dvipdfmx $(file_name)
	#ptex2pdf -l $(file_name).tex #ずっと使ってたやつ
	#ptex2pdf -l $(file_name).tex #ずっと使ってたやつ
	open $(file_name).pdf

pdf: $(file_name).dvi
	dvipdfmx $(file_name).dvi

.PHONY: clean
clean: 
	rm -f $(file_name).[^t]* $(file_name).toc

.PHONY: cln
cln: clean

