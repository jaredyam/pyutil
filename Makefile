README.md: commands.csv CONTENT.md
	@cat CONTENT.md > README.md && csv2markdown commands.csv ccl >> README.md
