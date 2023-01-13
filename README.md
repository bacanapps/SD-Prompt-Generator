# SD-Prompt-Generator
An edit of javi22020's Prompt Generator script that tries to create random prompts with a 'character with (object) [random relation to setting] [setting]' structure that works well for providing inspiration.

## Usage

To use, have Python installed, and download promptgen.py, or copy the contents and paste them into an empty document and save as promptgen.py, or whatever name you prefer. Put the .py somewhere you can access easily. Or, put it in your home folder (on Linux) or somewhere with the PATH edited on Windows, if you want to easily call the script without typing or pasting the file's path.

In a terminal/CLI, type

    python promptgen.py
    or
    python path/to/promptgen.py

Press 'enter' to keep generating prompts quickly. As prompts are randomized, they will be naturally hit-or-miss, so that makes it easy to roll the dice again.

To add or remove phrases, or edit how many are tacked on the main prompt, edit the .py. The structure is pretty straightforward, so if you want to, you can even further break down the prompt categories and add them into the code as you like for more complex or specialized random prompting.

Naturally, certain phrases will be better understood by different models. For instance, "catgirl" and "splash paint art" are represented much better in anime-based models than models that focus more on realistic art.

## Prompt explanation and examples

In this fork, prompt phrases are separated into general adjectives, character adjectives, objects, characters, styles, quality prompts, and settings. The usefulness of "quality prompts" (e.g. realistic, masterpiece, professional) despite their widespread application is debatable, but they are included nonetheless as they sometimes improve the detail of outfits and sense of depth.

The general adjectives add randomness to the output, but also can influence the overall visual impression of an image. I recommend using the [bad-artist](https://huggingface.co/nick-x-hacker/bad-artist) embeddings in your negative prompt, as these seem to help prevent over-representation of adjectives in the AI's output. For instance, without those 'negative embeddings', "terrifying" will make characters, well, terrifying, even if it's meant to be describing the setting.

The expanded prompt list was built off of personal experience after thousands of images generated with Stable Diffusion v1.5-based models. Artist names and existing IP were intentionally avoided for style and quality prompts to focus on getting decent-quality output off creativity alone.

![003659 099091dd 3062602010](https://user-images.githubusercontent.com/122599135/212419237-8c5f4942-388b-43d0-8390-c5dfae3aff34.png)

`heavily armored operative with a intricate smartphone in a ethereal forest, fascinating, magical, emotional, low contrast, cosmic horror, eyes focus, HDR, 4k, 8k, hyperdetailed [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: TheAlly's Mix II`

![003689 18c8966b 2537436940](https://user-images.githubusercontent.com/122599135/212424493-770e5ccc-35f7-4c0f-9c8b-1d88b3cc8ba0.png)

`heavily armored alien with a dystopian bodysuit near a shiny cockpit, Victorian, beautiful, scuffed, thick lines, wallpaper, anime, studio quality, UHD, detailed, highres [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Kenshi`

![003691 bd4d6aa3 743370597](https://user-images.githubusercontent.com/122599135/212424921-d6140040-39d6-41e6-b14a-ca8d8ee3a13f.png)

`Arab prince with a crystalline glass inside of a gloomy mountain, ancient, nice, cozy, after hours, eyes focus, detailed face, absurdres, studio quality, highres, hyperdetailed [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Kenshi`

![003703 1ed7680d 2859117530](https://user-images.githubusercontent.com/122599135/212426057-851353dc-5874-4c7a-8251-fabd28771577.png)

`Asian pilot with a ancient glass near a magical snowstorm, ethereal, trippy, emotional, neon lighting, epic composition, wavy, detailed, masterpiece, realistic, photorealism [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Elldreth's Stolen Dreams`
