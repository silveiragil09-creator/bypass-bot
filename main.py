import os
import sys

import discord

token = os.environ.get("DISCORD_TOKEN")
if not token:
    sys.exit("DISCORD_TOKEN environment variable is not set")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")


if __name__ == "__main__":
    client.run(token)
