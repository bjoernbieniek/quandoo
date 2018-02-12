#!/usr/bin/env python
"""
Aliens Sorter (TM) processes a list of alien species, sorts them by 
planet of origin and writes in a planet-specific format to the output file.
It uses ```aliens.csv``` as input and produces ```planets.csv``` by default.

"""
import copy
 
USAGE = """%prog [options]

No arguments are requiered. Aliens and their home planet will be read 
from default input file "aliens.csv". Planets with their inhabitants 
will be written to default output file "planets.csv"

       
"""

class planets:
    """Planets with their inhabitants"""
    def __init__(self, planet=None, alien=None, header=None):     
        self.planets = {planet : [alien]} if planet else {}
        self.header = header+"\n" if header else ''
        
    @classmethod
    def copy(self):
        """Copy dictionary"""
        return copy.deepcopy(self)
    def n(self):
        """Number of planets"""
        return len(self.planets)
    def m(self, p):
        """Number of planets for planet p"""
        return len(self.planets[p])
    def join(self, planet, alien):
        """Add inhabitant alien of planet to dictionary"""
        if planet in self.planets:
          self.planets[planet].append(alien)
        else:
          self.planets[planet] = [alien]
    def to_str(self):
      """Create string output"""
      lines=self.header
      for p in self.planets:
        lines = lines + self.planet_line(p,self.planets[p])
      return lines
    def planet_line(self,planet,aliens):
      """Create output line for planet with inhabitating aliens"""
      a = copy.deepcopy(aliens) # Don't change dictonary
      if planet==" zerg-1":
        line = " ".join(a).upper()+",zerg\n"
      elif planet==" ho":
        for i in range(self.m(planet)):
          a[i]=a[i]+"HO!"
        line = " | ".join(a)+",ho\n"
      elif planet==" mars":
        for i in range(self.m(planet)):
          a[i]=a[i]+"m"
        line = " ~~ ".join(a)+",mars\n"
      else:
	print('\n Warning: Unknown planet "'+planet+'". No output for this planet. Please define format.')
	line = ''
      return line
    
def main():
  import optparse

  # Parse command line
  parser = optparse.OptionParser(usage=USAGE)

  parser.add_option("-i", "--input", action="store", default='aliens.csv',
                    help="""\Path to input .csv file.""")
  parser.add_option("-o", "--output", action="store", default='planets.csv',
                    help="""\Path to output .csv file.""")
  parser.add_option("-t", "--top", action="store", default='species,planet',
                    help="""Header for output file.""")
  options, args = parser.parse_args()

  if len(args) != 0:
      parser.error("No arguments required")

  print('\n Aliens Sorter (TM)\n')
  # Init planets dictionary
  planets_dict = planets(header=options.top)
  
  # Read input file and sort into dictionary
  print ("Reading aliens input file "+options.input)
  f = open(options.input, 'r')
  aliens = f.readlines()
  header = True
  for line in aliens:
    if not header:
        alien = line.split(",")[0]
        planet = line.strip().split(",")[1]
        planets_dict.join(planet,alien)    
    else:
        header = False        
  f.close()

  # Create and write output
  print ("Writting planets output file "+options.output)
  output_lines = planets_dict.to_str()
  output = open(options.output,"w")
  output.writelines(output_lines)
  output.close()

  print ('\nDone.\n')

if __name__ == "__main__":
    main()