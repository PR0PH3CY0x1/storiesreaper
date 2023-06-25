from argparse import ArgumentParser


def parser():
    parser_ = ArgumentParser(
        prog='storiesreaper'
    )

    parser_.add_argument(
        '-u',
        '--username'
    )


    parser_.add_argument(
        '-p',
        '--path'
    )

    return parser_.parse_args()
