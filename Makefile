csv2markdown := python3 ./csv2markdown.py commands.csv ccl
update: commands.csv CONTENT.md
	@cat CONTENT.md > README.md && $(csv2markdown) >> README.md
