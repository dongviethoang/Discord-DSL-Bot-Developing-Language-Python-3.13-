"""
pth.py — Linker Layer Between Domain-Specific Language (DSL) Interpreter and Discord Application Programming Interface (API)

Description:
------------
This module acts as the "linker" between the custom Discord Domain-Specific Language (DSL) and the actual Discord Application Programming Interface (API).
It handles authentication using the bot token, establishes the connection via `discord.py`,
and initializes the interpreter thread that listens for console input.

Essentially, this is where the Domain-Specific Language (DSL) becomes *real* — commands written by the user are
interpreted and then sent through this file to reach the live Discord servers.

It uses the `discord` Python module (based on Discord’s Representational State Transfer (REST) and WebSocket Application Programming Interfaces (APIs)),
and acts as a lightweight runtime bridge. While Discord itself is originally built with
technologies like Node.js and HyperText Transfer Protocol (HTTP)/WebSockets, this linker abstracts that complexity
away for Domain-Specific Language (DSL)-level users.

Key Responsibilities:
---------------------
- Load environment configuration from a manually specified file
- Log in the bot using the provided token
- Set up the Discord event loop
- Spawn a thread to handle console input via the interpreter
- Serve as the only layer that directly interacts with Discord’s Application Programming Interface (API)

Note:
-----
As this project grows, this file may become longer and more complex. Handle with care.

Author:
-------
[Beta]
[Language: Python 3.13 (planned upgrade: 3.14 → "Pi-thon")]
[Version: vBeta Testing — 2025-08-07]
"""

import discord
from discord.ext import commands
import threading
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from interpreter import discordbot

# System-level bot control commands
systemcommands = ['!disablebot', '!pausebot']

def pth(_=None):
    """
    Linker function that connects the DSL bot interpreter to Discord's API.
    Loads the token from a manually-specified environment config file (e.g., 'config.env').
    """

    # Load your manually named environment file
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config.env'))

    # Get the token from the env file
    token = os.getenv("DISCORD_TOKEN")

    if not token:
        print("ERROR: DISCORD_TOKEN not found in config.env.")
        return

    # Assign token to the interpreter (still needed there)
    discordbot.bot_token = token

    # Setup Discord intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Create the bot instance
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        print('Bot is ready and connected to Discord!')

        # Start the command-line interpreter in a separate thread
        command_thread = threading.Thread(target=discordbot.inputcmds, args=(bot, systemcommands,))
        command_thread.start()

    # Run the bot using the token from config.env
    bot.run(token)
