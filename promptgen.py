#Modified from the original script: https://github.com/javi22020/Prompt-Generator/blob/main/main.py

#Automatic copy to clipboard arguments commented out. If import pyperclip gives a 'no module found' error, run pip install pyperclip in a terminal/command window

import random as rn
#import pyperclip as pc

#Feel free to add/remove prompts as you please.

genadjcts = ['pretty', 'relaxing', 'calm', 'quiet', 'wonderful', 'nice', 'incredible', 'amazing', 'cozy', 'beautiful', 'ominous', 'gloomy', 'post-apocalyptic', 'warm', 'stunning', 'breathtaking', 'fascinating', 'peaceful', 'surreal', 'celestial', 'ancient', 'ethereal', 'dramatic', 'horrific', 'terrifying', 'emotional', 'dystopian', 'dark', 'magical', 'psychedelic', 'apocalyptic', 'fantasy', 'dark fantasy', 'alien', 'otherworldly', 'foggy', 'Victorian', 'trippy', 'desolate', 'eldritch', 'gothic', 'sci-fi', 'futuristic', 'snowy', 'fantastical', 'lush']

objadjcts = ['futuristic', 'sci-fi', 'glowing', 'ornate', 'scuffed', 'pristine', 'rustic', 'floral', 'crystalline', 'intricate', 'smooth', 'shiny', 'dusty', 'dirty', 'colorful', 'high-tech', 'modern', 'cute', 'magical', 'ancient', 'detailed']

charadjcts = ['armored', 'heavily armored', 'divine', 'cyborg', 'medieval', 'steampunk', 'stylish', 'angelic', 'female', 'male', 'confused', 'lost', 'old', 'young', 'attractive', 'intimidating', 'battered', 'cute', 'modern', 'dirty', 'scarred', 'determined', 'bearded', 'caped', 'shrouded', 'Latin American', 'Caucasian', 'African', 'Indian', 'Arab', 'Asian', 'happy', 'overjoyed', 'lone', 'joyful', 'sad', 'pensive', 'evil', 'bloody', 'robed', 'fashionable', 'tough', 'masked', 'tattooed',]

objects = ['cat', 'dog', 'knife', 'weapon', 'flower', 'plushie', 'frog', 'mirror', 'glass', 'shadow', 'sillhouette', 'cape', 'backpack', 'dress', 'suit', 'bodysuit', 'artifact', 'map', 'fighter', 'sword', 'carbine', 'smartphone', 'book', 'walking stick', 'drink', 'lantern', 'mask', 'gas mask', 'hat', 'tattoos',]

chara = ['man', 'woman', 'girl', 'boy', 'assassin', 'bounty hunter', 'knight', 'stormtrooper', 'robot', 'soldier', 'man', 'woman', 'samurai', 'vampire', 'catgirl', 'wolf girl', 'cowgirl', 'cowboy', 'jedi', 'warrior', 'sorcerer', 'human woman', 'human man', 'human girl', 'human boy', 'prince', 'princess', 'king', 'queen', 'god', 'goddess', 'demigod', 'survivor', 'villain', 'hero', 'traveler', 'spaceman', 'space marine', 'explorer', 'wayferer', 'chef', 'bird', 'phoenix', 'swordsman', 'scout', 'schoolgirl', 'schoolboy', 'motorcyclist', 'monster', 'hunter', 'demon', 'angel', 'pilot', 'crewman', 'fox girl', 'wizard', 'emperor', 'viking', 'ninja', 'alien', 'businessman', 'guard', 'operative', 'scientist', 'police officer', 'serial killer', 'cultist', 'romantic couple', 'friends', 'spirit', 'crewwoman', 'Little Red Riding Hood', 'chancellor',]

