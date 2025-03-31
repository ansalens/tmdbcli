import requests
import json
from argparse import ArgumentParser
from dotenv import load_dotenv
from os import getenv

# Get API key
load_dotenv()
API_KEY = getenv("TMDB_KEY")

def fetch_movies(movie_type, page_number):
    """Fetch movies depending on movie_type argument on page page_number"""
    url = f"https://api.themoviedb.org/3/movie/{movie_type}?language=en-US&page={page_number}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {}".format(API_KEY)
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response_json = json.loads(response.text)
    except requests.exceptions.ConnectionError as conn_err:
        print("Connection couldn't be established.")
        raise SystemExit(conn_err)
    except requests.exceptions.Timeout as time_err:
        print("Took too long to establish a connection.")
        raise SystemExit(time_err)
    except json.JSONDecodeError as json_err:
        print("Failed to decode JSON response")
        raise SystemExit(json_err)

    print("Currently showing {} movie titles on page {}".format(len(response_json["results"]), response_json["page"]))
    for index, movie in enumerate(response_json["results"], start=1):
        print("{:>2}. {}".format(index, movie["title"]))


def main():
    parser = ArgumentParser(
            prog="tmdbcli",
            description="Fetch list of movies from TMDB API"
    )
    parser.add_argument(
            "-t",
            "--type",
            choices=["playing", "popular", "top", "upcoming"],
            help="fetch playing, popular, top or upcoming movies",
            metavar=""
    )

    # page argument has default value 1
    parser.add_argument(
            "-p",
            "--page",
            default=1,
            type=int,
            help="fetch more movies from a different page"
    )

    args = parser.parse_args()

    # movie type is required argument, rename specific arguments to valid API endpoints
    if args.type is None:
        parser.error("Did not specify type of movies to fetch")
    elif args.type == "playing":
        args.type = "now_playing"
    elif args.type == "top":
        args.type = "top_rated"

    fetch_movies(args.type, args.page)


if __name__ == "__main__":
    main()
