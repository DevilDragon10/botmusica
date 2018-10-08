import discord
import datetime
import random
import asyncio
import time



client = discord.Client()
players = {}
COR = 0xF7FE2E

dcs = ["discord.gg/", "discord.gg//", "https://discord.gg/"]

@client.event
async def on_ready():
    print('Estou ligado')
    print(client.user.name)
    print(client.user.id)
    print('-----Saga------')
    while True:
        await client.change_presence(game=discord.Game(name="Naruto Hero Online"))
        await asyncio.sleep(60)
        await client.change_presence(game=discord.Game(name="Use o !ajuda"))
        await asyncio.sleep(60)


@client.event
async def on_message(message):
    if message.content.startswith('!entrar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "O bot ja esta em um canal de voz")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('!sair'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Sai do canal de voz e a musica parou!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "O bot não esta em nenhum canal de voz.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('!play'):
        try:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
                    mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb)
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))

            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb2 = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
                    mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
                    mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
                    mscemb2.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb2.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb2)
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
            await client.send_message(message.channel, "Error: [{error}]".format(error=e))




    if message.content.startswith('!pause'):
        try:
            mscpause = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscpause)
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))
    if message.content.startswith('!resume'):
        try:
            mscresume = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscresume)
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))

    for listadc in dcs:
        if listadc in message.content.lower():
            if not message.author.server_permissions.administrator:
                return await client.delete_message(message)
                await client.send_message(message.channel, message.author.mention + " ❌ Você precisa da permissao de admin para divulgar!**")

    if message.content.startswith('!falar'):
        def check(msg):
            return msg.content.startswith('!falar')
        message = await client.wait_for_message(author=message.author, check=check)
        falar = message.content[len('!falar'):].strip()
        await client.send_message(message.channel, falar)

    if message.content.startswith('!Aliança'):
        user = message.author
        role = discord.utils.get(user.server.roles, name="Aliança")
        d1 = discord.utils.get(user.server.roles, name="Aliança")
        d2 = discord.utils.get(user.server.roles, name="Sunagakure")
        d3 = discord.utils.get(user.server.roles, name="Konohagakure")
        d4 = discord.utils.get(user.server.roles, name="Akatsuki")
        akat = 0
        user = message.author
        if discord.utils.get(user.roles, name="Akatsuki"):
            await client.send_message(message.channel,"Na Aliança não aceitamos Akatsuki Espião! {}".format(message.author.mention))
            akat = 1
            return akat
        await client.remove_roles(user,d1)
        await client.remove_roles(user,d2)
        await client.remove_roles(user,d3)
        await client.remove_roles(user,d4)
        await client.add_roles(user, role)
        await client.send_message(message.channel, "Agora você faz parte da Aliança Shinobi! {}".format(message.author.mention))
        await client.delete_message(message)

    if message.content.startswith('!aliança'):
        user = message.author
        role = discord.utils.get(user.server.roles, name="Aliança")
        d1 = discord.utils.get(user.server.roles, name="Aliança")
        d2 = discord.utils.get(user.server.roles, name="Sunagakure")
        d3 = discord.utils.get(user.server.roles, name="Konohagakure")
        d4 = discord.utils.get(user.server.roles, name="Akatsuki")
        akat = 0
        user = message.author
        if discord.utils.get(user.roles, name="Akatsuki"):
            await client.send_message(message.channel,"Na Aliança não aceitamos Akatsuki Espião! {}".format(message.author.mention))
            akat = 1
            return akat
        await client.remove_roles(user,d1)
        await client.remove_roles(user,d2)
        await client.remove_roles(user,d3)
        await client.remove_roles(user,d4)
        await client.add_roles(user, role)
        await client.send_message(message.channel, "Agora você faz parte da Aliança Shinobi! {}".format(message.author.mention))
        await client.delete_message(message)

    if message.content.startswith('!doação'):
        def check(msg):
            return msg.content.startswith('!doação')
        message = await client.wait_for_message(author=message.author, check=check)
        falar = message.content[len('!doação'):].strip()
        await client.send_message(discord.Object(id='457532267951161358'), falar)

    if message.content.lower().startswith('!apagar'):
        if not message.author.server_permissions.manage_messages:
            return await client.send_message(message.channel, "**Você não tem permissão para executar esse comando SATANÁS!!! !**")
        try:
            limite = int(message.content[8:]) + 1
            await client.purge_from(message.channel, limit=limite)
            await client.send_message(message.channel, '{} mensagens foram deletadas por {}'.format(limite - 1,message.author.mention))
        except:
            await client.send_message(message.channel, 'Eu não tenho permissão para apagar mensagens nesse servidor.')

    if message.content.lower().startswith('!kick'):
        if not message.author.server_permissions.kick_members:
            return await client.send_message(message.channel, "**Você não tem permissão para executar esse comando bobinho(a)!**")
        try:
            user = message.mentions[0]
            embed = discord.Embed(title="CHUTÃO", colour=discord.Colour(0x191f30),description="Um úsuario não teve sorte, e infelizmente foi kickado de nosso servidor! Pelo menos não foi um ban certo?")
            embed.set_thumbnail(url="https://pictogram-free.com/material/353-pictogram-free.jpg")
            embed.set_footer()
            embed.add_field(name="Informações", value="**O usuario(a) <@{}> foi kickado com sucesso do servidor.**".format(user.id))
            await client.send_message(message.channel, embed=embed)
            await client.kick(user)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario para kickar!**")

    if message.content.lower().startswith('!ban'):
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel, "**Você não tem permissão para executar essa merda!**")
        try:
            user = message.mentions[0]
            embed = discord.Embed(title="BANIDO", colour=discord.Colour(0x191f30),description="O Shinobi pertubou tanto o ADM, que foi banido!")
            embed.set_thumbnail(url="https://pictogram-free.com/highresolution/307-free-pictogram.png")
            embed.set_footer()
            embed.add_field(name="Informações", value="**O Shinobi <@{}> foi banido com sucesso do servidor.**".format(user.id))
            await client.send_message(message.channel, embed=embed)
            await client.ban(user)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario para banir!**")

    if message.content.lower().startswith('!promo'):
        embed = discord.Embed(title="Promoção", colour=discord.Colour(0x191f30),description="Promoção ativa!!")
        embed.set_thumbnail(url="https://pictogram-free.com/highresolution/307-free-pictogram.png")
        embed.set_footer()
        embed.add_field(name="Informação", value="Novas promoção com duração de 20 dias, com 3x do seu real valor!")
        await client.send_message(discord.Object(id='457532267951161358'), embed=embed)

    if message.content.lower().startswith('!nho'):
        await client.delete_message(message)
        embed = discord.Embed(title="Links", colour=discord.Colour(0x191f30),description="Links importantes!!")
        embed.set_thumbnail(url="https://pictogram-free.com/highresolution/307-free-pictogram.png")
        embed.set_footer()
        embed.add_field(name="Informação", value="www.narutohero.com.br, www.narutohero.com.br/forum, www.narutohero.com.br/patch.rar")
        await client.send_message(discord.Object(id='356651093184479244'), embed=embed)

    if message.content.startswith("!ajuda"):
        em2 = discord.Embed(title='📫 Todos meus comandos foram enviado para sua DM.')
        em2.set_thumbnail(url='https://images-ext-2.discordapp.net/external/f0J4oSn6NxHfqrCcwv34yNM_ShHZfS73F3KH2YyeqoE/https/i.imgur.com/pjJOX5J.gif')
        Embed = discord.Embed(title="**Comandos**", color=discord.Colour(0xff0000),description='Todos os comandos existente no BOT.')
        Embed.add_field(name='**⚙Moderação**', value='`!ban`'
                                                      ' `!kick`'
                                                      ' `!vote + assunto da votação`'
                                                      ' `!apagar + quantidade`'
                                                      ' `!lock`'
                                                      ' `!unlock`'
                                                      ' `!fechar`'
                                                      ' `!liberar`')
        Embed.add_field(name='**🕹️Diversão**', value=' `!contagem`'
                                                     ' `!saga + pergunta`'
                                                     ' `!avatar`'
                                                     ' `!xingar + usuário`')
        Embed.add_field(name='**💻Utilidades**', value='`!Aliança ou !aliança`'
                                                        ' `!ping`'
                                                        ' `!serverinfo`'
                                                        ' `!userinfo`'
                                                        ' `!botinfo`')
        Embed.add_field(name='**🎵PlayList**', value=' `!entrar`'
                                                    ' `!sair`'
                                                    ' `!play`'
                                                    ' `!resume`')
        await client.send_message(message.author, embed=Embed)
        await client.send_message(message.channel, embed=em2)

    if message.content.lower().startswith('!botinfo'):
        await client.delete_message(message)
        embedbot = discord.Embed(
            title='**🤖 Informações do Bot**',
            color=0x00a3cc,
            description='\n'
        )
        embedbot.set_thumbnail(url="https://cdn.discordapp.com/attachments/476866172684337152/497246773182464001/screenNaruto_Hero_Online167.jpg")  # Aqui você coloca a url da foto do seu bot!
        embedbot.add_field(name='`💮 | Nome`', value=client.user.name, inline=True)
        embedbot.add_field(name='`◼ | ID`', value=client.user.id, inline=True)
        embedbot.add_field(name='💠 | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
        embedbot.add_field(name='📛 | Tag', value=client.user)
        embedbot.add_field(name='💻 | Servidores', value=len(client.servers))
        embedbot.add_field(name='👥 | Usuarios', value=len(list(client.get_all_members())))
        embedbot.add_field(name='⚙ | Programador', value="`Saga`")  # Aqui você coloca seu nome/discord
        embedbot.add_field(name='🐍 Python  | Version',
                           value="`3.5`")  # Aqui você coloca a versão do python que você está utilizando!
        embedbot.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)

        await client.send_message(message.channel, embed=embedbot)

    if message.content.lower().startswith("!sorteio"):  # esse comandos sorteia um memebro
        if message.author.server_permissions.administrator:
            n = random.choice(list(message.server.members))
            n1 = '{}'.format(n.name)
            m1 = discord.utils.get(message.server.members, name="{}".format(n1))
            embed = discord.Embed(
                title="Sorteiar membro",
                colour=0xab00fd,
                description="Membro sorteado foi {} se fudeu meu irmão!".format(m1.mention)
                )
            hh = await client.send_message(message.channel, "{}".format(m1.mention))
            await client.delete_message(hh)
            await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message("{} você não tem permissão de executar esse comando!".format(message.author.mention))

    if message.content.startswith("!contagem"):
        await client.delete_message(message)
        mensagem = "**5**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**4**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**3**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**2**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**1**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**O Bot Putão é chatão!**"
        await client.send_message(message.channel, mensagem)

    if message.content.lower().startswith('!saga'):
        try:
            respostas = ['Sim', 'Não', 'Talvez', 'Nunca', 'Claro', 'Sei de Nada', 'Pergunte para o Kass', 'Saga morreu não pode responder', 'Pergunte no posto ipiranga']
            resposta = random.choice(respostas)
            mensagem = message.content[5:]
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name="Pergunta:", value='{}'.format(mensagem), inline=False)
            embed.add_field(name="Resposta:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

    if message.content.lower().startswith('!ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=0xFF0000, description='Meu tempo de resposta é `{}ms`!'.format(round((t2 - t1) * 1000)))
        await client.send_message(message.channel, embed=ping_embed)

    if message.content.lower().startswith("!serverinfo"):
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        embed = discord.Embed(title="\n", description="Abaixo está as informaçoes principais do servidor!")
        embed.set_thumbnail(url=message.server.icon_url)
        embed.set_footer(text="{} • {}".format(message.author, horario))
        embed.add_field(name="Nome:", value=message.server.name, inline=True)
        embed.add_field(name="Dono:", value=message.server.owner.mention)
        embed.add_field(name="ID:", value=message.server.id, inline=True)
        embed.add_field(name="Cargos:", value=str(len(message.server.roles)), inline=True)
        embed.add_field(name="Canais de texto:", value=str(len([c.mention for c in message.server.channels if c.type == discord.ChannelType.text])),
                                   inline=True)
        embed.add_field(name="Canais de voz:", value=str(len([c.mention for c in message.server.channels if c.type == discord.ChannelType.voice])),
                                   inline=True)
        embed.add_field(name="Membros:", value=str(len(message.server.members)), inline=True)
        embed.add_field(name="Bots:",
                                   value=str(len([a for a in message.server.members if a.bot])),
                                   inline=True)
        embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),
                                   inline=True)
        embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('!userinfo'):
        try:
            user = message.mentions[0]
            server = message.server
            embedinfo = discord.Embed(title='Informações do usuário', color=0x03c3f5, )
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='Usuário:', value=user.name)
            embedinfo.add_field(name='Apelido', value=user.nick)
            embedinfo.add_field(name='🆔 ID:', value=user.id)
            embedinfo.add_field(name='📅 Entrou em:', value=user.joined_at.strftime("%d %b %Y às %H:%M"))
            embedinfo.add_field(name='📅 Server criado em:', value=server.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='Jogando:', value=user.game)
            embedinfo.add_field(name="Status:", value=user.status)
            embedinfo.add_field(name='Cargos:', value=([role.name for role in user.roles if role.name != "@everyone"]))
            await client.send_message(message.channel, embed=embedinfo)
        except ImportError:
            await client.send_message(message.channel, 'Buguei!')
        except:
            await client.send_message(message.channel, '? | Mencione um usuário válido!')
        finally:
            pass

    if message.content.lower().startswith('!vote'):
        vote = message.content[5:].strip()
        votee = await client.send_message(message.channel,
                                          message.author.mention + " **Iniciou uma votação?**\n\n``" + vote + "``")
        await client.delete_message(message)
        await client.add_reaction(votee, '👍')
        await client.add_reaction(votee, '👎')

    if message.content.lower().startswith('!corrida'):
        await client.send_message(message.channel, "Digite !nome @nomedoUsuario para disputar com alguém")
        def check(msg):
            return msg.content.startswith("!nome")
        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len("!nome".format(message.author.mention)):]
        await client.send_message(message.channel, ":thinking: = {} ".format(message.author.mention))
        await client.send_message(message.channel, ":angry: = {}".format(name))
        await asyncio.sleep(2)
        contagem = 5
        while contagem > 0:
            await client.send_message(message.channel, "***" + str(contagem) + "***")
            await asyncio.sleep(1)
            contagem = contagem - 1
        velocidade1 = random.randint(100, 150)
        velocidade2 = random.randint(100, 150)
        vm1 = velocidade1 / 1
        vm2 = velocidade2 / 1
        metros1 = 0
        metros2 = 0
        while metros1 < 100 and metros2 < 100:
            v1 = random.randint(10, 15)
            v2 = random.randint(10, 15)
            metros1 = metros1 + v1
            metros2 = metros2 + v2
            m1 = await client.send_message(message.channel, ":thinking: = {} ".format(str(metros1)))
            m2 = await client.send_message(message.channel, ":angry: = {}".format(str(metros2)))
            await asyncio.sleep(2)
            await client.delete_message(m1)
            await client.delete_message(m2)
            if metros1 > 100:
                await client.send_message(message.channel, "O Vencedor foi {} obtendo uma velocidade de {} m/s".format(
                    message.author.mention, str(vm1)))
            if metros2 > 100:
                await client.send_message(message.channel, "O Vencedor foi {} obtendo uma velocidade de {} m/s".format(
                    name, str(vm2)))

    if message.content.startswith("!servidores"):
            servidores = '\n'.join([s.name for s in client.servers])
            embe = discord.Embed(title="Olá, sou o Saga, atualmente estou online em " + str(len(client.servers)) + " servidores com " + str(
                len(set(client.get_all_members()))) + " membros!",
                                color=0xFF0000,
                                description=servidores)
            await client.send_message(message.channel, embed=embe)


    if message.content.startswith("!avatar"):
        xtx = message.content.split(' ')
        if len(xtx) == 1:
            useravatar = message.author
            avatar = discord.Embed(
                title="Avatar de: {}".format(useravatar.name),
                color=0x00FF00,
                description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
            )

            avatar.set_image(url=useravatar.avatar_url)
            avatar.set_footer(text="Pedido por {}#{}".format(useravatar.name, useravatar.discriminator))
            await client.send_message(message.channel, embed=avatar)
        else:
            try:
                useravatar = message.mentions[0]
                avatar = discord.Embed(
                      title="Avatar de: {}".format(useravatar.name),
                      color=0x00FF00,
                      description="[Clique aqui]("+useravatar.avatar_url+") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

            except IndexError:
                a = len() + 7
                uid = message.content[a:]
                useravatar = message.server.get_member(uid)
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=0x00FF00,
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

    if message.content.lower().startswith('!fechar'):
        membro = discord.utils.find(lambda r: r.name == "@everyone", message.server.roles)
        fechado = discord.PermissionOverwrite()
        fechado.read_messages = False
        fechado.send_messages = False
        await client.edit_channel_permissions(message.channel, membro, fechado)
        await client.send_message(message.channel, "Canal fechado para membros!")

    if message.content.lower().startswith('!liberar'):
        membro = discord.utils.find(lambda r: r.name == "@everyone", message.server.roles)
        aberto = discord.PermissionOverwrite()
        aberto.read_messages = True
        aberto.send_messages = True
        await client.edit_channel_permissions(message.channel, membro, aberto)
        await client.send_message(message.channel, "Canal Aberto novamente")

    if message.content.lower().startswith('!lock'):
        membro = discord.utils.find(lambda r: r.name == "@everyone", message.server.roles)
        lock = discord.PermissionOverwrite()
        lock.send_messages = False
        await client.edit_channel_permissions(message.channel, membro, lock)
        await client.send_message(message.channel, "Não se pode mandar mensagem nesse canal ate segunda ordem!")

    if message.content.lower().startswith('!unlock'):
        membro = discord.utils.find(lambda r: r.name == "@everyone", message.server.roles)
        unlock = discord.PermissionOverwrite()
        unlock.send_messages = True
        await client.edit_channel_permissions(message.channel, membro, unlock)
        await client.send_message(message.channel, "Já pode mandar mensagem novamente !")

    if message.content.lower().startswith('!abraçar'):
        try:
            user = message.mentions[0]
            embed = discord.Embed(title='{} deu um forte abraço em {}'.format(message.author, user.name), colour=discord.Colour(0x0f0f0f), description='\n')
            embed.set_image(url='https://66.media.tumblr.com/36a8846fadf080496c4ff8000f7126aa/tumblr_o4gzpr5Da11vnh6hco1_500.gif')
            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, "Você precisa marcar alguém seu animal!")

    if message.content.startswith('!xingar'):
        alvo = message.mentions[0]
        user = message.mentions[0]
        embed = discord.Embed(title='Enviando a mensagem via DM para o {} em 3 segundos'.format(user.name))
        await client.send_message(message.channel, embed=embed)
        await asyncio.sleep(0)
        contagem = 3
        while contagem > 0:
            await client.send_message(message.channel, "" + str(contagem))
            await asyncio.sleep(1)
            contagem = contagem - 1
        await client.send_message(alvo, "Vai tomar no cu {} seu lixo!".format(user.mention))

    if message.content.lower().startswith('!skin'):
        user = message.mentions[0]
        prefic = len('!skin') + 1
        body = message.content[prefic:]
        embed = discord.Embed(title='Olha como tu é um merda meu irmão!{}'.format(user.name), color=discord.Colour(0x0f00f),)
        embed.set_image(url="https://mc-heads.net/body/{body}")
        await client.send_message(message.channel, embed=embed)



client.run('NDg3Mzk4MzYwOTk1NzI1MzIz.DpmLBg.i_CTmGoWbaBJFR1W5oocmQ1bjfY')