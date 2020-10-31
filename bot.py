import discord
from discord.ext import commands
import urllib.request
import datetime
import sqlite3
import time
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='g', intents=intents)
con = sqlite3.connect('Users.db')

@bot.event
async def on_ready():
    print('connecte')


@bot.event
async def on_message(message):
    if message.author.bot:
        return()
    else:
        str_tmp = str(message.author)
        size = len(str_tmp)
        name = str_tmp[:size - 5]
        name = "'" + name + "'"
        str_tmp = "'" + str_tmp + "'"

        #j'arrivais pas a récupérer l'id du coup j'ai trouvé une petite arnaque 
        execut = "UPDATE USERS set id = " + str(str_tmp) +  " where name=" +  str(name)+ ";"

        change_xp = "UPDATE USERS set xp = xp" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
        change_xp_ecrit = "UPDATE USERS set xp_ecrit = xp_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"

        with con:
            curr = con.cursor()
            curr.execute(execut)
            curr.execute(change_xp)
            curr.execute(change_xp_ecrit)

        #un double for (je suis pas très a l'aise avec le sql :(  ) pour récupérer le level et le xp ecrit que j'incrémente)
        for row in curr.execute('SELECT xp FROM USERS WHERE ID = ' + str(str_tmp)):
            for xpp in curr.execute('SELECT level_ecrit FROM USERS WHERE ID = ' + str(str_tmp)):
                    for level_xp in curr.execute('SELECT xp_oral FROM USERS WHERE ID = ' + str(str_tmp)):
                        salut = str(row)
                        lenngtf = len(salut) -2          
                        xp = int (salut[1:lenngtf])

                        leve = str(xpp)
                        length2 = len(xpp) - 3
                        levell = int(leve[1:length2])

                        #row = xp
                        ##c est harcodé pour lxp mais je peux gérer pour changer ca 



                        if (levell < 9 and xp > 30 ):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 30" +  " where id=" +  str(str_tmp)+ ";"

                            messagee = ("Hey! " + str(message.author.name) + "Tu passes au niveau " + str(levell + 1) + ". Continue, monter comme ça et tu toucheras bientôt le soleil! pour passer niveau 10 il faut que tu passes 5h en vocal :sunglasses:")

                            await message.channel.send(messagee)
                            curr.execute(change_level_ecrit)
                            curr.execute(change_xp_ecrit)
                            return()

                        if (levell == 9 and xp > 30 and  level_xp >= 18000):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 30" +  " where id=" +  str(str_tmp)+ ";"

                            messagee = (str(message.author.name) + ", tu as atteint le lvl 10 ! T'es ailes brûlent car tu es beaucoup trop proche du soleil.\n C'est une excellente nouvelle pour toi : Tu peux dorénavant faire ta demande de certification en ouvrant un ticket sur le serveur et avoir ainsi accès à des salons secrets qui risque de te mettre en émoi :speak_no_evil: ")
                            await message.channel.send(messagee)
                            curr.execute(change_level_ecrit)
                            curr.execute(change_xp_ecrit)
                            return()


                        if (levell > 10 and levell < 20 and xp >= 50):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 50" +  " where id=" +  str(str_tmp)+ ";"

                            messagee = (f"Hey" + str(message.author.name) +"! Tu passes au niveau "+ str(levell + 1) + "! Merci d'être encore parmi nous et surtout, garde ta bonne humeur ! :grinning:")
                            await message.channel.send(messagee)
                            curr.execute(change_level_ecrit)
                            curr.execute(change_xp_ecrit)
                            return()

                        if (levell > 20 and levell < 30 and xp >= 90):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 90" +  " where id=" +  str(str_tmp)+ ";"
                            messagee = (f"Hey" + str(message.author.name) + "! Tu passes au niveau "+ str(levell + 1) + "! Merci d'être encore parmi nous et surtout, garde ta bonne humeur ! :grinning:")
                            await message.channel.send(messagee)
                            curr.execute(change_level_ecrit)
                            curr.execute(change_xp_ecrit)
                            return()


                        if (levell > 30 and levell < 40 and xp >= 140):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 140" +  " where id=" +  str(str_tmp)+ ";"

                            messagee =(f"Hey" + str(message.author.name) + " ! Tu passes au niveau " + str(levell + 1) + " ! Continue de monter comme ça et tu deviendra bientôt un dinosaure :sauropod:")
                            await message.channel.send(messagee)
                            curr.execute(change_level_ecrit)
                            curr.execute(change_xp_ecrit)
                            return()

                        if (levell > 40 and levell < 49 and xp >= 200):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 200" +  " where id=" +  str(str_tmp)+ ";"

                            messagee =(f"Hey" + str(message.author.name) + " ! Tu passes au niveau " + str(levell + 1) + " ! Continue de monter comme ça et tu deviendra bientôt un dinosaure :sauropod:. Pour passer level 50, il faut que tu passes 20h en vocal")
                            await message.channel.send(messagee)
                            return()

                        if (levell  == 49 and xp >= 200 and level_xp >= 72000):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 200" +  " where id=" +  str(str_tmp)+ ";"

                            messagee =(f (str(message.author.name)) + ", tu as atteint le lvl 50. Un merci sincère de notre part. Tu obtiens le rôle Ancien. Lorsque tu postes un lien maintenant, cela sera très bien présenté. Et cela, en permanence :heart:")
                            await message.channel.send(messagee)
                            curr.execute(change_level_ecrit)
                            curr.execute(change_xp_ecrit)
                            return()

                        if (levell >= 50 and levell < 70 and xp >= 300):
                            change_level_ecrit = "UPDATE USERS set level_ecrit = level_ecrit" + "+ 1" +  " where id=" +  str(str_tmp)+ ";"
                            change_xp_ecrit =  "UPDATE USERS set xp = xp" + "- 300" +  " where id=" +  str(str_tmp)+ ";"

                            messagee =(f"Salut l'ancien ! Tu passes au niveau "+ " ! Tiens donc, ne serait-ce pas un cheveux blanc qui pousse ? :older_adult:")
                            await message.channel.send(messagee)
                            curr.execute(change_level_ecrit)
                            curr.execute(change_xp_ecrit)
                            return()

                        
                        if (levell >= 70 and xp == 1):
                            messagee =(f (str(message.author.name)) + "! INCROYABLE ! Tu as atteint le niveau levell, c'est le niveau maximum ! Tu es devenu un dinosaure :sauropod: Du coup une récompense spéciale s'offre à toi. Envoie un message privé au fondateur ! :partying_face:")
                            await message.channel.send(messagee)
                            return()
                        

                            #ca execute les changements sql
                            with con:
                                curr = con.cursor()
                                curr.execute(change_level_ecrit)
                                curr.execute(change_xp_ecrit)


