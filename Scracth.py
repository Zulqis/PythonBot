@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx):
    moreoma = ctx.author.id
    message = await ctx.send("Are you sure it's the Scholar ronin not your ronin? react with emoji below")

    emojis = ['<:yesconfirm:877249155846766593>', '<:noconfirm:877249212486668299>']

    # Adds reaction to above message
    for emoji in (emojis):
        await message.add_reaction(emoji)

    def check(reaction, user):
        reacted = reaction.emoji
        return user.id == moreoma and str(reaction.emoji) in emojis

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10, check=check)
    except asyncio.TimeoutError:
        await ctx.send("timeout")
    else:
        if str(reacted) == '<:yesconfirm:877249155846766593>':
            await ctx.channel.purge(limit=number + 2, check=lambda msg: not msg.pinned)
        elif reaction.emoji == '<:noconfirm:877249212486668299>':
            await ctx.send("Alright, we have cancel it")





            # Adds reaction to above message
            for emoji in (emojis):
                await message.add_reaction(emoji)

            def check(reaction, user):
                reacted = reaction.emoji
                return user.id == message.author.id and str(reaction.emoji) in emojis

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10, check=check)
            except asyncio.TimeoutError:
                await message.channel.send("timeout")
            else:
                reacted = reaction.emoji
                if str(reacted) == '<:yesconfirm:877249155846766593>':
                    await message.channel.send('Yay')
                elif str(reacted) == '<:noconfirm:877249212486668299>':
                    await message.channel.send("Alright, we have cancel it")