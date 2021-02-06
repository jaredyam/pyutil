csv2markdown := python3 ./csv2markdown.py
update: commands.csv CONTENT.md
	@cat CONTENT.md > README.md && $(csv2markdown) commands.csv >> README.md