@bot.event
async def on_voice_state_update(member, before, after):

   # si le mec se co (on prend alors le timer)
    if(before.channel is None and after.channel is not None):
        with con:
            curr = con.cursor()
            for roww in curr.execute('SELECT * FROM USERS WHERE remote = ' + str(member.id)):
                    for sa in curr.execute('SELECT xp_oral FROM USERS WHERE remote = ' + str(member.id)):
                        name = float(sa[0])
                    
                        sql = ("UPDATE USERS SET start_time = ? where remote = ?")
                        
                        debut = time.time()
                        total = debut - name
                        val = (total, str(member.id)) 
                        curr.execute(sql, val)

    #s'il se déco 

    if after.channel is  None:  
        with con:
            curr = con.cursor()      
            for row in curr.execute('SELECT start_time FROM USERS WHERE remote = ' + str(member.id)):
                for xp in curr.execute('SELECT start_time FROM USERS WHERE remote = ' + str(member.id)):
                                for sa in curr.execute('SELECT xp_oral FROM USERS WHERE remote = ' + str(member.id)):
                                    for si in curr.execute('SELECT xp FROM USERS WHERE remote = ' + str(member.id)):

                                        name = float(sa[0])
                                     
                                        si = float(si[0])
                                
                                        debut = float(row[0])
                                        fin = time.time()
                                        time_log = (fin - debut)


                                        sql = ("UPDATE USERS SET xp_oral = ? where remote = ?")
                                        val = (time_log, str(member.id))
                                        curr.execute(sql, val)

                                        sqll = ("UPDATE USERS SET start_time = ? where remote = ?")
                                        vall = (0.0, str(member.id))
                                        curr.execute(sqll,vall)

                                        xp_gain = (time_log - name) / 60 + 1
                                        xp_gain = round(xp_gain)

                                        sql = ("UPDATE USERS SET xp = ? where remote = ?")
                                        data = (xp_gain + si, str(member.id))
                                        curr.execute(sql, data)
                                        
@bot.event
async def on_member_join(member):
    name = member.name
    name = "'" + name + "'"
    idd = member.id
    idd = "'" + str(idd) + "'"

    execut = "INSERT INTO users VALUES("+ str(idd) + ","+ str(idd) + "," + str(name) + ", 1, 0, 0, 0, 0.0)"
    
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users(id text  PRIMARY KEY, remote text ,name text, level_ecrit INTEGER  , xp INTEGER  , xp_ecrit INTEGER  , xp_oral, start_time float)")
        cur.execute(execut)
        cur.execute("SELECT * FROM USERS")

 # pour retirer l'xp et eviter tout probleme, si un pelo se deco reco, bah il est niveau 1 :( (je vais cdder un truc pour que le fondateur puisse mettre le level de quelqu un commpe il veut)

@bot.event
async def on_member_remove(member):    
    memberr = member.id
    member = "'" + str(memberr) + "'" 
    execut =  ("DELETE from users where remote = " + member + ";")

    with con:
        cur = con.cursor()
        cur.execute(execut)
        cur.execute("SELECT * FROM USERS")



bot.run("NzY4NTI0NjU2MzA2NDIxODIx.X5BuXA.AKdfOv1Dc32RhKitPrYPjaskZXU")


