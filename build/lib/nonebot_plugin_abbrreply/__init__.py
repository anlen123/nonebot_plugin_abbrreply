import aiohttp

from nonebot.adapters.onebot.v11 import Message
from nonebot.params import T_State
from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11 import Bot,Event
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name='缩写查询器',
    description='输入拼音首字母，猜测文字',
    usage=(
        "NoneBot 短句回复 查看插件"
    ),
    extra={
        'menu_template': 'default',
        'menu_data': [
            {
                'func': '缩写查询器',
                'trigger_method': 'on_cmd',
                'trigger_condition': 'sx lsp',
                'brief_des': '查缩写',
                'detail_des': '查缩写'
            },
            {
                'func': '缩写查询器',
                'trigger_method': 'on_cmd',
                'trigger_condition': '缩写 lsp',
                'brief_des': '查缩写',
                'detail_des': '查缩写'
            },
        ],
    }
)

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


sx = on_regex(pattern="^sx\ |^缩写\ (.*)")


@sx.handle()
async def _(bot: Bot,event: Event):
    msg = str(event.get_message())[3:]
    data = await get_sx(msg)
    result = ""
    try:
        data = data[0]
        name = data['name']
        try:
            content = data['trans']
            result += ' , '.join(content)
        except KeyError:
            pass
        try:
            inputs = data['inputting']
            result += ' , '.join(inputs)
        except KeyError:
            pass
        if result:
            await sx.finish(message=name + "可能解释为：\n" + result)
        await sx.finish(message=f"没有找到缩写 {msg} 的可能释义")
    except KeyError:
        await sx.finish(message=f"出错啦")

