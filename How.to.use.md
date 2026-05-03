<div align="center">

<img src="https://i.gyazo.com/eede5ec8d371e0208e446f11c3e08cfb.png" alt="Fuckdl banner" width="720">

# 🔴🟡 **How to use Fuckdl** 🟡🔴
### *Modded version of Vinetrimmer with latest updates*

![Theme](https://img.shields.io/badge/UI-Red%20%26%20Gold-B8860B?style=for-the-badge&labelColor=8B0000)
![Guide](https://img.shields.io/badge/Setup-Step%20by%20Step-FFD700?style=for-the-badge&labelColor=B22222)
[![Telegram](https://img.shields.io/badge/Telegram-%40barbiedrm-FFD700?style=for-the-badge&labelColor=8B0000&logo=telegram)](https://t.me/barbiedrm)

</div>

---

## 🟥 1. Install Python

Install **Python 3.10 – 3.12**.
✅ Tick **"Add Python to PATH"** during the installer.

> 🟨 Verify with:
> ```powershell
> python --version
> ```

---

## 🟨 2. Install the Visual C++ Redistributable

Required for some native dependencies:

🔗 <https://aka.ms/vs/17/release/vc_redist.x64.exe>

---

## 🟥 3. Run `install.bat`

From the repo root:

```powershell
.\install.bat
```

This will:

- 🔴 Verify Python is installed and on `PATH`
- 🟡 Install / upgrade **Poetry**
- 🔴 Configure Poetry to keep the venv inside the project
- 🟡 Install all Fuckdl dependencies into `.venv\`

When it finishes, you can verify the install with:

```powershell
.\help.bat
```

You should see the **red & gold banner** and the help screen.

---

## 🟨 4. Cookies (sites that use browser sessions)

Install the Firefox add-on **Cookies.txt One Click**:
🔗 <https://addons.mozilla.org/en-US/firefox/addon/cookies-txt-one-click/>

Then for each site, log in, click the add-on, save the file as
**`default.txt`**, and place it under
`Fuckdl\Cookies\<ServiceFolder>\default.txt`.

| 🔴 Site | 🟡 Cookie folder |
|---|---|
| `max.com` | `Fuckdl\Cookies\Max\default.txt` |
| `primevideo.com` / `amazon.com` | `Fuckdl\Cookies\Amazon\default.txt` |
| `tv.apple.com` | `Fuckdl\Cookies\AppleTVPlus\default.txt` |
| `tv.apple.com` / `music.apple.com` | `Fuckdl\Cookies\iTunes\default.txt` |
| `disneyplus.com` (cookie mode) | `Fuckdl\Cookies\DisneyPlus\default.txt` |
| `paramountplus.com` | `Fuckdl\Cookies\ParamountPlus\default.txt` |
| `peacocktv.com` | `Fuckdl\Cookies\Peacock\default.txt` |
| `hulu.com` | `Fuckdl\Cookies\Hulu\default.txt` |
| Any other site | `Fuckdl\Cookies\<ServiceName>\default.txt` |

> 🟨 The `<ServiceName>` should match the folder name expected by the
> service module (the same casing used in `download.<Service>.bat`).

---

## 🟥 5. Credentials (sites that use email + password)

For services like **DisneyPlus, Crunchyroll, Crave, Videoland, ParamountPlus,
All4, RakutenTV, BritBox**, etc., open `fuckdl\fuckdl.yml` (use Notepad++ or VS Code) and fill in the `credentials:` block:

```yaml
credentials:
  Crunchyroll: 'email@example.com:YourPassword'
  DisneyPlus:  'email@example.com:YourPassword'
  Crave:       'email@example.com:YourPassword'
  ParamountPlus: 'email@example.com:YourPassword'
  RakutenTV:   'email@example.com:YourPassword'
  Hidive:      'email@example.com:YourPassword'
  Mubi:        'email@example.com:YourPassword'
```

> 🟥 **Important:** every value must be a single string in the form
> `email:password` wrapped in **single quotes**. A common mistake is writing
> `''email:password''` (double single-quotes) which will break YAML parsing.

---

## 🟨 6. CDM device (PlayReady SL2000 / SL3000)

1. Create a new folder under `fuckdl\devices\` (any name, e.g. `my_sl3000`).
2. Drop the two device files into it:
   - `bgroupcert.dat`
   - `zgpriv.dat`
3. Edit `fuckdl\fuckdl.yml` and set the device under `cdm:` for the service
   you want, e.g.:

```yaml
cdm:
  default: 'my_sl3000'
  Amazon:  'my_sl3000'
  DisneyPlus: 'my_sl3000'
```

🟡 Fuckdl will automatically build the `.prd` file and **reprovision it
every hour** so you don't have to.

---

## 🟥 7. Run a download — quick examples

> 🟨 The service **code** is the canonical alias defined in each service
> module (e.g. `AMZN`, `DSNP`, `ATVP`). All codes are listed in the
> [README → Supported Services](README.md#-supported-services) table.

### Amazon — single episode

```powershell
poetry run fuckdl dl -al en -sl en -w S01E1 Amazon `
  https://www.primevideo.com/region/eu/detail/0KRGHGZCHKS920ZQGY5LBRF7MA/
```

### Amazon — full season

```powershell
poetry run fuckdl dl -al en -sl en -w S01 Amazon `
  https://www.primevideo.com/region/eu/detail/0KRGHGZCHKS920ZQGY5LBRF7MA/
```

### iTunes — by movie ID

```powershell
poetry run fuckdl dl -al tr -sl tr iTunes -m umc.cmc.2lj6d47e7094s6ss83j0uppdm
```

### Apple TV+ — single episode

```powershell
poetry run fuckdl dl -al en -sl en -w S01E01 AppleTVPlus `
  https://tv.apple.com/us/show/big-beasts/umc.cmc.7d9yulmth1rvkwpij477qsqsk
```

### Disney+ — print decryption keys only

```powershell
poetry run fuckdl dl -q 1080 --no-cache --keys DSNP `
  entity-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

---

## 🟨 8. Getting help

🔴 General help (all flags):

```powershell
poetry run fuckdl dl -h
```

🟡 Service-specific help (extra options for that service):

```powershell
poetry run fuckdl dl Amazon -h
poetry run fuckdl dl DisneyPlus -h
poetry run fuckdl dl Crunchyroll -h
```

> 🟥 Service-specific options must come **after** the service name.

---

## 🟥 9. Common CLI flags

| 🟡 Flag | 🔴 Meaning |
|---|---|
| `-q` | Resolution (`720`, `1080`, `2160`) |
| `-v` | Video codec (default `H264`) |
| `-a` | Audio codec |
| `-r` | Color range (`SDR` / `HDR` / `DV`) |
| `-w` | Wanted episodes (`S01E01-S02E03`, `S01-S05,S07`) |
| `-al` | Audio language (default `orig`) |
| `-sl` | Subtitle language (default `all`) |
| `-A` | Audio only |
| `-S` | Subtitles only |
| `--list` | List available tracks, don't download |
| `--keys` | Print decryption keys, don't download |
| `--cache` / `--no-cache` | Use / bypass key vault |
| `--proxy` | Proxy URI **or** 2-letter country code |
| `--cdm` | Override CDM device for this run |

---

## 🟨 10. Troubleshooting

| 🔴 Symptom | 🟡 Fix |
|---|---|
| `Could not load user config: while parsing a block mapping` | A YAML quoting mistake in `fuckdl\fuckdl.yml` (often doubled `''…''` quotes). Use single quotes once: `'email:password'`. |
| `tinycss SyntaxWarning: invalid escape sequence '\\\`'` | Harmless warning from a third-party package on Python 3.12+. Ignore, or run with `python -W ignore::SyntaxWarning`. |
| Banner shows `?[38;5;...m` instead of colors | Old Windows console without ANSI. Use **Windows Terminal** or run inside the new Conhost. |
| Service says it needs a region | Use `--proxy <country>` (e.g. `--proxy us`) and configure a provider under `proxy_providers:` in `fuckdl.yml`. |
| `Failed to install Poetry` | Run PowerShell as Administrator and retry `install.bat`. |

---

## 📡 Contact

[![Telegram](https://img.shields.io/badge/Telegram-%40barbiedrm-FFD700?style=for-the-badge&labelColor=8B0000&logo=telegram)](https://t.me/barbiedrm)

<div align="center">

🔴🟡  *Built for archivists. Themed in red & gold.*  🟡🔴

</div>
