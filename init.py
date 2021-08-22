import discord
import os 
from gsheet import *
import asyncio

client = discord.Client()
sheet = gsheet()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    emojis = ['<:yesconfirm:877249155846766593>', '<:noconfirm:877249212486668299>']

    # Restrict the command to a role
    # Change REQUIREDROLE to a role id or None
    REQUIREDROLE = None
    if REQUIREDROLE is not None and discord.utils.get(message.author.roles, id=str(REQUIREDROLE)) is None:
        await message.channel.send('You don\'t have the required role!')
        return

    statusbot = 'maintenance' 
    embedVaran = discord.Embed(title="Maintenance", description="", color=0xFF0000)
    embedVaran.add_field(name="<:Runfunc:878922516016537642> Add Ronin data ", value="<:whitess:876236898635497472> Working!", inline=False)
    embedVaran.add_field(name="<:Notfunc:878922388283211788> SLP Checking ", value="<:whitess:876236898635497472> DNS error from api lunaciarover", inline=False)
    embedVaran.add_field(name="<:Runfunc:878922516016537642> Help Command ", value="<:whitess:876236898635497472> Working!", inline=False)
        
    #Role AXIE= 870114617655971870

    if message.content.startswith(';mt'):
        await message.delete()
        await message.channel.send(embed=embedVaran)
        return

    if message.content.startswith(';slp-data') and statusbot == 'maintenance':
        await message.channel.send(embed=embedVaran)
        return

    if message.content.startswith(';slp-dm') and statusbot == 'maintenance':
        await message.channel.send(embed=embedVaran)
        return

    if message.content.startswith(';donemt'):
        embedVaran = discord.Embed(title="Maintenance", description="", color=0x35FF03)
        embedVaran.add_field(name="<:Runfunc:878922516016537642> Add Ronin data ", value="<:whitess:876236898635497472> Working!", inline=False)
        embedVaran.add_field(name="<:Runfunc:878922516016537642> SLP Checking ", value="<:whitess:876236898635497472> Working!", inline=False)
        embedVaran.add_field(name="<:Runfunc:878922516016537642> Help Command ", value="<:whitess:876236898635497472> Working!", inline=False)
        await message.delete()
        await message.channel.send(embed=embedVaran)
        return

    if message.content.startswith(';help slp-dm'):
        embedVarslpdm = discord.Embed(title="For ;slp-dm", description="1. Enter your TTB Data first, see ;help for information\n2. Write ;slp-dm and enter", color=0xFF10F0)
        embedVarslpdm.set_image(url="https://i.imgur.com/xQpm3yK.png")
        await message.channel.send(embed=embedVarslpdm)
        return

    # Help slp-check
    if message.content.startswith(';help slp-check'):
        embedVarslpcheck = discord.Embed(title="For ;slp-check", description="Tag users that you want to check after the command", color=0xFF10F0)
        embedVarslpcheck.set_image(url="https://i.imgur.com/Madcsau.png")
        await message.channel.send(embed=embedVarslpcheck)
        return

    # Help ;slp-data
    if message.content.startswith(';help slp-data'):
        embedVarslpdata = discord.Embed(title="For ;slp-data", description="1. Enter your TTB Data first, see ;help for information\n2. Write ;slp-data and enter", color=0xFF10F0)
        embedVarslpdata.set_image(url="https://i.imgur.com/B26SDaC.png")
        await message.channel.send(embed=embedVarslpdata)
        return

    # Help ;ronin-add
    if message.content.startswith(';help ronin-add'):
        embedVarronin = discord.Embed(title="For ;ronin-add 0x", color=0xFF10F0)
        embedVarronin.add_field(name="[Ronin address]", value='1. Copy your Scholar Ronin address without "ronin:" content\n2. Paste it beside 0x without space\n\nEx.\nBefore: "ronin:1a2a1c938ce3ec39b6d47113c7955baa9dd454f2"\n\nAfter: "0x1a2a1c938ce3ec39b6d47113c7955baa9dd454f2"',inline=False)
        embedVarronin.add_field(name="[Share percentage]", value="Look for your share percentage (usually '65%' in TTB)", inline=False)
        embedVarronin.set_image(url="https://i.imgur.com/msC7CAi.png")
        await message.channel.send(embed=embedVarronin)

        embedVarronin2 = discord.Embed(title="wrong format:", color=0xFF10F0)
        embedVarronin2.set_image(url="https://i.imgur.com/vF1Onta.png")
        await message.channel.send(embed=embedVarronin2)
        return

    # Use Tutorial
    if message.content.startswith(';help'):
        embedVar = discord.Embed(title="Team Think Big Scholar SLP Tracker", description="The bot still on build test, so if the command fails you can dm @ZUL | Think Big\n\n", color=0xFF10F0)
        embedVar.add_field(name=";help", value="<:whitess:876236898635497472> help to view this list\n\n", inline=False)
        embedVar.add_field(name=";help [Command]", value="<:whitess:876236898635497472> show help for specific command", inline=False)
        embedVar.add_field(name=";ronin-add 0x[Ronin address] [Share Percentage]", value="<:whitess:876236898635497472> add scholar ronin address\n\n", inline=False)
        embedVar.add_field(name=";slp-data", value="<:whitess:876236898635497472> view your own information\n\n", inline=False)
        embedVar.add_field(name=";slp-dm", value="<:whitess:876236898635497472> view your own information via DM privately\n\n", inline=False)
        embedVar.add_field(name=";slp-check [Scholar Name]", value="<:whitess:876236898635497472> view other scholar's information (Only managers can exec this command)", inline=False)
        embedVar.set_footer(text="Tag moderators if you find some bug", icon_url="https://cdn.discordapp.com/avatars/871606043002691594/e37f424a6cf0c239d7b8a64d9b87ee10.png")
        await message.channel.send(embed=embedVar)

    # RONIN ADD CHECKING FORMAT
    if message.content.startswith(';ronin-add ronin'):
        await message.channel.send('`You cannot put "ronin:" for adding data, see ;help ronin-add`')
        return

    if message.content.startswith(';ronin-add 00'):
        await message.channel.send('`Error format!! for adding data, see ;help ronin-add`')
        return

    if message.content.startswith(';ronin-add 0x['):
        await message.channel.send('`No need to put "[ ]" for adding data, see ;help ronin-add`')
        return

    # CORRECT RONIN ADD FORMAT GOES HERE
    if message.content.startswith(';ronin-add 0x'):
        SPREADSHEET_ID = '1ElZ5f4PdswtqyJ4slioCgBNXlA5lxktJfe6cq6Yq6XI' # Add ID here
        RANGE_NAME = 'BotInput!A2'

        FIELDS = 2 # Amount of fields/cells

        # Code
        embedVar2 = discord.Embed(title="", description="Your TTB Data has been successfully submitted!", color=0x35FF03)
        embedVar3 = discord.Embed(title="", description='Error: You need to add {0} fields [Ronin] and [Share percentage].'.format(FIELDS), color=0xFF10F0)
        embedConfirm = discord.Embed(title='Confirm is that TTB Scholar ronin and not your ronin? (react to confirm)', color=0xFF10F0)
        embedTimeout = discord.Embed(title="Confirm Timeout", description="You must react this emoji <:yesconfirm:877249155846766593> / <:noconfirm:877249212486668299>", color=0xFF0000)

        msg = message.content[10:]
        result = [x.strip() for x in msg.split()]
        if len(result) == FIELDS:
            persen = message.content[53:]
            for word in persen.split():
                word = word.replace('%', '')
                if word.isnumeric():
                    num = int(word)
                    print(num)
                    if num < 0:
                        await message.channel.send("Can't use negative for share percentage") 
                    elif 60 < num < 100:
                        await message.channel.send(embed=embedConfirm)
                        # Adds reaction to above message
                        for emoji in (emojis):
                            await message.add_reaction(emoji)

                        def check(reaction, user):
                            reacted = reaction.emoji
                            return user.id == message.author.id and str(reaction.emoji) in emojis

                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=10, check=check)
                        except asyncio.TimeoutError:
                            #Purge confirm message
                            await message.channel.purge(limit=1)
                            await message.channel.send(embed=embedTimeout)
                            return
                        else:
                            reacted = reaction.emoji
                            if str(reacted) == '<:yesconfirm:877249155846766593>':
                                #Purge confirm message
                                await message.channel.purge(limit=1)
                                # Add
                                print(message.created_at)
                                DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + result
                                sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
                                await message.channel.send(embed=embedVar2)
                                return
                            elif str(reacted) == '<:noconfirm:877249212486668299>':
                                #Purge confirm message
                                await message.channel.purge(limit=1)
                                await message.channel.send("`Alright, we cancel it and have a nice day!`<a:byee:878389556221726841>")
                                return
                    else:
                        await message.channel.send('Share percentage range is 60 - 100')
                        return
        else:
            # Needs more/less fields
            await message.channel.send(embed=embedVar3)
            return

    if message.content.startswith(';ronin-add'):
        await message.channel.send('`Wrong format!! Please add 0x before the address, see ;help ronin-add`')
        return

    # Whois
    # Please dont remove the copyright and github repo
    elif len(message.mentions) > 0:
        for muser in message.mentions:
            if muser.id == client.user.id:
                if any(word in message.content for word in ['what','this']):
                    await message.channel.send('umm me? TTB Utility Tools Bot v1')
                if any(word in message.content for word in ['cool']):
                    await message.channel.reply("You're cool too!!")
                if any(word in message.content for word in ['error']):
                    await message.channel.send('alright, error reported to <@188289061708890113> thankyou!')


client.run('ODcxNjA2MDQzMDAyNjkxNTk0.YQdwYg.8wM1AqnWk1GSGYjYM5MYvBQavTw') # Add bot token here
