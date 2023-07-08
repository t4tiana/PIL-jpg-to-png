import sys
import os
from PIL import Image

'''After py and then python file name, this takes the first user input as the folder to pull the pics.
So it has to be Pokedex because thats the directory that contains the pokemon jpgs.
so into the terminal I type py JPGtoPNGconvert.py Pokedex {new folder name}. Pranav chose Pokemex.'''
folder = sys.argv[1]
#this makes sure the loop is looking in the Pokedex directory
directory = f'C:\\Users\\tiana\\.vscode\\Practice\\{folder}'
new_folder = sys.argv[2]
#create the new folder to save the pngs. P called it Pokemex.
os.makedirs(new_folder, exist_ok=True)

#iterate over the directory to find the jpgs
for file in os.listdir(directory):
    #to find the jpgs, this is the splitext trick from Corey Schafer's pillow video
    fn, fext = os.path.splitext(file)
    if fext == '.jpg':
        #a new variable is created because the 'file' in 'for file' is just a string
        #this actually opens the jpg file so it can be manipulated (saved)
        pokepic = Image.open(file)
        #go to the Pokemex folder so that it saves there instead of the Pokedex folder
        os.chdir(new_folder)
        #save it using corey's trick to get the filename to be the same as original
        pokepic.save("{}.png".format(fn), 'png')
        #change back to Pokedex directory before the loop restarts so that the next
        #jpg can be processed. Otherwise, exception will be thrown because we're still in Pokemex
        #and there arent any jpgs in there
        os.chdir(directory)