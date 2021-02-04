csv2table := python3 ~/Projects/utilities/csv2table.markdown/csv2table.markdown.py
update: commands.csv
	@cat CONTENT.md > README.md && $(csv2table) commands.csv >> README.md
