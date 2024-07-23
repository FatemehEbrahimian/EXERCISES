import sys
import pyfiglet
def main():
 fonts=pyfiglet.FigletFont.getFonts()
 if len(sys.argv)==1:
    text=input(":")
    figlet=pyfiglet.Figlet()
 elif len(sys.argv)==3:
    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        if sys.argv[2] in fonts:
           text=input("Input:")
        figlet=pyfiglet.Figlet(sys.argv[2])
 else:
   sys.exit()
 main()

