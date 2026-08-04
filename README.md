# <img  src="https://raw.githubusercontent.com/ABSphreak/ABSphreak/master/gifs/Hi.gif" width="30px"> About Me
Hi, I'm **Lorenzo**  
🎓 Third-year **Computer Science** student at *Sapienza University of Rome*

🎯 My main interests include:
- Artificial Intelligence & Computer Vision
- Software Engineering
- Systems and low-level programming

## 🌐 Socials
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/PLACEHOLDER)

# 💻 Tech Stack
<!-- STACK:START -->

![C](https://img.shields.io/badge/C-0B9E06?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-AB7F02?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-019496?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-D80B26?style=for-the-badge)
![Java](https://img.shields.io/badge/Java-6611D4?style=for-the-badge)
![Makefile](https://img.shields.io/badge/Makefile-62950A?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-DA0BF1?style=for-the-badge)
![TypeScript](https://img.shields.io/badge/TypeScript-099D49?style=for-the-badge)

<!-- STACK:END -->

# 🚀 Projects developed
<!-- PROJECTS:START -->

| Project | What it is | Stack |
| :--- | :--- | :--- |
| **[Link-Map](https://github.com/LM-official/Link-Map)** | 🗺️ A personal knowledge base — a digital garden of interlinked notes, published as an interactive graph with Quartz. | `TypeScript` `JavaScript` |
| **[Finger-Slicer](https://github.com/LM-official/Finger-Slicer)** | 🖐️ A webcam Fruit-Ninja alike game where your fingertip is the blade and any photo becomes the fruit | `Python` |
| **[Concrete-Hunters](https://github.com/LM-official/Concrete-Hunters)** | 🌎 Lightweight, dependency-free exploration site — lazy-loaded articles, photo carousels, and password-protected locations (AES-256-GCM). Pure HTML/CSS/JS. | `JavaScript` `HTML` `CSS` |
| **[JBlackjack](https://github.com/LM-official/JBlackjack)** | 🃏 Blackjack game in pure Java Swing — play against AI opponents with accounts, avatars, stats, level progression, looping soundtracks, and a MVC + Observer architecture. | `Java` |
| **[Client-Server-Cryptography](https://github.com/LM-official/Client-Server-Cryptography)** | 🔐 Multithreaded XOR block cipher with a TCP client/server in pure C. Encrypts files block-by-block across threads, sends them over the network, and decrypts them in parallel on the server. | `C` `Makefile` |
| **[C-Precompiler](https://github.com/LM-official/C-Precompiler)** | ⚙️ A dependency-free C preprocessor in pure C: recursively expands quoted #includes, strips comments, and validates identifiers | `C` |

<!-- PROJECTS:END -->

# 📊 GitHub Stats
![](https://github-readme-stats.vercel.app/api?username=LM-official&theme=tokyonight&hide_border=false&include_all_commits=true&count_private=true)<br/>
![](https://streak-stats.demolab.com/?user=LM-official&theme=tokyonight&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=LM-official&theme=tokyonight&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LM-official/LM-official/snake/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/LM-official/LM-official/snake/github-snake.svg" />
  <img alt="A snake eating my contribution graph" src="https://raw.githubusercontent.com/LM-official/LM-official/snake/github-snake.svg" />
</picture>
</div>

---

<div align="center">

🤖 The `Tech Stack` and `Projects developed` sections are generated automatically

</div>

---

## 🛠️ How this README builds itself
Nothing in the generated sections is written by hand. Two scheduled workflows keep them current:
| Workflow | What it does |
| :--- | :--- |
| [update-readme.yml](.github/workflows/update-readme.yml) | Runs [`update_projects.py`](scripts/update_projects.py), which asks the GitHub API for every public (not forked) repository and rewrites two blocks of this file |
| [snake.yml](.github/workflows/snake.yml) | Draws the contribution-graph animation and publishes it to the `snake` branch |

The script reads **only repository metadata** — never the files inside a repository:
| Column | Comes from |
| :--- | :--- |
| `Project` | the repository name |
| `What it is` | the repository's `About` description |
| `Stack` | the `Languages` GitHub detected (the same data behind the coloured languages bar) |

So a project is updated by editing its `About` field on GitHub, never by editing this README.

Badge colours are a **SHA-256** of the language name mapped onto a hue, then darkened until white text stays readable. The hash keeps a language's colour identical between runs — a genuinely random colour would rewrite this file everyday and commit it for nothing.

The two generated blocks live between **HTML markers**:
```
<!-- "STACK:START" -->     ...     <!-- "STACK:END" -->
<!-- "PROJECTS:START" -->  ...     <!-- "PROJECTS:END" -->
```

Everything outside them is hand-written and never touched.

---

## 🎮 Reusing it
It costs nothing to run. Public repositories get unlimited Actions minutes, every service used is a free public one, and there are no API keys or accounts to set up — the workflows use the `GITHUB_TOKEN` GitHub creates for each run.

1. **Clone it and make it yours.** On GitHub, create an empty repository named **exactly your username** — that name is what puts a README on a profile page. Then:
```sh
git clone https://github.com/LM-official/LM-official.git YOUR-USERNAME
cd YOUR-USERNAME
rm -rf .git && git init     # drop my history, start yours
git remote add origin https://github.com/YOUR-USERNAME/YOUR-USERNAME.git
```

2. **Replace `LM-official` with your username everywhere.** One find-and-replace across the repository covers all of it: the **stats card**s, the **snake images** and `config.py`.
3. **Rewrite the top of this README** — bio, interests, socials. **Leave** the four `START`/`END` markers alone and everything between them will fill itself in.
4. **Allow the bot to commit**, before pushing: Settings → Actions → General → Workflow permissions → Read and write.
5. **Run it**, by pushing. Both workflows also trigger on every push to `main`, so the first one starts them:
```sh
git add . && git commit -m "My profile"
git push -u origin main
```
6. **Give each of your repositories an `About` description**, since that is what the table shows.

Nothing inside `scripts/` or `.github/` needs touching. The workflows read the owner from the repository itself, so the script already knows whose profile it is building. `USERNAME` in [`config.py`](scripts/config.py) only matters if you run it by hand (not recomended):
```sh
python scripts/update_projects.py
```

---

## ⚙️ Tuning
Everything adjustable lives in [`scripts/config.py`](scripts/config.py):
| Setting | Effect |
| :--- | :--- |
| `SKIP_REPO` | repositories to keep out of the table, on top of the profile one, always skipped |
| `SKIP_LANG` | languages to keep out of every stack, however much of a repository they fill |
| `MAX_DESCRIPTION` | where a long `About` description gets truncated |
| `MAX_STACK` | languages shown per project |
| `MIN_SHARE` | ignore `Languages` below this share of a repository |
| `SATURATION`, `LIGHTNESS` | how vivid and how deep the badges are |
| `MAX_LUMINANCE` | contrast floor against the white badge text |
| `COLOR_SALT` | bump it to any other value to redraw the whole palette |

---

## 👥 Authors
This repository was designed and built by:
- **[LM-official](https://github.com/LM-official)**

---

## 📄 License
Released under the MIT License. See [LICENSE](LICENSE).