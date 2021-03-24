## Infoga - Email OSINT

Infoga is a tool gathering email accounts informations (ip,hostname,country,...) from different public source (search engines, pgp key servers and shodan) and check if emails was leaked using haveibeenpwned.com API. Is a really simple tool, but very effective for the early stages of a penetration test or just to know the visibility of your company in the Internet.

 ![screen](https://raw.githubusercontent.com/m4ll0k/Infoga/master/screen/main.png)

## Installation

```
$ git clone https://github.com/m4ll0k/Infoga.git infoga
$ cd infoga
$ python setup.py install
$ python infoga.py
```

## Usage

```
$ python infoga.py --domain nsa.gov --source all --breach -v 2 --report ../nsa_gov.txt
```

![run_1](https://raw.githubusercontent.com/m4ll0k/Infoga/master/screen/run_2.png)


```
$ python infoga.py --info m4ll0k@protonmail.com --breach -v 3 --report ../m4ll0k.txt
```

![info](https://raw.githubusercontent.com/m4ll0k/Infoga/master/screen/image_5.png)


## Support Docker
### Install Docker Linux
Install Docker
```sh
curl -fsSL https://get.docker.com | bash
```
> To use docker you need superuser power

### Build Image dirsearch
To create image
```sh
docker build -t "infoga:1" .
```
> **dirsearch** this is name the image and **1** is version

### Using dirsearch
For using
```sh
docker run -it --rm "infoga:1" --domain target --source all --breach -v 2
```
> target is the site
