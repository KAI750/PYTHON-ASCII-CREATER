#BY KAI

import PIL.Image
import os
import requests
import os, glob, time
from pyfiglet import figlet_format
import fcntl, termios, struct

th, tw, hp, wp = struct.unpack(
    'HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0,
                                                           0)))

BB = '''\033[1;35m ____  _        _    ____ _  __  ____  _     ___   ___  ____   
| __ )| |      / \  / ___| |/ / | __ )| |   / _ \ / _ \|  _ \  
|  _ \| |     / _ \| |   | ' /  |  _ \| |  | | | | | | | | | | 
| |_) | |___ / ___ \ |___| . \  | |_) | |__| |_| | |_| | |_| | 
|____/|_____/_/   \_\____|_|\_\ |____/|_____\___/ \___/|____/  
                                                               \n-BY \33[31mK\033[1;90mA\33[32mI\033[1;35m
        
-DISCORD = https://discord.gg/BB7\033[1;35m

'''

SYMBOLS = ["@", "#", "S", "%", "!", "*", "+", ";", ":", ",", "."]

UNICODE = ["█", "█", "▓", "▓", "▒", "▒", "░", "░", "┉", "┉", " "]


def delt():
    files = glob.glob('images/*')
    for f in files:
        os.remove(f)


def gen_id():
    global uid
    res = requests.get("https://idgen.i-api.repl.co/uid?length=5").json()["id"]
    uid = res


def download(img_name, url):
    res = requests.get(url)
    f = open(f"images/{img_name}.png", "wb")
    f.write(res.content)
    f.close()
    PIL.Image.open(f"images/{img_name}.png").convert("RGBA").save(
        f"images/{img_name}.png")


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


def symbols_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([SYMBOLS[pixel // 25] for pixel in pixels])
    return (characters)


def unicode_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([UNICODE[pixel // 25] for pixel in pixels])
    return (characters)


def imageAscii(new_width=100):
    os.system("cls||clear")
    print(BB + "\033[1;35mPlease Use Fullscreen Mode")
    type = input(
        "\033[1;35m[1]: SYMBOLS ASCII ART\n[2]: UNICODE ASCII ART\n>>>\033[1;35m "
    )
    if type == "1":
        url = input("\033[1;35mImage URL\n>>>\033[1;35m ")
        gen_id()
        try:
            download(uid, url)
            image = PIL.Image.open(f"images/{uid}.png")
        except Exception as e:
            print(
                f"\033[93m{e}\nYou are seeing this error because the image url is not accessible or the image type is not supported\nIgnore the Traceback Error."
            )

        new_image_data = symbols_to_ascii(grayify(resize_image(image)))
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i + new_width)]
                                for i in range(0, pixel_count, new_width))
        os.system("cls||clear")
        print('\033[1;35m' + ascii_image)
        ft = open(f"ascii/{uid}.txt", "wb")
        ft.write(bytes(ascii_image, "UTF-8"))
        ft.close()
        delt()
    elif type == "2":
        url = input("\033[1;35mImage URL\n>>>\033[1;35m ")
        gen_id()
        try:
            download(uid, url)
            image = PIL.Image.open(f"images/{uid}.png")
        except Exception as e:
            print(
                f"\033[93m{e}\nYou are seeing this error because the image url is not accessible or the image type is not supported\nIgnore the Traceback Error."
            )

        new_image_data = unicode_to_ascii(grayify(resize_image(image)))
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i + new_width)]
                                for i in range(0, pixel_count, new_width))
        os.system("cls||clear")
        print('\033[1;35m' + ascii_image)
        ft = open(f"ascii/{uid}.txt", "wb")
        ft.write(bytes(ascii_image, "UTF-8"))
        ft.close()
        delt()
    else:
        imageAscii()


def textAscii():
    os.system("cls||clear")
    gen_id()
    print(BB)
    type = input(
        "\033[1;35m[1]: Standard Font\n[2]: Custom Font\n>>>\033[1;35m ")
    if type == "1":
        text = input("\033[1;35mYour Text\n>>>\033[1;35m ")
        data = figlet_format(str(text), font="standard")
        os.system("cls||clear")
        print('\033[1;35m' + data)
        fta = open(f"ascii/text-{uid}.txt", "wb")
        fta.write(bytes(data, "UTF-8"))
        fta.close()
    elif type == "2":
        styl = input(
            "\033[1;35mFont Name\n (visit 'font.txt' for fonts)\n>>>\033[1;35m "
        )
        text = input("\033[1;35mYour Text\n>>>\033[1;35m ")
        try:
            data = figlet_format(str(text), font=styl)
            os.system("cls||clear")
            print('\033[1;35m' + data)
            fta = open(f"ascii/text-{styl}-{uid}.txt", "wb")
            fta.write(bytes(data, "UTF-8"))
            fta.close()
        except:
            print(f"\33[31mError: {styl} is not a valid font!\33[37m")
            time.sleep(2)
            textAscii()
    else:
        textAscii()


def main():
    os.system("cls||clear")
    print(
        BB +
        "\033[1;35mSelect The Convertor:\n[1]: Image To Ascii\n[2]: Text To Ascii"
    )
    con = input(">>>\033[1;35m ")
    if con == "1":
        imageAscii()
    elif con == "2":
        print("\033[1;35mPlease Use Fullscreen Mode")
        textAscii()
    else:
        main()


main()
