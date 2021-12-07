import discord
from discord.ext.commands.core import check
from discord.flags import Intents
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import MissingPermissions
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.ui import Select
import random
import time
import json

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

driver.get("https://roblox.com/login")

intents = discord.Intents().all()
client = commands.Bot(command_prefix = "+", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name + "#" + client.user.discriminator)
    print(client.user.id)
    print('----------')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/emppu-dev")) # dont change / edit this line of code if u gonna make ur bot public

guilds = len(list(client.guilds))

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Commands", description = "`+r <roblox asset link>` Mass Report (You can report decals, t-shirts, audios and shirts)")
    em.set_footer(text = "byps.cf · https://github.com/emppu-dev")
    await ctx.send(embed = em)

@client.command()
async def r(ctx, arg):

    if "roblox.com" in arg:

        count=0

        t111 = time.time()

        e111 = time.time()
        total111 = e111-t111

        cookies = [
            'cookie1',
            'cookie2'
        ]
        valinta = random.choice(cookies)

        driver.add_cookie({"name": ".ROBLOSECURITY", "value": f"{valinta}"})
        driver.refresh()

        page = requests.get(arg)
        if "Decal" in page.text:
            print("[+] Decal detected")
            whatis = "Decal"
        elif "T-Shirt" in page.text:
            print("[+] T-Shirt detected")
            whatis = "T-Shirt"
        elif "Audio" in page.text:
            print("[+] Audio detected")
            whatis = "Audio"
        elif "Shirt" in page.text:
            print("[+] Shirt detected")
            whatis = "Shirt"
        elif "followPlayerIntoGame" in page.text:
            print("[+] Player detected")
            whatis = "Player"
        else:
            print("[+] Unknown detected")
            whatis = "Unknown"
        f = open("blacklist.txt","r")
        contents = f.read()
        f.close()
        if arg in contents:
            msg = 'You cant report that asset!'
            em = discord.Embed(title = "Something went wrong!", description = msg)
            em.set_footer(text = "byps.cf · https://github.com/emppu-dev")
            await ctx.send(embed = em)
        x = "x"
        if x == "x":
            msg = f'Mass reporting {whatis} `{arg}`'
            em = discord.Embed(title = "Starting", description = msg)
            em.set_footer(text = "byps.cf · https://github.com/emppu-dev")
            # em.set_footer(text = "Only use this command to report stuff like cp, animal cruelty, etc")
            await ctx.send(embed = em)
            assetlink = arg

            driver.get(assetlink)

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "icon-more"))
            )
            element.click()

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "report-item"))
            )
            element.click()

            count = 1
            for _ in range(25):

                t1 = time.time()
                t2 = time.time()
                t3 = time.time()
                t4 = time.time()
                t5 = time.time()
                t6 = time.time()
                t7 = time.time()
                t8 = time.time()
                t9 = time.time()
                t10 = time.time()
                t11 = time.time()
                t12 = time.time()
                t13 = time.time()
                t14 = time.time()
                t15 = time.time()
                t16 = time.time()
                t17 = time.time()
                t18 = time.time()
                t19 = time.time()
                t20 = time.time()
                t21 = time.time()
                t22 = time.time()
                t23 = time.time()
                t24 = time.time()
                t25 = time.time()
                
                ajankohtainen = driver.current_url
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ReportCategory"))
                )
                sel=Select(element)
                sel.select_by_value('7')

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "Comment"))
                )
                if whatis == "Decal":
                    comments = ['Can you please ban this bypassed illegal roblox image that shows and inappropriate image.',
                    'Please ban this inappropriate image.',
                    'Could you please ban this inappropriate image.',
                    'My son just saw this disturbing inappropriate image on here. Could you please take it down.',
                    'bypassed image',
                    'someone made a illegal image',
                    'Disturbing image.',
                    'Take this down.',
                    'Why did you accept this inappropriate image in to your systems?',
                    'Take this image down.',
                    'Dear roblox. Can you please delete this bypassed image.']
                elif whatis == "T-Shirt":
                    comments = ['Can you please ban this bypassed illegal roblox t-shirt that shows and inappropriate image.',
                    'Please ban this inappropriate t-shirt.',
                    'Could you please ban this inappropriate t-shirt.',
                    'My son just saw this disturbing inappropriate t-shirt on here. Could you please take it down.',
                    'bypassed t-shirt',
                    'someone made a illegal t-shirt',
                    'Disturbing t-shirt.',
                    'Take this down.',
                    'Why did you accept this inappropriate t-shirt in to your systems?',
                    'Take this bypassed t-shirt down.',
                    'Dear roblox. Can you please delete this bypassed t-shirt.']
                elif whatis == "Audio":
                    comments = ['Can you please ban this bypassed illegal roblox Audio that is very loud and has swear words in it.',
                    'Please ban this inappropriate Audio that has bad words in it.',
                    'Could you please ban this inappropriate Audio.',
                    'My son just heard this disturbing inappropriate Audio on here. Could you please take it down.',
                    'bypassed Audio',
                    'someone made a illegal Audio',
                    'Super loud Audio.',
                    'Take this bypassed Audio down please.',
                    'Why did you accept this inappropriate Audio in to your systems?',
                    'Take this Audio that has swear words in it down.',
                    'Dear roblox. Can you please delete this bypassed Audio.']
                elif whatis == "Shirt":
                    comments = ['Can you please ban this bypassed illegal roblox shirt that shows this innapropriate image.',
                    'Please ban this inappropriate shirt.',
                    'Could you please ban this inappropriate shirt.',
                    'My son just saw this disturbing inappropriate shirt on here. Could you please take it down.',
                    'bypassed shirt',
                    'someone made a illegal shirt',
                    'Disturbing shirt.',
                    'Take this down.',
                    'How did you accept this inappropriate shirt in to your systems?',
                    'Take this shirt down.',
                    'Dear roblox. Can you please delete this bypassed shirt.']

                element.send_keys(random.choice(comments))

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "report-abuse"))
                )
                element.click()
                driver.get(ajankohtainen)
                print(f"[+] Reported {assetlink} - {count} Times")
                count = count + 1

                e1 = time.time()
                e2 = time.time()
                e3 = time.time()
                e4 = time.time()
                e5 = time.time()
                e6 = time.time()
                e7 = time.time()
                e8 = time.time()
                e9 = time.time()
                e10 = time.time()
                e11 = time.time()
                e12 = time.time()
                e13 = time.time()
                e14 = time.time()
                e15 = time.time()
                e16 = time.time()
                e17 = time.time()
                e18 = time.time()
                e19 = time.time()
                e20 = time.time()
                e21 = time.time()
                e22 = time.time()
                e23 = time.time()
                e24 = time.time()
                e25 = time.time()

                total1 = e1-t1
                total2 = e2-t2
                total3 = e3-t3
                total4 = e4-t4
                total5 = e5-t5
                total6 = e6-t6
                total7 = e7-t7
                total8 = e8-t8
                total9 = e9-t9
                total10 = e10-t10
                total11 = e11-t11
                total12 = e12-t12
                total13 = e13-t13
                total14 = e14-t14
                total15 = e15-t15
                total16 = e16-t16
                total17 = e17-t17
                total18 = e18-t18
                total19 = e19-t19
                total20 = e20-t20
                total21 = e21-t21
                total22 = e22-t22
                total23 = e23-t23
                total24 = e24-t24
                total25 = e25-t25
                total111 = e111-t111
                vastaus = total1+total2+total3+total4+total5+total6+total7+total8+total9+total10+total11+total12+total13+total14+total15+total16+total17+total18+total19+total20+total21+total22+total23+total24+total25+total111

                if count > 25:
                    print("[+] Done")
                    msg = f'Done {ctx.author.mention} `{vastaus}s`'
                    em = discord.Embed(title = f"Mass reporting {whatis} done", description = msg)
                    em.set_footer(text = "byps.cf · https://github.com/emppu-dev")
                    await ctx.send(embed = em)

        elif whatis == "Unknown":
            msg = f'You cant report this type({whatis}) yet'
            em = discord.Embed(title = "Error", description = msg)
            em.set_footer(text = "byps.cf · https://github.com/emppu-dev")
            # em.set_footer(text = "Only use this command to report stuff like cp, animal cruelty, etc")
            await ctx.send(embed = em)

    else:
        msg = f'Something went wrong!'
        em = discord.Embed(title = "Error", description = msg)
        em.set_footer(text = "byps.cf · https://github.com/emppu-dev")
        await ctx.send(embed = em)

@client.command()
async def credits(ctx):
    msg = 'Coding: https://emppu.cc/ - https://github.com/emppu-dev'
    em = discord.Embed(title = "Credits", description = msg)
    await ctx.send(embed = em)

client.run("YOUR_TOKEN")
