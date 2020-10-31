import discord
from discord.ext import commands
import urllib.request
import time
import random
import os
import sqlite3

bot = commands.Bot(command_prefix='g')
con = sqlite3.connect('Users.db')


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game("*help pour me demander de l'aide :)"))
    print("Projet gerald prêt")


@bot.command()
async def rank(ctx):
    i = 0
    j = 0

    arr = []
    arr2 = []
  
    my_classement = []
    
    auteur = str(ctx.message.author)
    auteur = "'" +auteur + "'"
    print (auteur)
    with con:
        curr = con.cursor()

        for rank in curr.execute('SELECT name FROM USERS ORDER BY xp_ecrit DESC;'):
            if (i <= 10):
                i  = i + 1
                arr.append(rank[0])
        i = 0

        for rank in curr.execute('SELECT xp_ecrit FROM USERS ORDER BY xp_ecrit DESC;'):
            if (i <= 10):
                i  = i + 1
                arr2.append(rank[0])


        i = 0
        print("-----------------------")

       

        i = 0
        print("-----------------------")
        for rank in curr.execute('SELECT id FROM USERS ORDER BY xp_ecrit DESC;'):
                i  = i + 1
                if (rank[0] == str(ctx.message.author)):
                    for rank in curr.execute('SELECT xp_ecrit FROM USERS ORDER BY xp_ecrit DESC;'):
                        j = j + 1

                        if (j == i):
                            my_classement.append(j)
                            my_classement.append(rank[0])


        
        print("classement :", my_classement[0],"nombre de points: " ,my_classement[1])
        for i in range(len(arr)):
            print(arr[i], arr2[i])
    
           
bot.run("NzcxNDQzNzk2NjU0NDI0MDY2.X5sNBQ.7me53kBhTx75aO9I3knjtc5aWWs")