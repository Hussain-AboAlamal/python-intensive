import asyncio
import os
import shutil
import sys
import time

import aiohttp
import aiofiles
import requests

SEPARATOR = os.sep
DIRECTORY_PATH = 'pokemons'
"""The directory name that contains pokemons images
"""


async def get_pokemon(session, url):
    """Fetch pokemon data from api

    Args:
        session (_type_): HTTP request session
        url (str): url of the pokemon data

    Returns:
        dict: pokemon name and his sprite images
    """
    async with session.get(url) as resp:
        pokemon = await resp.json()
        # tasks = []
        content: list[str] = []
        sprites: dict = pokemon['sprites'];
        for key in sprites:
            sprite = sprites[key]
            if type(sprite) == str and sprite is not None:
                image = requests.get(sprite).content
                content.append(image)

        directory: dict = {
            'name': pokemon['name'],
            'content': content
        }

        return directory


async def main(items):
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
    async with session:

        tasks = []
        for number in items:
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)

        # delete and re-create pokemons directory
        shutil.rmtree(DIRECTORY_PATH, ignore_errors=False, onerror=None)
        os.makedirs(DIRECTORY_PATH)

        for pokemon in original_pokemon:
            # create a directory for each pokemon name
            os.makedirs(f'{DIRECTORY_PATH}{SEPARATOR}{pokemon["name"]}')
            for index, sprite in enumerate(pokemon['content']):
                # create an image for each pokemon sprite
                fName = f'{DIRECTORY_PATH}{SEPARATOR}{pokemon["name"]}{SEPARATOR}image{index+1}.jpg'
                async with aiofiles.open(fName, mode='wb') as file:
                    await file.write(sprite)

if __name__ == "__main__":
    # get pockemons ID's from user input
    items = input("Please enter the ID's of pockemons to fetch separated by space: ")
    items = items.split();

    # check that user has entered valid values
    if len(items) < 1:
        print('You havn\'t entetred a valid values')
        sys.exit()
    
    # calculate the running time of the process
    s = time.perf_counter()
    print('Downloading iamges, it may take a while')
    asyncio.run(main(items))
    elapsed = time.perf_counter() - s
    print(f"executed in {elapsed:0.2f} seconds.")
