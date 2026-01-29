

# Detect OS and set RM command accordingly

RM = rm -f
CAT = cat
SEP = /

ifeq ($(OS),Windows_NT)
	RM = del /Q
	CAT = type
	SEP = \\
endif

files_to_clean := .$(SEP)samples$(SEP)gantt.html .$(SEP)samples$(SEP)mermaid.html .$(SEP)samples$(SEP)graphviz.html .$(SEP)src$(SEP)report.html \
	.$(SEP)samples$(SEP)index.html .$(SEP)reports$(SEP)report.html

.PHONY: default
default: 
	@echo No default target.  See Makefile for more details!

.PHONE: clean
clean:
	@echo removing $(files_to_clean)
	@-$(RM) $(files_to_clean)
	@echo Done.
	