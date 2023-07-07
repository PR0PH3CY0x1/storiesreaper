from config.config import read_data

from storiesreaper.banner.banner import init

from storiesreaper.utils.loader import loader
from storiesreaper.utils.profile import profile
from storiesreaper.utils.stories import collect

from storiesreaper.argparser.parser import parser


def main():
    args = parser(

    )

    init()

    config = read_data(
        args.path
    )

    loader_ = loader(
        config['username'],
        config['password']
    )

    profile_ = profile(
        loader_,
        args.username
    ) 

    collect(
        loader_,
        profile_,
        config['path']
    )

    print(
        f"{COLORS['SCANNER']}COLLECTING STOIRES: {config['username']} | {args.username}"
    )


if __name__ == '__main__':
    main()
