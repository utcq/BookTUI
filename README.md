# Installation

To install booktui you will need poppler, to install poppler follow the following instructions

**Arch Linux**
```bash
sudo pacman -S poppler
```

**Debian based**
```bash
sudo apt-get purge build
sudo apt-get update
sudo apt-get install libpoppler-dev
```

----------------------------------------


If you want to read epub files too you'll need epub2txt

**Arch Linux**
```bash
yay -S epub2txt
```

**Other distro**
```bash
git clone https://github.com/kevinboone/epub2txt2.git
cd epub2txt2
make
sudo make install
```

----------------------------------------

Finally the booktui installation

**All Distro**

```bash
cd ~
git clone https://github.com/UnityTheCoder/BookTUI.git
cd BookTUI
python3 -m pip install -r requirements.txt
sudo sudo ln -s ~/BookTUI/main.py /usr/bin/booktui
chmod +x /usr/bin/booktui
```


# Uninstallation

```bash
rm -rf ~/BookTUI
sudo rm /usr/bin/booktui
```


# Updating
```bash
booktui update
```

# Usage

The usage is really simple
```
Usage: booktui file.pdf/.epub [OPTIONAL: page_number]
KEYS: 
    -> = Next page
    <- = Previous page
    Q = exit
    :search = Search a word in text
    N = next found word 
```
![Alt text](https://github.com/UnityTheCoder/BookTUI/blob/main/images/screen6.png?raw=true)
