#!/usr/bin/env python3
"""
NeverEndingQuest - AI-Powered D&D Campaign Manager
Main entry point for terminal interface
"""

import os
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    import config
except ImportError:
    print("ERROR: config.py not found!")
    print("Please copy config_template.py to config.py and add your API key")
    sys.exit(1)

from core.managers.campaign_manager import CampaignManager
from core.managers.character_manager import CharacterManager
from core.ai.dm_wrapper import DMWrapper
from utils.console_helper import ConsoleHelper


class NeverEndingQuest:
    """Main game controller"""
    
    def __init__(self):
        self.console = ConsoleHelper()
        self.campaign_manager = CampaignManager()
        self.character_manager = CharacterManager()
        self.dm = DMWrapper()
        self.running = False
        self.current_character = None
        
    def start(self):
        """Start the game"""
        self.console.clear()
        self.console.print_header("NeverEndingQuest - AI-Powered D&D Campaign")
        self.console.print_separator()
        
        # Check for existing saves
        if self.has_saved_games():
            self.show_main_menu()
        else:
            self.console.print_info("Welcome, adventurer! Let's create your character.")
            self.create_character()
            
    def has_saved_games(self):
        """Check if there are any saved characters"""
        saves_path = Path("modules/saves")
        if not saves_path.exists():
            return False
        return len(list(saves_path.glob("*.json"))) > 0
        
    def show_main_menu(self):
        """Display main menu"""
        while True:
            self.console.clear()
            self.console.print_header("Main Menu")
            print("\n1. New Character")
            print("2. Load Character")
            print("3. Settings")
            print("4. Exit")
            
            choice = input("\nYour choice: ").strip()
            
            if choice == "1":
                self.create_character()
                break
            elif choice == "2":
                if self.load_character():
                    break
            elif choice == "3":
                self.show_settings()
            elif choice == "4":
                sys.exit(0)
            else:
                self.console.print_error("Invalid choice. Please try again.")
                input("Press Enter to continue...")
                
    def create_character(self):
        """Create a new character with AI guidance"""
        self.console.clear()
        self.console.print_header("Character Creation")
        
        # Get character name
        name = input("\nWhat is your character's name? ").strip()
        if not name:
            name = "Adventurer"
            
        # Use AI to guide character creation
        self.console.print_info("\nThe AI Dungeon Master will guide you through character creation...")
        
        character_data = self.character_manager.create_character_with_ai(name, self.dm)
        self.current_character = character_data
        
        self.console.print_success(f"\nWelcome, {name}! Your adventure begins...")
        input("Press Enter to continue...")
        
        # Start the game loop
        self.game_loop()
        
    def load_character(self):
        """Load an existing character"""
        saves_path = Path("modules/saves")
        save_files = list(saves_path.glob("*.json"))
        
        if not save_files:
            self.console.print_error("No saved games found.")
            input("Press Enter to continue...")
            return False
            
        self.console.clear()
        self.console.print_header("Load Character")
        
        for i, save_file in enumerate(save_files, 1):
            # Load character data to show name and level
            with open(save_file, 'r') as f:
                data = json.load(f)
                char_name = data.get('name', 'Unknown')
                char_level = data.get('level', 1)
                char_class = data.get('class', 'Unknown')
                print(f"{i}. {char_name} - Level {char_level} {char_class}")
                
        print(f"{len(save_files) + 1}. Cancel")
        
        choice = input("\nSelect character: ").strip()
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(save_files):
                with open(save_files[choice_num - 1], 'r') as f:
                    self.current_character = json.load(f)
                self.console.print_success(f"\nLoaded {self.current_character['name']}!")
                input("Press Enter to continue...")
                self.game_loop()
                return True
        except (ValueError, IndexError):
            pass
            
        return False
        
    def game_loop(self):
        """Main game loop"""
        self.running = True
        
        self.console.clear()
        self.console.print_header(f"Playing as {self.current_character['name']}")
        
        # Initial scene setting
        response = self.dm.start_adventure(self.current_character)
        self.console.print_dm(response)
        
        while self.running:
            print("\n" + "="*80)
            user_input = input("\n> ").strip()
            
            if not user_input:
                continue
                
            # Check for special commands
            if user_input.lower() in ['quit', 'exit']:
                if self.confirm_quit():
                    break
                continue
            elif user_input.lower() == 'help':
                self.show_help()
                continue
            elif user_input.lower() == 'character':
                self.show_character_sheet()
                continue
            elif user_input.lower() == 'save':
                self.save_game()
                continue
                
            # Send to AI DM
            try:
                response = self.dm.process_action(user_input, self.current_character)
                self.console.print_dm(response)
                
                # Auto-save every few actions
                if hasattr(config, 'ENABLE_AUTO_SAVE') and config.ENABLE_AUTO_SAVE:
                    self.auto_save()
                    
            except Exception as e:
                self.console.print_error(f"Error processing action: {e}")
                if config.DEBUG_MODE:
                    import traceback
                    traceback.print_exc()
                    
    def show_character_sheet(self):
        """Display character information"""
        self.console.clear()
        self.console.print_header("Character Sheet")
        
        char = self.current_character
        print(f"\nName: {char.get('name', 'Unknown')}")
        print(f"Class: {char.get('class', 'Unknown')}")
        print(f"Level: {char.get('level', 1)}")
        print(f"Race: {char.get('race', 'Unknown')}")
        print(f"HP: {char.get('current_hp', 0)}/{char.get('max_hp', 0)}")
        print(f"XP: {char.get('xp', 0)}")
        
        input("\nPress Enter to continue...")
        
    def show_help(self):
        """Show help information"""
        self.console.clear()
        self.console.print_header("Help")
        
        print("\nAvailable Commands:")
        print("  help        - Show this help")
        print("  character   - View character sheet")
        print("  save        - Save game")
        print("  quit/exit   - Quit game")
        print("\nJust type what you want to do naturally!")
        print("Examples:")
        print("  'I search the room for traps'")
        print("  'I attack the goblin with my sword'")
        print("  'I try to persuade the merchant'")
        
        input("\nPress Enter to continue...")
        
    def save_game(self):
        """Save the current game"""
        saves_path = Path("modules/saves")
        saves_path.mkdir(parents=True, exist_ok=True)
        
        char_name = self.current_character.get('name', 'character').replace(' ', '_')
        save_file = saves_path / f"{char_name}.json"
        
        with open(save_file, 'w') as f:
            json.dump(self.current_character, f, indent=2)
            
        self.console.print_success(f"Game saved to {save_file}")
        
    def auto_save(self):
        """Automatically save the game"""
        if not hasattr(self, '_action_count'):
            self._action_count = 0
            
        self._action_count += 1
        
        if self._action_count >= config.AUTO_SAVE_FREQUENCY:
            self.save_game()
            self._action_count = 0
            
    def confirm_quit(self):
        """Confirm before quitting"""
        response = input("\nSave before quitting? (y/n): ").strip().lower()
        if response == 'y':
            self.save_game()
        return True
        
    def show_settings(self):
        """Show settings menu"""
        self.console.clear()
        self.console.print_header("Settings")
        print("\nSettings coming soon...")
        input("Press Enter to continue...")


def main():
    """Entry point"""
    try:
        game = NeverEndingQuest()
        game.start()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\nFatal error: {e}")
        if hasattr(config, 'DEBUG_MODE') and config.DEBUG_MODE:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
