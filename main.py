import discord
from dotenv import load_dotenv  # type: ignore
import os

import asyncio


load_dotenv()  # Lädt die Variablen aus der .env-Datei
# Discord API
# Erstelle eine Discord-Client-Instanz
# und lade die Umgebungsvariablen
# aus der .env-Datei
prefix = os.getenv("COMMAND_PREFIX")  # Hole den Prefix aus der Umgebungsvariable1
if not prefix:
    raise ValueError("COMMAND_PREFIX ist nicht in der .env-Datei definiert!")

class MyClient(discord.Client):  # Erbt von discord.Client
    async def on_ready(self):  # Wird aufgerufen, wenn der Bot bereit ist
          print(f'Logged in as {self.user}')  # Gibt den Namen des Bots aus
    
    async def on_message(self, message):  # Wird aufgerufen, wenn eine Nachricht gesendet wird
        print(f'Message from {message.author}: {message.content}')  # Gibt die Nachricht und den Autor aus
        if message.content.startswith(prefix + 'ping'):  # Wenn die Nachricht mit !ping beginnt
            await message.channel.send('Pong!')
    async def help(self, message):
        if message.content.startswith(prefix + 'help'):
            # Hier können Sie die Hilfe-Nachricht anpassen
            await message.channel.send('Hier ist eine Liste der Befehle:\n!ping - Antwortet mit Pong!\n!help - Zeigt diese Nachricht an.')
        # Hier können Sie weitere Befehle hinzufügen


    
intents = discord.Intents.default()  # Erstellt die Intents
intents.messages = True  # Aktiviert die Nachrichten-Intents
intents.message_content = True  # Aktiviert die Nachrichten-Inhalte-Intents

    
client = MyClient(intents=intents)  # Erstellt den Bot mit den Intents
    
    # Hole den Token aus der Umgebungsvariable
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise ValueError("DISCORD_TOKEN ist nicht in der .env-Datei definiert!")
    
client.run(token)  # Verwenden Sie start() statt run()
