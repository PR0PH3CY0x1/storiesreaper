from instaloader import Profile


def profile(loader, username):
    profile = Profile.from_username(
        loader.context, 
        username
    )

    return profile
