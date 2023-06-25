from instaloader import Instaloader


def loader(username, password):
    loader_ = Instaloader()
    loader_.login(
        username,
        password
    )

    loader_.download_stories()

    return loader_
