# NeverEndingQuest - Custom D&D Campaign Manager

An AI-powered Dungeon Master for running custom D&D 5th Edition campaigns with infinite adventure potential.

## Features

- **AI Dungeon Master**: GPT-powered storytelling that adapts to your actions
- **Character Creation**: Guided character creation with AI assistance
- **Save/Load System**: Automatic progress saving with backup protection
- **Campaign Management**: Create and manage adventure modules
- **Turn-Based Combat**: Tactical combat with D&D 5e rules
- **Natural Language**: No commands to memorize - just describe what you want to do

## Quick Start

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy the template
cp config_template.py config.py

# Edit config.py and add your OpenAI API key
# Get one at: https://platform.openai.com/api-keys
```

### 3. Run the Game

```bash
python main.py
```

## Project Structure

```
NeverEndingQuest_Custom/
├── main.py                 # Main game entry point
├── config_template.py      # Configuration template
├── requirements.txt        # Python dependencies
├── core/                   # Core game modules
│   ├── ai/                # AI integration
│   │   └── dm_wrapper.py  # AI Dungeon Master wrapper
│   └── managers/          # Game systems
│       ├── character_manager.py
│       └── campaign_manager.py
├── utils/                 # Utility functions
│   └── console_helper.py  # Console formatting
├── prompts/              # AI system prompts
│   └── system_prompt.txt
├── modules/              # Adventure modules
│   └── saves/           # Character saves
└── data/                # Game data
```

## How to Play

1. **Start the Game**: Run `python main.py`
2. **Create Character**: Follow the AI's guidance to create your character
3. **Play Naturally**: Just type what you want to do
   - "I search the room for traps"
   - "I attack the goblin with my sword"
   - "I try to persuade the merchant to give us a discount"
4. **Special Commands**:
   - `help` - Show available commands
   - `character` - View your character sheet
   - `save` - Save your game
   - `quit` - Exit the game

## Customization for Your D&D Campaign

### Adding Custom Modules

Create a new module for your campaign:

```python
from core.managers.campaign_manager import CampaignManager

manager = CampaignManager()
manager.create_basic_module(
    name="Your Adventure Name",
    description="Your adventure description",
    min_level=1,
    max_level=5
)
```

### Customizing the AI

Edit `prompts/system_prompt.txt` to customize how the AI DM behaves:
- Add your world lore
- Define house rules
- Set tone and style preferences

### Configuration Options

Edit `config.py` to customize:
- AI models and temperature
- Token compression settings
- Auto-save frequency
- Debug options

## Advanced Features

### Token Compression
The system automatically compresses conversation history to reduce API costs by 70-90%.

### Auto-Save
Games automatically save every 5 actions (configurable in `config.py`).

### Module System
Create self-contained adventure modules that can be reused and shared.

## Requirements

- Python 3.9 or higher
- OpenAI API key
- 4GB+ RAM recommended
- Internet connection for AI API

## Configuration

Key settings in `config.py`:

```python
# AI Models
DM_MAIN_MODEL = "gpt-4o-mini"  # Main storytelling

# Compression
COMPRESSION_ENABLED = True      # Enable compression

# Game Settings  
DEFAULT_STARTING_LEVEL = 1     # Starting level
AUTO_SAVE_FREQUENCY = 5        # Save every N actions

# Debug
DEBUG_MODE = False             # Enable debug output
```

## Troubleshooting

**"config.py not found"**
- Copy `config_template.py` to `config.py`
- Add your OpenAI API key

**"OpenAI package not installed"**
- Run `pip install -r requirements.txt`

**Slow AI responses**
- Normal (10-30 seconds for AI processing)
- Check your internet connection
- Verify API key is valid

## Creating Your Campaign

This system is designed to be customized for your specific D&D campaign:

1. **Edit the System Prompt**: Add your world lore to `prompts/system_prompt.txt`
2. **Create Modules**: Build adventure modules for your campaign locations
3. **Add NPCs**: Create characters unique to your world
4. **Custom Rules**: Configure house rules in the system prompt

## License

This is a custom implementation for your personal D&D campaign. The system uses:
- OpenAI's GPT models (requires API key)
- D&D 5e mechanics (SRD 5.1 compatible)

## Support

For issues or questions:
1. Check the README
2. Review `config_template.py` for settings
3. Enable DEBUG_MODE for detailed logging

## Credits

Based on the NeverEndingQuest project architecture
Customized for your D&D campaign and booklet project

---

**Ready to Begin Your Adventure?**

```bash
python main.py
```

Let the AI guide you through character creation and start your journey!
