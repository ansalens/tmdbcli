# tmdbcli
The Movie Database (TMDB) command line API tool for fetching movies.
With this mini tool you can get a list of upcoming, top rated, popular or now playing movies.
[Original project URL.](https://roadmap.sh/projects/tmdb-cli)

### Features

- Obtain details (rating/release date) about now playing, top rated, upcoming and popular movies 
- View movie details from other pages

## Example usage

```sh
$ python3 tmdbcli.py -t top -p 2
Currently showing 20 movie titles on page 2
 1. Fight Club
    | Rating:   8.4
    | Released: 1999-10-15
 2. Cinema Paradiso
    | Rating:   8.4
    | Released: 1988-11-17
 3. Counterattack
    | Rating:   8.4
    | Released: 2025-02-27
 4. City of God
    | Rating:   8.4
    | Released: 2002-08-30
 5. Psycho
    | Rating:   8.4
    | Released: 1960-06-22
<snip>
```

## Prerequisites

- Python >=3.9
- requests, dotenv modules
- [TMDB API key](https://www.themoviedb.org/login)

## Installation

1. Clone repository

```sh
git clone https://github.com/ansalens/tmdbcli; cd tmdbcli
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

