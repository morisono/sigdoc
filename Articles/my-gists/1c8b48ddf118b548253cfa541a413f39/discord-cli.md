# Discord Cli workflow



- [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter/blob/master/.docs/Using-the-CLI.md)

```sh
DiscordChatExporter.Cli v2.43.3

USAGE
  dotnet DiscordChatExporter.Cli.dll [options]
  dotnet DiscordChatExporter.Cli.dll [command] [...]

OPTIONS
  -h|--help         Shows help text.
  --version         Shows version information.

COMMANDS
  channels          Get the list of channels in a server.
  dm                Gets the list of all direct message channels.
  export            Exports one or multiple channels.
  exportall         Exports all accessible channels.
  exportdm          Exports all direct message channels.
  exportguild       Exports all channels within the specified server.
  guide             Explains how to obtain the token, server or channel ID.
  guilds            Gets the list of accessible servers.

You can run `dotnet DiscordChatExporter.Cli.dll [command] --help` to show help on a specific command.
```

```
To get the token for your personal account:
 *  Automating user accounts is technically against TOS — USE AT YOUR OWN RISK!
 1. Open Discord in your web browser and login
 2. Open any server or direct message channel
 3. Press Ctrl+Shift+I to show developer tools
 4. Navigate to the Network tab
 5. Press Ctrl+R to reload
 6. Switch between random channels to trigger network requests
 7. Search for a request that starts with "messages"
 8. Select the Headers tab on the right
 9. Scroll down to the Request Headers section
 10. Copy the value of the "authorization" header

To get the token for your bot:
 1. Go to Discord developer portal
 2. Open your application's settings
 3. Navigate to the Bot section on the left
 4. Under Token click Copy
 *  Your bot needs to have the Message Content Intent enabled to read messages

To get the ID of a server or a channel:
 1. Open Discord
 2. Open Settings
 3. Go to Advanced section
 4. Enable Developer Mode
 5. Right-click on the desired server or channel and click Copy Server ID or Copy Channel ID
```

## ref

- https://discordhelp.net/discord-token
- [Discord Lookup](https://discord.id/)
- [GitHub - hugonun/discordid2date: Turns a Discord ID (channel, server, user or message) into the creation date.](https://github.com/hugonun/discordid2date)
- [How to Check Discord Account Age – TechCult](https://techcult.com/how-to-check-discord-account-age/)
[Site Unreachable](https://hugo.moe/discord/discord-id-creation-date.html)
## i.e.

```sh
set -x DISCORD_TOKEN ***
set -x SERVER_ID ***
set -x CHANNEL_ID 726495265330298973

# List All
discordx guilds -t $DISCORD_TOKEN 
discordx channels -t $DISCORD_TOKEN -g $SERVER_ID 
discordx dm -t $DISCORD_TOKEN -g $SERVER_ID 



# Export
discordx export -t $DISCORD_TOKEN -g $CHANNEL_ID -p 20mb --media --reuse-media 

# Format 
discordx export -t $DISCORD_TOKEN -f Json/Csv/HtmlDark/HtmlLight/PlainText

# Filter 
discordx export -t $DISCORD_TOKEN --after "2019-09-17 23:34" --before "2019-09-18"
discordx exportguild -t $DISCORD_TOKEN -g $CHANNEL_ID --include-threads all
```