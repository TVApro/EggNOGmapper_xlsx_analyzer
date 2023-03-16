# EggNOGmapper_xlsx_analyzer
A small code part for extracting data from an Excel output file of EggNog-mapper v.2.0

Steps required for analysis:

1.1. Obtain .faa files from the annotated genomes (you may use https://github.com/TVApro/UltraChtec for this)

1.2. Load each .faa file into eggNog_mapper (http://eggnog-mapper.embl.de/), get Excel files as the output

2. Remove the top two "technical" lines from each table

3. Put all tables in one folder

4. Run the script using any IDE for Python

4.1 By default, it counts the number of proteins in COG groups and builds a summary table for all genomes

4.2. You can optionally sort the data in any presented column by choosing column name

5. The result can be copied from the IDE or saved as a .csv table
