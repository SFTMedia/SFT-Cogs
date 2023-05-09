"""Initialize FindHelp cog."""
import json
from pathlib import Path

from redbot.core.bot import Red

from .findhelp import FindHelp

with Path(__file__).parent.joinpath("info.json").open() as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


async def setup(bot: Red) -> None:
    """Load FindHelp cog."""
    cog = FindHelp(bot)
    await bot.add_cog(cog)