
PREFIX?=~/.local/share/krita/

install:
	@echo Installing..
	cp src/* $(PREFIX)/pykrita/
