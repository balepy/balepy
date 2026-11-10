<p align="center">
  <img src="./assets/logo.png" width="200" alt="BalePy Logo" style="border-radius: 50px;">
</p>

<h1 align="center">balepy</h1>

<h3 align="center">
  A Python library for creating bots using the Bale Messenger API.
</h3>

<p align="center">
  <a href="https://balepy.xyz">Documentation</a> |
  <a href="https://ble.ir/balepy_gap">Community</a> |
  <a href="https://ble.ir/balepy">Channel</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/balepy/">
    <img src="https://static.pepy.tech/personalized-badge/balepy?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads" alt="PyPI Downloads">
  </a>
</p>

## Installation and Updates

### Install from PyPI (Recommended)

```bash
pip install -U balepy
```

### Install the Latest Development Version from GitHub

```bash
pip install -U git+https://github.com/balepy/balepy.git
```

## Quick Start

```python
from balepy import Client, filters
from balepy.types import Message

app = Client("MyBot", "TOKEN")

@app.on_message(filters.command("start"))
async def start_handler(message: Message):
    await message.reply("سلام! ربات شروع شد 🌿")

@app.on_message(filters.text)
async def echo(message: Message):
    await message.reply(message.text)

app.run()
```

## Support for Other Messengers

BalePy is designed around the Bale Bot API and can also be configured to work with other messengers that provide compatible Bot APIs.

### Telegram

```python
app = Client(
    "MyBot",
    "TOKEN",
    base_url="https://api.telegram.org"
)
```

### Soroush Plus (SPlus)

```python
app = Client(
    "MyBot",
    "TOKEN",
    base_url="https://api.splus.ir"
)
```

### Bale (Default)

```python
app = Client("MyBot", "TOKEN")
```

**Note:** Compatibility with other messengers depends on their API specifications and supported methods.

## Contributing

Contributions are welcome!

If you find a bug, have a feature request, or want to improve the library, feel free to:

- Open an issue to report bugs or suggest new features.
- Submit a pull request with your improvements.
- Help improve the documentation.

Every contribution is appreciated!

## License

Balepy is released under the [MIT License](https://github.com/Erfan-Bafandeh/balepy/blob/main/LICENSE).

