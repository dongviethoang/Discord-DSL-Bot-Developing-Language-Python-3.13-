# Discord Bot DSL Runtime

A custom domain-specific language (DSL) designed for creating and controlling Discord bots using a structured scripting system. This runtime connects your DSL-written bot logic to the official Discord API via a linker and interpreter system.

Note: This project is under active development. Structure and APIs may change.

---

## Project Structure

```
discord_dsl_runtime/
├── discordpkg/
│   ├── __init__.py
│   └── pth.py           ← Linker to Discord API
├── interpreter/
│   └── discordbot.py    ← Bot Interpreter (input handling, command routing)
├── bots/
│   └── ExampleBot.py    ← DSL bot source code
├── config.env           ← Secrets (token, channel ID, etc.)
└── README.md            ← This file
```

---

## Overview

| Component      | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `pth.py`       | Linker module: connects DSL to Discord via `discord.py`, loads `.env`.     |
| `discordbot.py`| Interpreter: handles input commands, message sending, pause/resume states. |
| `ExampleBot.py`| Sample bot using the DSL structure.                                         |
| `config.env`   | Stores sensitive bot credentials (not committed to Git).                   |

---

## Environment Configuration

You must create a `.env` file before running the bot. You may rename it (e.g., `config.env`) and specify its path in `pth.py`.

Example `config.env`:
```
DISCORD_TOKEN=your_bot_token_here
CHANNEL_ID=1402842937510989887
```

Make sure your `.env` file uses UTF-8 (without BOM) encoding if you're on Windows.

---

## Getting Started

### Requirements

- Python 3.10 or higher
- `discord.py`
- `python-dotenv`

### Install Dependencies

```
pip install discord.py python-dotenv
```

### Running the Bot

```
python bots/ExampleBot.py
```

Or directly use the linker:

```
python discordpkg/pth.py
```

---

## Features

- DSL-style scripting layer for bots
- Linker abstraction layer for Discord API
- Interpreter with command-line input
- Async-safe communication with Discord
- Pause and resume bot command flow
- Secure environment variable support
- Designed to mirror Discord’s module structure (`discordpkg.pth`)

---

## Design Philosophy

"It should feel like coding a Discord bot, without needing to touch Discord.py."

Inspired by the modular and extensible nature of Discord bots, this runtime keeps things familiar while offering flexibility to write bot logic in a custom DSL format.

---

## Warnings

- `pth.py` may become large and complex as it evolves
- Asynchronous Python knowledge is recommended for development
- `config.env` must be correctly formatted and present at runtime

---

## Roadmap

- [ ] DSL syntax parser
- [ ] Auto command registration
- [ ] GitHub repository setup
- [ ] Installer or shell launcher script
- [ ] MacOS and Linux support
- [ ] VSCode and Replit starter templates

---

## Author

**Beta**  
Developer of the DSL, interpreter, and linker  
Also known as "Class Software Engineer"

---

## License

This project is licensed under the MIT License.

Copyright (c) 2025 Beta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.