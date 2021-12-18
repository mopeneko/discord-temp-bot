import os

from discord.ext import commands

INITIAL_EXTENSIONS = [
    "cogs.temp_cog",
]


class Bot(commands.Bot):
    def __init__(self, command_prefix="."):
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            self.load_extension(cog)


def main():
    bot = Bot()
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
