PY = python3
PELICAN = pelican
OUTPUT = output

.PHONY: html serve devserver publish clean

html:
	$(PELICAN) content -s pelicanconf.py -o $(OUTPUT)

serve: html
	cd $(OUTPUT) && $(PY) -m http.server 8000

devserver:
	$(PELICAN) content -s pelicanconf.py -o $(OUTPUT) -r -l

publish:
	$(PELICAN) content -s publishconf.py -o $(OUTPUT)

clean:
	rm -rf $(OUTPUT)
