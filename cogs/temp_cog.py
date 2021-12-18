import os

import requests
from discord.ext import commands


class TempCog(commands.Cog):
    ENDPOINT_FORMAT = "https://api.switch-bot.com/v1.0/devices/%s/status"

    def __init__(self, bot):
        self.bot = bot
        self.endpoint = self.ENDPOINT_FORMAT % os.getenv("SWITCHBOT_DEVICE_ID")
        self.token = os.getenv("SWITCHBOT_TOKEN")

    @commands.command()
    async def temp(self, ctx):
        headers = {
            "Authorization": self.token,
        }
        resp = requests.get(self.endpoint, headers=headers).json()

        temp = resp["body"]["temperature"]
        humidity = resp["body"]["humidity"]

        await ctx.send(f"温度: {temp}℃\n湿度: {humidity}%")


def setup(bot):
    bot.add_cog(TempCog(bot))
