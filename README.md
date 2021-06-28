# disko.py

Disko Bot, is a Discord Music Bot that not only plays music directly from Youtube but also downloads the audio.mp3 file in the source folder.
Create a new application at [Discord Developer Portal](https://discord.com/developers/applications), and then select 'Add Bot'. 

Disko Bot also requires "manage messages" permissions on your server to use features like recognizing curse words and deleting them automatically.

### Installation

```
Token = "YOUR_TOKEN"
YOUR_PREFIX = "~"
client = commands.Bot(command_prefix=YOUR_PREFIX)
```

- `YOUR_TOKEN`, the token of the bot available on the [Discord Developers](https://discord.com/developers/applications) section once you created the bot. Simply copy and paste it here.
- `YOUR_PREFIX = "~"`, the prefix that will be set to use the bot and access commands. (e.g "!", "$", ".", "~")

Install all the dependencies using the interpreter. Run the Disko.py to turn on the bot!

### Commands

- `YOUR_PREFIX`play [URL], plays music in the voice channel.
- `YOUR_PREFIX`pause, pauses the music. 
- `YOUR_PREFIX`leave, leaves the voice channel.
- `YOUR_PREFIX`stop, stops playing the music.
- `YOUR_PREFIX`join, joins the voice channel.
- `YOUR_PREFIX`server, displays server information.
- `YOUR_PREFIX`meme, shares random meme from r/dankmemes on Reddit.

Hope you like it! ❤️
