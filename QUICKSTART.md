# NeverEndingQuest - Quick Start Guide

## What You Have

I've recreated the NeverEndingQuest system based on the repository you forked. This is a streamlined version optimized for your D&D campaign project.

## Files Included

```
NeverEndingQuest_Custom/
├── main.py                 - Main game (run this!)
├── config_template.py      - Settings template
├── requirements.txt        - Python packages needed
├── README.md              - Full documentation
├── setup.sh               - Linux/Mac setup script
├── setup.bat              - Windows setup script
├── core/                  - Core game engine
├── utils/                 - Helper utilities
├── prompts/               - AI system prompts
├── modules/               - Adventure modules (empty, ready for your content)
└── data/                  - Game data (empty, ready for your content)
```

## Installation (3 Steps)

### Step 1: Install Python Packages

**Windows:**
```
setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**Or manually:**
```bash
pip install -r requirements.txt
```

### Step 2: Add Your API Key

1. Copy `config_template.py` to `config.py`
2. Open `config.py` in a text editor
3. Replace `"your-api-key-here"` with your actual OpenAI API key
4. Save the file

Get an API key at: https://platform.openai.com/api-keys

### Step 3: Run the Game

```bash
python main.py
```

## First Time Playing

When you run the game:

1. You'll be prompted to create a character
2. Enter your character's name
3. The AI will guide you through choosing:
   - Race (Human, Elf, Dwarf, etc.)
   - Class (Fighter, Wizard, Rogue, etc.)
   - Background (optional)
4. The AI creates a backstory for you
5. Your adventure begins!

## How to Play

Just type what you want to do naturally:

```
> I look around the room
> I attack the goblin with my sword
> I try to persuade the merchant
> I search for traps
> I cast fireball at the enemies
```

## Special Commands

- `help` - Show help menu
- `character` - View your character sheet
- `save` - Save your game
- `quit` or `exit` - Quit game (prompts to save)

## Customizing for Your Campaign

### Add Your World Lore

Edit `prompts/system_prompt.txt` to add:
- Your world's history
- Custom locations
- Special rules
- Tone and style preferences

### Create Adventure Modules

```python
from core.managers.campaign_manager import CampaignManager

manager = CampaignManager()
module = manager.create_basic_module(
    name="The Haunted Keep",
    description="A dark fortress holds ancient secrets",
    min_level=3,
    max_level=5
)
```

### Configure Settings

Edit `config.py` to change:
- AI model (gpt-4o-mini is cost-effective)
- Compression settings (reduces API costs)
- Auto-save frequency
- Starting level
- Debug options

## Integration with Your D&D Booklet

This system can help with your booklet project:

1. **Generate Content**: Use the AI to create NPCs, locations, quests
2. **Test Adventures**: Playtest your campaign modules
3. **Create Backstories**: Generate character backgrounds
4. **World Building**: Develop locations and lore
5. **Combat Balancing**: Test encounter difficulty

## Next Steps

### For Your Campaign

1. **Edit System Prompt**: Add your world lore to `prompts/system_prompt.txt`
2. **Create Modules**: Build adventures for your campaign
3. **Add NPCs**: Create unique characters
4. **Test & Iterate**: Playtest your content

### Advanced Features

- **Token Compression**: Automatically reduces API costs by 70-90%
- **Auto-Save**: Saves progress every 5 actions
- **Module System**: Organize adventures into reusable modules
- **Character Progression**: Full D&D 5e leveling system

## Troubleshooting

**"config.py not found"**
- Copy `config_template.py` to `config.py`

**"OpenAI package not installed"**
- Run `pip install -r requirements.txt`

**"Invalid API key"**
- Check your API key in `config.py`
- Make sure it starts with "sk-"

**Slow responses**
- Normal (AI takes 10-30 seconds)
- Check internet connection

## Cost Information

Using `gpt-4o-mini` (default):
- Very affordable
- ~$0.15 per million input tokens
- ~$0.60 per million output tokens
- Typical session: $0.10 - $0.50

The token compression system reduces costs by 70-90%.

## Support

- Read the full README.md
- Check config_template.py for all settings
- Enable DEBUG_MODE in config.py for troubleshooting

## Have Fun!

This is YOUR system now. Customize it, break it, rebuild it, and make it perfect for your D&D campaign!

The AI is here to help bring your creative vision to life. Enjoy your adventure! 🎲⚔️🐉
