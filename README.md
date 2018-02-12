Ugly Aliens Sorter
====================

Aliens Sorter (TM) processes a list of alien species, sorts them by 
planet of origin and writes in a planet-specific format to the output file.
It uses ```aliens.csv``` as input and produces ```planets.csv``` by default.


Usage: python aliens_sorter.py [options]

No arguments are requiered. Aliens and their home planet will be read 
from default input file "aliens.csv". Planets with their inhabitants 
will be written to default output file "planets.csv"

       
Options:\n
  -h, --help            show this help message and exit\n
  -i INPUT, --input=INPUT\n
                        \Path to input .csv file.\n
  -o OUTPUT, --output=OUTPUT\n
                        \Path to output .csv file.\n
  -t TOP, --top=TOP     Header for output file.\n