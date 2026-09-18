# Enhanced discordbot.py with Command-Action Mapping System

import string
import keyboard
import time
import asyncio
import random

# My existing globals
commandarea = []
responsearea = ""
bot_token = ""
EXAMPLE_BOT_TOKEN = "123456781234567812345678"
paused = False

# NEW: Command-Action Mapping Dictionary
command_actions = {
    '/say': 'send_message',           # Send custom message
    '/test': 'send_test_message',     # Send test message
    '/sayhi': 'send_greeting',        # Send greeting
    '/joke': 'send_joke',             # Send random joke
    '/troll': 'handle_troll',         # Handle troll commands
    '/status': 'send_status',         # Send bot status
    '/time': 'send_time',             # Send current time
    '/help': 'send_help',             # Send help message
}

# NEW: Response Templates for Different Actions
response_templates = {
    'greeting': [
        "Hello there!",
        "Hi! How's it going?", 
        "Greetings, human!",
        "Hey! Nice to see you!"
    ],
    'jokes': [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call a fake noodle? An impasta!"
    ],
    'troll_rickroll': "**Never gonna give you up, never gonna let you down!**\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ\n\nYou just got rickrolled!"
}

# My existing functions
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        print(f"Pausing bot: {bot_token}...")
        print(f"Paused bot: {bot_token}.")
        print(f"Press R to resume {bot_token}...")

def disable_pause():
    global paused
    keyboard.wait('r')
    paused = not paused
    print(f"Resuming operational performance of app: {bot_token}")

def validation():
    if EXAMPLE_BOT_TOKEN in bot_token or EXAMPLE_BOT_TOKEN not in bot_token:
        return True
    else:
        return False

# My existing async functions
async def send_test_message(bot, message):
    channel_id = 1404372732166012941
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)

async def send_message_to_channel(bot, channel_id, message):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)

# NEW: Action Handler Functions
async def execute_send_message(bot, channel_id, args):
    """Handle /say command - send custom message"""
    message = args
    await send_message_to_channel(bot, channel_id, message)
    return f"Sent message: '{message}'"

async def execute_send_test_message(bot, channel_id, args):
    """Handle /test command - send test message"""
    await send_test_message(bot, "This message was sent from your console!")
    return "Test message sent!"

async def execute_send_greeting(bot, channel_id, args):
    """Handle /sayhi command - send random greeting"""
    greeting = random.choice(response_templates['greeting'])
    await send_message_to_channel(bot, channel_id, greeting)
    return f"Sent greeting: {greeting}"

async def execute_send_joke(bot, channel_id, args):
    """Handle /joke command - send random joke"""
    joke = random.choice(response_templates['jokes'])
    await send_message_to_channel(bot, channel_id, joke)
    return f"Sent joke!"

async def execute_handle_troll(bot, channel_id, args):
    """Handle /troll command with subcommands"""
    if args.lower() == "rickroll":
        message = response_templates['troll_rickroll']
        await send_message_to_channel(bot, channel_id, message)
        return "RICKROLL DEPLOYED! Target trolled successfully!"
    else:
        await send_message_to_channel(bot, channel_id, "Unknown troll type! Try: /troll rickroll")
        return "Unknown troll type specified"

async def execute_send_status(bot, channel_id, args):
    """Handle /status command - send bot status"""
    status_msg = f"Bot Status: Online\nCommands available: {len(command_actions)}\nDSL Version: Beta"
    await send_message_to_channel(bot, channel_id, status_msg)
    return "Status sent!"

async def execute_send_time(bot, channel_id, args):
    """Handle /time command - send current time"""
    import datetime
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_msg = f"Current time: {current_time}"
    await send_message_to_channel(bot, channel_id, time_msg)
    return "Time sent!"

async def execute_send_help(bot, channel_id, args):
    """Handle /help command - send available commands"""
    help_msg = "**Available Commands:**\n"
    for cmd in commandarea:
        help_msg += f"• {cmd}\n"
    help_msg += "\nUse any command followed by arguments!"
    await send_message_to_channel(bot, channel_id, help_msg)
    return "Help sent!"

# NEW: Dynamic Command Executor
async def execute_command(bot, command, args):
    """Execute any registered command dynamically"""
    channel_id = 1404372732166012941  # My default channel
    
    # Get the action for this command
    action = command_actions.get(command)
    
    if not action:
        return f"Unknown command: {command}"
    
    # Map action strings to actual functions
    action_functions = {
        'send_message': execute_send_message,
        'send_test_message': execute_send_test_message,
        'send_greeting': execute_send_greeting,
        'send_joke': execute_send_joke,
        'handle_troll': execute_handle_troll,
        'send_status': execute_send_status,
        'send_time': execute_send_time,
        'send_help': execute_send_help,
    }
    
    # Execute the appropriate function
    func = action_functions.get(action)
    if func:
        return await func(bot, channel_id, args)
    else:
        return f"Action '{action}' not implemented"

# UPDATED: Main Input Command Handler
def inputcmds(bot, systemcommands):
    while True:
        # Pause handling
        while paused:
            time.sleep(0.1)
        
        user_input = input("Enter in the listed commands: ")
        
        # Check if input matches any registered command
        command_found = False
        
        for command in commandarea:
            if user_input.startswith(f"{command} "):
                # Command with arguments
                args = user_input[len(command)+1:]
                print(f"The command: {user_input} executed.")
                
                # Execute command dynamically
                result_future = asyncio.run_coroutine_threadsafe(
                    execute_command(bot, command, args), 
                    bot.loop
                )
                
                try:
                    result = result_future.result(timeout=5)
                    print(result)
                except Exception as e:
                    print(f"Error executing command: {e}")
                
                command_found = True
                break
                
            elif user_input == command:
                # Command without arguments
                print(f"The command: {user_input} executed.")
                
                result_future = asyncio.run_coroutine_threadsafe(
                    execute_command(bot, command, ""), 
                    bot.loop
                )
                
                try:
                    result = result_future.result(timeout=5)
                    print(result)
                except Exception as e:
                    print(f"Error executing command: {e}")
                
                command_found = True
                break
        
        # Handle system commands
        if user_input == systemcommands[0]:
            print("This will disable your bot. Are you sure you wanna disable? (Y/N): ")
            b = input()
            if b == "Y":
                print(f"Disabling {bot_token}...")
                exit()

        elif user_input == systemcommands[1]:
            toggle_pause()
            disable_pause()
        
        # If no command found, show error
        if not command_found and user_input not in systemcommands:
            print(f"Unknown command: {user_input}")
            print(f"Available commands: {', '.join(commandarea)}")
            print(f"System commands: {', '.join(systemcommands)}")