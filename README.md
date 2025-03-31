# tmdbcli
The Movie Database (TMDB) command line API tool for fetching movies.
With this mini tool you can get a list of upcoming, top rated, popular or now playing movies.

## Example usage

```sh
$ python3 tmdbcli.py -t top -p 3
Currently showing 20 movie titles on page 3
 1. Gabriel's Inferno: Part III
 2. Hope
 3. Whiplash
 4. Se7en
 5. Radical
 6. Inception
 7. Rear Window
 8. The Legend of Hei
 9. The Silence of the Lambs
10. Spider-Man: Across the Spider-Verse
11. American History X
12. High and Low
13. Lucy Shimmers and the Prince of Peace
14. The Wild Robot
15. Princess Mononoke
16. Dou kyu sei – Classmates
17. Ikiru
18. Back to the Future
19. The Quintessential Quintuplets Movie
20. A Brighter Summer Day
```

## Prerequisites

- Python >=3.9
- requests, dotenv modules
- [TMDB API key](https://www.themoviedb.org/login)

### Installation

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

5. Create your own .venv and put your API key inside it

```sh
API_KEY=insert_api_key_here
```

