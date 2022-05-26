import discord
import os



bot_token = os.environ['bot_token']
client = discord.Client()



prefix = "."
mentionable_report = '''```py
#Mentionable Roles```'''

def split(s):
    half, rem = divmod(len(s), 2)
    return s[:half + rem], s[half + rem:]



  
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Scanning  " + str(len(client.guilds)) + " servers!"))
    print(f'{client.user} has connected to Discord!')
  

@client.event
async def on_mention(channel):
    global welcome
  
    channel.send(welcome)
    pass


@client.event
async def on_message(message):
    global prefix
    global mentionable_report
    if message.author == client.user:
        return

    
    if "<@bot_user_id>" in message.content:
        welcome = f"""**__👋 I'm Server Inspector!__**
      
I'll help check your server's basic security and inform you without making any changes.
      
Use `{prefix}help` to get my commands. 

**Use this bot in a private channel to prevent vulnerabilities being disclosed.**

***🚨 WARNING: I WILL NOT CHANGE ANY SETTINGS, ONLY SHOW YOU POTENTIONAL VULNERABILITIES 🚨***"""
        await message.channel.send(welcome)
        pass

    def pingable_roles(guild):
        mentionable_report = """```css
            [ AUDIT ]``` 🛡️ - **__ROLE MENTIONABILITY SCAN__**\n"""
        for role in message.guild.roles:
            if role.mentionable:
                mentionable_report += f'**`➡`⚠️ ALERT**: `@{role.name}` is mentionable\n'
        return mentionable_report

    def role_permissions(guild):
        permission_report = """```css
            [ AUDIT ]``` 🛡️ - **__ROLE PERMISSIONS SCAN__**\n"""
        for role in message.guild.roles:
            if role.permissions.administrator == True:
               permission_report += f"**`➡`🚨 CRITICAL:** `@{role.name}` has dangerous permission's. **Detected** `administrator` permission.\n"
              
            else:
                if role.permissions.kick_members == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `kick_members` permission.\n"
                    pass
                elif role.permissions.ban_members == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `ban_members` permission.\n"
                    pass
                elif role.permissions.manage_channels == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `manage_channels` permission.\n"
                    pass
                elif role.permissions.manage_guild == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `manage_guild` permission.\n"
                    pass
                elif role.permissions.view_audit_log == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `view_audit_log` permission.\n"
                    pass
                elif role.permissions.manage_messages == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `manage_messages` permission.\n"
                    pass
                elif role.permissions.mention_everyone == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `mention_everyone` permission.\n"
                    pass
                elif role.permissions.mute_members == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `mute_members` permission.\n"
                    pass
                elif role.permissions.deafen_members == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `deafen_members` permission.\n"
                    pass
                elif role.permissions.move_members == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `move_members` permission.\n"
                    pass
                elif role.permissions.manage_nicknames == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `manage_nicknames` permission.\n"
                    pass
                elif role.permissions.manage_roles == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `manage_roles` permission.\n"
                    pass
                elif role.permissions.manage_webhooks == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `manage_webhooks` permission.\n"
                    pass
                elif role.permissions.manage_emojis == True:
                    permission_report += f"**`➡`⚠️ ALERT:** `@{role.name}` has potentially dangerous permission's. **Detected** `manage_emojis` permission.\n"
                    pass
        return permission_report

    def server_settings(guild):
        print(guild.verification_level)
        print(guild.explicit_content_filter)
        print (guild.name)
        guild_exp_filter = str(guild.explicit_content_filter)
        guild_ver_level = str(guild.verification_level)
        settings_report = """```css
            [ AUDIT ] ``` :shield: - **__SERVER SETTINGS SCAN__**\n"""
        if guild_ver_level == "none":
          settings_report += f"**`➡`:rotating_light: CRITICAL:** **No server verification.**\n"
        elif guild_ver_level == "low":
          settings_report += f"**`➡`:warning: ALERT:** **Low** server verification level.\n"
        elif guild_ver_level == "medium":
          settings_report += f"**`➡` 🆗 ** **Medium** server verification level set.\n"
        elif guild_ver_level == "high":
          settings_report += f"**`➡` ✅ ** **High** server verification level set.\n"
        elif guild_ver_level == "extreme":
          settings_report += f"**`➡` ✅ ** **Highest** server verification level set.\n"
        if guild_exp_filter == "disabled":
          settings_report += f"**`➡` ⚠️ ALERT**: Server Content Filter **disabled**.\n"
        elif guild_exp_filter == "all_members":
          settings_report += f"**`➡` ✅ ** Server Content Filter set to **High**.\n"
        elif guild_exp_filter == "no_role":
          settings_report += f"**`➡` ✅ ** Server Content Filter set to **Medium**.\n"
        return settings_report

    if message.author.guild_permissions.administrator == True:

        
        if message.content.startswith(prefix + "scanmentions"):
            pingable_roles(message.guild)
            await message.channel.send(pingable_roles(message.guild))
            pass

        
        if message.content.startswith(prefix + "help"):
            help = f"""
__**Commands**__

`{prefix}help` - Displays this help page.

`{prefix}contact` - Displays a contact page.        

`{prefix}scanmentions` - Scans all roles and checks mentionable roles.

`{prefix}scanpermissions` - Scans all roles and checks  permissions.

`{prefix}scansettings` - Scans server settings to check for vulnerablities.

`{prefix}scanall` - Performs a full scan.
"""
            await message.channel.send(help)
            pass

      
        if message.content.startswith(prefix + "scanpermissions"):
            permission_report = role_permissions(message.guild)
            permission_report2 = """"""
            permission_report3 = """"""
            permission_report4 = """"""
            permission_report5 = """"""
            permission_report6 = """"""
            permission_report7 = """"""
            rep_len = len(permission_report)
            if rep_len >= 2000:
                permission_report2, permission_report3 = split(permission_report)
                if len(permission_report2) >= 2000:
                    perission_report4, permission_report5 = split(permission_report2)
                    permission_report6, permission_report7 = split(permission_report3)
            if permission_report2 == """""":
                await message.channel.send(permission_report)
                pass
            else:
                if permission_report4 == """""":
                    await message.channel.send(permission_report2)
                    pass
                    await message.channel.send(permission_report3)
                    pass
                else:
                    await message.channel.send(permission_report4)
                    pass
                    await message.channel.send(permission_report5)
                    pass
                    await message.channel.send(permission_report6)
                    pass
                    await message.channel.send(permission_report7)
                    pass

        if message.content.startswith(prefix + "contact"):
          contact = f"""
**__Contact Info__**
        
**Official bot name:** Server Inspector#2618

**Developed by:** BankkRoll.ETH#0573

**Pricing?:** Free!! *Buy me a coffee?* to help hosting costs, greatly appreciated but not required, thanks!

**Buy me a coffee!:** - 0x19C6f06D3ca908F1B276c13e0e0166bD830D992c 

**Contact:** https://twitter.com/bankkroll_eth
          """
          await message.channel.send(contact)
          pass
            
        
        if message.content.startswith(prefix + "scansettings"):
            await message.channel.send(server_settings(message.guild))
            pass

        
        if message.content.startswith(prefix + "scanall"):
            await message.channel.send(""" **__🔍 FULL SCAN REPORT BELOW 🔎__**\n""")
            await message.channel.send(server_settings(message.guild))
            pass
            await message.channel.send(pingable_roles(message.guild))
            pass
            permission_report = role_permissions(message.guild)
            permission_report2 = """"""
            permission_report3 = """"""
            permission_report4 = """"""
            permission_report5 = """"""
            permission_report6 = """"""
            permission_report7 = """"""
            rep_len = len(permission_report)
            if rep_len >= 2000:
                permission_report2, permission_report3 = split(permission_report)
                if len(permission_report2) >= 2000:
                    perission_report4, permission_report5 = split(permission_report2)
                    permission_report6, permission_report7 = split(permission_report3)
            if permission_report2 == """""":
                await message.channel.send(permission_report)
                pass
            else:
                if permission_report4 == """""":
                    await message.channel.send(permission_report2)
                    pass
                    await message.channel.send(permission_report3)
                    pass
                else:
                    await message.channel.send(permission_report4)
                    pass
                    await message.channel.send(permission_report5)
                    pass
                    await message.channel.send(permission_report6)
                    pass
                    await message.channel.send(permission_report7)
                    pass
    else:
        if message.content.startswith(prefix + "scanall") or message.content.startswith(prefix + "scansettings") or message.content.startswith(prefix + "scanpermissions") or message.content.startswith(prefix + "scanmentions") or message.content.startswith(prefix + "contact") or message.content.startswith(prefix + "help") or message.content.startswith(prefix + "prefix"):
            await message.channel.send("Error: Only users with `Administrator` Permission may use this bot.")
            pass
        else:
            pass



if __name__ == '__main__':
    client.run(bot_token)
