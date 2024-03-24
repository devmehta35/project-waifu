from flask import Flask, render_template
import aiohttp
import asyncio

app = Flask(__name__)

async def get_image_url(url):
    headers = {'Content-type': 'application/json'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            image = await resp.json()
            return image['url']

@app.route('/')
def home():
    return render_template('index.html')

# Nekos

@app.route('/neko')
def neko():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/neko'))
    return render_template('image.html', image_url=image_url)

@app.route('/nsfw-neko')
def nsfw_neko():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/nsfw-neko'))
    return render_template('image.html', image_url=image_url)

# Hentai 

@app.route('/hentai-ai')
def hentai_ai():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/ai'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-ass')
def hentai_ass():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/ass'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-boobs')
def hentai_boobs():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/boobs'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-creampie')
def hentai_creampie():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/creampie'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-paizuri')
def hentai_paizuri():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/paizuri'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-pussy')
def hentai_pussy():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/pussy'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-random')
def hentai_random():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/random'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-vtuber')
def hentai_vtuber():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/vtuber'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-ecchi')
def hentai_ecchi():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/ecchi'))
    return render_template('image.html', image_url=image_url)

@app.route('/hentai-fucking')
def hentai_fucking():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/fucking'))
    return render_template('image.html', image_url=image_url)

# In Real Life (IRL)

@app.route('/irl-ass')
def irl_ass():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/irl-ass'))
    return render_template('image.html', image_url=image_url)

@app.route('/irl-boobs')
def irl_boobs():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/irl-boobs'))
    return render_template('image.html', image_url=image_url)

@app.route('/irl-creampie')
def irl_creampie():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/irl-creampie'))
    return render_template('image.html', image_url=image_url)

@app.route('/irl-fucking')
def irl_fucking():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/irl-fucking'))
    return render_template('image.html', image_url=image_url)

@app.route('/irl-pussy')
def irl_pussy():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/irl-pussy'))
    return render_template('image.html', image_url=image_url)

@app.route('/irl-random')
def irl_random():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    image_url = loop.run_until_complete(get_image_url('https://nekos.pro/api/irl-random'))
    return render_template('image.html', image_url=image_url)
