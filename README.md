# tmdbcli
The Movie Database (TMDB) command line API tool for fetching movies.
With this mini tool you can get a list of upcoming, top rated, popular or now playing movies.
[Original project URL.](https://roadmap.sh/projects/tmdb-cli)

## Example usage

```sh
$ python3 tmdbcli.py -t popular -p 2
Currently showing 20 movie titles on page 2
 1. The Gorge
 2. Demon City
 3. Frogman
 4. Hellhound
 5. The Monkey
 6. A Minecraft Movie
 7. The Vigilante
 8. Sky Force
 9. Dark Match
10. Companion
11. I, the Executioner
12. Kraven the Hunter
13. Amaran
14. Plankton: The Movie
15. Giro final
16. Venom: The Last Dance
17. Flow
18. Memoir of a Snail
19. Solo Leveling -ReAwakening-
20. Mickey 17
```

## Prerequisites

- Python >=3.9
- requests, dotenv modules
- [TMDB API key](https://www.themoviedb.org/login)

## Installation

1. Clone repository

```sh
git clone https://github.com/ansalens/tmdbcli
cd tmdbcli
```

2. Create a virtual environment

```sh
python -m venv .venv
```

3. Activate venv

```sh
source .venv/bin/activate
```

4. Install required modules

```sh
pip install -r requirements.txt
```

5. Create your own .env file and put your API key inside it following the format

```sh
API_KEY=insert_api_key_here
```

- Or use output redirection to create .env file from shell

```bash
echo "API_KEY=insert_api_key_here" > .env
```

