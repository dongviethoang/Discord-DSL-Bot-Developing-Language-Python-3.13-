import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from interpreter import discordbot
from discordpkg.pth import systemcommands
from discordpkg.pth import pth

# NOW YOU CAN ADD ANY COMMAND TO THIS LIST!
discordbot.commandarea = [
    '/test',      # Send test message
    '/say',       # Send custom message  
    '/sayhi',     # Send random greeting
    '/joke',      # Send random joke
    '/troll',     # Troll commands (rickroll, etc)
    '/status',    # Show bot status
    '/time',      # Show current time
    '/help'       # Show available commands
]

discordbot.bot_token = "[Base64 Encoded User/App ID].[Three-Character Timestamp].[Secure Cryptographic Signature]"

if discordbot.bot_token:
    print("Login success.")
    pth(discordbot.bot_token)
else:
    print("Login failed.")

# Note: The inputcmds call is now handled in pth.py, so this line is removed
