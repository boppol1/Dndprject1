"""
NeverEndingQuest Configuration Template
Copy this file to config.py and add your API keys
"""

# ============================================================================
# API CONFIGURATION
# ============================================================================

# OpenAI API Key (get from https://platform.openai.com/api-keys)
OPENAI_API_KEY = "your-api-key-here"

# Alternative: Use Claude API by Anthropic
# ANTHROPIC_API_KEY = "your-anthropic-api-key-here"
# USE_ANTHROPIC = False  # Set to True to use Claude instead of GPT

# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

# Primary AI Models
DM_MAIN_MODEL = "gpt-4o-mini"  # Main storytelling and game narration
DM_SUMMARIZATION_MODEL = "gpt-4o-mini"  # Conversation compression
DM_VALIDATION_MODEL = "gpt-4o-mini"  # Rule validation and mechanics

# Specialized Models
DM_COMBAT_NARRATOR_MODEL = "gpt-4o-mini"  # Combat descriptions
MODULE_CREATION_MODEL = "gpt-4o-mini"  # Module/content generation
NPC_GENERATION_MODEL = "gpt-4o-mini"  # NPC creation

# ============================================================================
# TOKEN COMPRESSION SETTINGS
# ============================================================================

# Enable/disable token compression system (70-90% cost reduction)
COMPRESSION_ENABLED = True
COMPRESSION_CACHE_SIZE = 1000  # Number of compressed messages to cache
COMPRESSION_PARALLEL_WORKERS = 5  # Parallel compression threads
USE_COMPRESSED_PROMPTS = True  # Use compressed system prompts

# Model Routing Settings
ENABLE_ACTION_PREDICTION = True  # Enable intelligent model routing
MINI_MODEL_THRESHOLD = 0.3  # Confidence threshold for mini model

# ============================================================================
# WEB INTERFACE SETTINGS
# ============================================================================

WEB_PORT = 8358
WEB_HOST = "localhost"  # Change to "0.0.0.0" for network access
DEBUG_MODE = False  # Set to True for development

# ============================================================================
# GAME SETTINGS
# ============================================================================

# Starting level for new characters
DEFAULT_STARTING_LEVEL = 1

# Enable/disable features
ENABLE_PARTY_RECRUITMENT = True
ENABLE_STORAGE_SYSTEM = True
ENABLE_PLAYER_HOUSING = True
ENABLE_AUTO_SAVE = True

# Save frequency (in game actions)
AUTO_SAVE_FREQUENCY = 5

# ============================================================================
# DEBUG SETTINGS
# ============================================================================

# Logging
ENABLE_DEBUG_LOGGING = False
LOG_API_CALLS = False
LOG_FILE_PATH = "debug/logs/game.log"

# Combat debugging
AMMO_DEBUG = False
COMBAT_DEBUG = False

# ============================================================================
# PATHS
# ============================================================================

MODULES_PATH = "modules"
PROMPTS_PATH = "prompts"
DATA_PATH = "data"
GRAPHIC_PACKS_PATH = "graphic_packs"
SCHEMAS_PATH = "schemas"

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================

# Temperature settings for AI generation
STORYTELLING_TEMPERATURE = 0.8
VALIDATION_TEMPERATURE = 0.2
COMBAT_TEMPERATURE = 0.7

# Token limits
MAX_CONTEXT_TOKENS = 128000
MAX_RESPONSE_TOKENS = 4000

# Retry settings
MAX_API_RETRIES = 3
API_RETRY_DELAY = 2  # seconds
