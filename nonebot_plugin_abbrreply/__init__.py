import aiohttp
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event


async def get_sx(word):
    url = "https://lab.magiconch.com/api/nbnhhsh/guess"

    headers = {
        'origin': 'https://lab.magiconch.com',
        'referer': 'https://lab.magiconch.com/nbnhhsh/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
    data = {
        "text": f"{word}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, data=data) as resp:
            msg = await resp.json()
            return msg if msg else []


sx = on_command(cmd="sx", aliases={"缩写"})


# 识别参数 并且给state 赋值

@sx.handle()
async def sx_rev(bot: Bot, event: Event, state: dict):
    msg = str(event.message).strip()
    date = await get_sx(msg)
    try:
        name = date[0]['name']
        print(name)
        content = date[0]['trans']
        print(content)
        await bot.send(event=event, message=name + "\n" + str(content))
    except :
        await bot.send(event=event, message="没有找到缩写")

