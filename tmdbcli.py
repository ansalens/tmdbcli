from json import loads
from requests import get
from argparse import ArgumentParser
from dotenv import load_dotenv
from os import getenv

load_dotenv()
API_KEY = getenv("TMDB_KEY")

def fetch_movies(movie_type, page):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US&page={}".format(movie_type, page)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {}".format(API_KEY)
    }
    response = get(url, headers=headers)
    response_json = loads(response.text)

    print("Currently showing {} movie titles on page {}".format(len(response_json["results"]), response_json["page"]))
    for index, movie in enumerate(response_json["results"], start=1):
        print("{:>2}. {}".format(index, movie["title"]))


def main():
    parser = ArgumentParser(
            prog="tmdbcli",
            description="Fetch movie lists from TMDB API"
    )
    parser.add_argument(
            "-t",
            "--type",
            choices=["playing", "popular", "top", "upcoming"],
            help="fetch playing, popular, top or upcoming movies",
            metavar=""
    )

    parser.add_argument(
            "-p",
            "--page",
            default=1,
            type=int,
            help="fetch more movies from a different page"
    )

    args = parser.parse_args()

    if args.type is None:
        parser.error("Did not specify type of movies to fetch")
    elif args.type == "playing":
        args.type = "now_playing"
    elif args.type == "top":
        args.type = "top_rated"

    fetch_movies(args.type, args.page)


if __name__ == "__main__":
    main()
