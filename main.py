import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
TOKEN = ("MTM2NjcwNTI4NDkxNDg3MjM2MA.GaHlkr.e04n0gwYqr-hxTrjzqo5nZMo7yFwY-XuIQ7Lso")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Web server agar bot tetap hidup (untuk Replit atau Railway)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!", 200

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Event sambut member baru
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')  # ubah sesuai nama channel
    if channel:
        await channel.send(f"Selamat datang di server, {member.mention}!")

# Command: halo
@bot.command()
async def halo(ctx):
    await ctx.send(f"Halo {ctx.author.mention}, selamat datang di server!")

# Command: motivasi
@bot.command()
async def motivasi(ctx):
    await ctx.send("Jangan menyerah, masa depan milik mereka yang terus berjuang!")

# Command: pantun
@bot.command()
async def pantun(ctx):
    await ctx.send("Jalan-jalan ke Kalimantan,
Beli durian sama si Paman,
Kalau kamu ingin jadi andalan,
Teruslah belajar dengan ketekunan!")

# Command: materi
@bot.command()
async def materi(ctx):
    await ctx.send("Lihat materi lengkap di channel #materi")

# Command: pengumuman
@bot.command()
async def pengumuman(ctx):
    await ctx.send("Cek pengumuman terbaru di channel #pengumuman")

# Command: tanya pak nastain
@bot.command()
async def tanya(ctx, *, pertanyaan):
    await ctx.send(f"{ctx.author.mention} bertanya ke Pak Nastain: {pertanyaan}\n<@userID_PakNastain>")  # ganti userID_PakNastain

# Aktifkan server dan jalankan bot
keep_alive()
bot.run(TOKEN)
