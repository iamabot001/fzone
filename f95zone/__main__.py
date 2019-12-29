import getpass
import argparse


from f95zone.paths.pathmeta import PathMeta
from f95zone.crawler.crawler import Crawler
from f95zone.persistence.cache import Cache
from f95zone.persistence.loader import Loader


if __name__ == '__main__':
    argp = argparse.ArgumentParser()
    paths = PathMeta()
    watchlist = paths.cache / 'watchlist'
    data_store = paths.cache / 'data0.pickle'

    argp.add_argument(
        '-usr',
        '--username',
        action='store',
        default=None,
        dest='username',
        help='Username, if you want to login to get links'
    )

    argp.add_argument(
        '-pass',
        '--password',
        action='store',
        default=None,
        dest='password',
        help=(
            'Password for the given username'
            'if empty, you will be safely prompted to enter the password when required'
            'if provided it may echo in the shell history'
            'Recommended: Do not provide via argument'
        )
    )

    argp.add_argument(
        '-f',
        '--force',
        dest='force',
        action='store_true',
        default=False,
        help='force overwrite local database',
    )
    argp.add_argument(
        '-u',
        '--update',
        dest='update',
        action='store_true',
        default=False,
        help='update watchlist'
    )
    argp.add_argument(
        '-e',
        '--export',
        dest='export',
        action='store_true',
        default=False,
        help='export data to json file'
    )
    args = argp.parse_args()

    username = args.username
    if args.username is None:
        password = None
    else:
        password = getpass.getpass("Enter password: ") if args.password is None else args.password

    def generate_watchlist():
        crawler = Crawler(username, password)
        status: bool = crawler.dump()
        if status:
            print("Watchlist generated ...")

    def dump_data():
        print("Caching data, this may take a while ...")
        cache = Cache(username, password)
        status = cache.dump(json_format=True)
        if status:
            print("Data cached")

    def load_data(json_friendly: bool = True) -> list:
        loader = Loader()
        if not json_friendly:
            return loader.content
        else:
            return loader.json_friendly

    def export_cache_to_json():
        Cache(username, password).export_to_json()

    def main():
        if args.update:
            generate_watchlist()
        if args.force:
            dump_data()
        if args.export:
            export_cache_to_json()
        data = load_data(json_friendly=True)
        print(data)

    main()