styles = ['oil painting', 'minimalistic', 'natural', 'colored', '35mm', 'award-winning photography', 'cinematic lighting', 'limited palette', 'pastel colors', 'cyberpunk', 'render', 'rendered in unreal engine', 'photo', 'glitch art', 'space art', 'high contrast', 'low contrast', 'epic composition', 'nighttime', 'vivid colors', 'soft lighting', 'wavy', 'extradimensional', 'depth of field', 'tonemapping', 'illustration', 'digital painting', 'line art', 'ink', 'color field painting', 'god rays', 'saturated', 'desaturated', 'tonal colors', 'full body', 'eyes focus', 'anime', 'aerial view', 'street level view', 'panoramic', 'hard edge', 'thick lines', 'color page', 'precise lineart', 'neon lighting', 'sun rays', 'nostalgic', 'brutalism', 'high resolution scan', 'winter', 'spring', 'autumn', 'summer', 'studio lighting', 'bokeh', 'motion lines', 'wallpaper', 'muted colors', 'colorgrading', 'vintage', 'aesthetic', 'cosmic horror', 'abstract art', 'simple background', 'synthwave', 'splatter paint style', 'portrait', 'vaporwave', 'concept art', 'cartoon', 'simplistic', 'dim', 'blurred background', 'ambient lighting', 'intense shadows', 'slow motion', 'reflections', 'detailed face', 'animecore', 'astrophotography', 'biomechanical', 'darkwave', 'deathpunk', 'glitchcore', 'glowwave', 'holographic', 'beautifully lit', 'technopunk']

genmetas = ['realistic', '8k', '4k', 'detailed', 'hyperdetailed', 'sharp focus', 'masterpiece', 'absurdres', 'highres', 'professional', 'photorealism', 'studio quality', 'HQ', 'UHD', 'HDR', 'highres',]

settings = ['street', 'beach', 'mountain', 'landscape', 'lake', 'planet', 'city', 'river', 'valley', 'house near a lake', 'house', 'house near the beach', 'skyscrapers', 'nature', 'town', 'forest', 'swamp', 'alien planet', 'urban landscape', 'natural landscape', 'alien landscape', 'street', 'city streets', 'town streets', 'liminal space', 'abandoned building', 'stronghold', 'thunderstorm', 'snowstorm', 'nature park', 'battleground', 'castle', 'detailed background', 'epic sky', 'kitchen', 'bedroom', 'living room', 'office', 'outer space', 'throne room', 'cockpit', 'car', 'sports car', 'fighter', 'starship', 'fireplace', 'truck', 'cargo bay', 'space station', 'dock', 'meadow', 'stream', 'cave', 'stadium', 'alleyway', 'market', 'theater', 'workshop', 'field', 'farm', 'barn', 'path', 'jungle', 'pond', 'highway', 'underground cave', 'skyline', 'horizon', 'desert', 'mesa', 'misty island', 'Arctic landscape', 'cityscape', 'cottage', 'cabin in the woods', 'tunnel', 'hilly landscape', 'bathroom', 'village']

relatedesc = ['near a', 'in a', 'next to a', 'in front of a', 'inside of a', 'outside of a',]


#Set number of random general adjective, style, and quality phrases to add after the main description of the prompt.
numadjectives = 3
numstyles = 3
numquality = 4

cond = ''
while cond == '':
    listadj = rn.sample(genadjcts, numadjectives)
    adj = ', '.join(listadj)
    #Selects a character and accompanying character adjective
    character = rn.choice(charadjcts) + ' ' + rn.choice(chara) 
    #Selects an adjective and an accompanying object
    obj = rn.choice(objadjcts) + ' ' + rn.choice(objects)
    #Creates a setting for the character and object to be in
    setting = rn.choice(relatedesc) + ' ' + rn.choice(genadjcts) + ' ' + rn.choice(settings)
    #Constructs main part of prompt
    prompt = character + ' ' + 'with a ' + obj + ' ' + setting + ', ' + adj
    liststyles = rn.sample(styles, numstyles) + rn.sample(genmetas, numquality)
    sty = ', '.join(liststyles)
    prompt = prompt + ', ' + sty
    print()
    print(prompt)
    print()
    cond = input("Press 'enter' to generate another prompt.")
#pc.copy(prompt)
#print('\nThe prompt has been copied to your clipboard')
