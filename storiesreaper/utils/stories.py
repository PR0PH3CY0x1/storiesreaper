def collect(loader, profile, path):
    loader.download_stories(
        userids=profile,
        filename_target=path
    )
