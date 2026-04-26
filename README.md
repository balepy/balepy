# BalePy

<p align=center>
<img src="https://balepy.github.io/statics/logo.png" style="width: 200px; height: 200px; border: 1px solid red;" align=center alt="balepy">
</p>
<h3 align="center"> Balepy a Python Library for create bot API in bale messenger  <br> <h5 align=center> <a href="https://balepy.xyz">Docs</a> | <a href="https://ble.ir/balepy_gap">Community</a> | <a href="https://ble.ir/balepy">Channel</a></h3>
<h2 align="center"><a href="https://pypi.org/project/balepy"><img src="https://static.pepy.tech/personalized-badge/balepy?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads" alt="PyPI Downloads"></a></h2>

### Install and Update:
```bash
pip install -U balepy
```

### Start:
```python
from balepy import Client, filters

bot = Client("MyBot", "TOKEN")

@bot.on_message(filters.command("start"))
async def start_handler(message):
    await message.reply("سلام! ربات شروع شد 🌿")

@bot.on_message(filters.text)
async def echo(message):
    await message.reply(message.text)

bot.run()
```

### Contributors
Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

### License
BalePy is released under the MIT License. See the bundled [LICENSE](https://github.com/balepy/balepy/blob/main/LICENSE) file for details.

