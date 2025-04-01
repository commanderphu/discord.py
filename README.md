# discord.py Projekt

Dieses Repository enthält einen Discord-Bot, der mit der Bibliothek `discord.py` erstellt wurde. Der Bot ist so konzipiert, dass er mithilfe von Docker einfach eingerichtet und skaliert werden kann.

## Funktionen
- Erstellt mit `discord.py`
- Einfache Bereitstellung mit Docker
- Unterstützt Docker Compose für Multi-Container-Setups

## Voraussetzungen
- Docker auf Ihrem System installiert
- Docker Compose installiert (optional, für Multi-Container-Setups)

## Bereitstellung mit Docker

1. Erstellen Sie das Docker-Image:
    ```bash
    docker build -t discord-bot .
    ```

2. Starten Sie den Container:
    ```bash
    docker run -d --name discord-bot -e DISCORD_TOKEN=Ihr_Token_hier discord-bot
    ```

    Ersetzen Sie `Ihr_Token_hier` durch Ihren tatsächlichen Discord-Bot-Token.

## Bereitstellung mit Docker Compose

1. Erstellen Sie eine `docker-compose.yml`-Datei:
    ```yaml
    version: '3.8'

    services:
      discord-bot:
         build: .
         environment:
            - DISCORD_TOKEN=Ihr_Token_hier
         restart: unless-stopped
    ```

2. Starten Sie den Bot mit Docker Compose:
    ```bash
    docker-compose up -d
    ```

3. Um den Bot zu stoppen:
    ```bash
    docker-compose down
    ```

## Umgebungsvariablen
- `DISCORD_TOKEN`: Ihr Discord-Bot-Token (erforderlich).

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Details finden Sie in der [LICENSE](LICENSE)-Datei.

## Beitrag
Fühlen Sie sich frei, Issues zu eröffnen oder Pull Requests einzureichen, um das Projekt zu verbessern.

## Kontakt
Bei Fragen oder Unterstützung wenden Sie sich an den Repository-Besitzer.