#!/usr/bin/env python3
import os
import sys

from atproto import Client
from atproto.exceptions import RequestException, UnauthorizedError
from collections import defaultdict
from datetime import datetime
from dotenv import load_dotenv


def main():

    load_dotenv()

    user_handle = os.getenv("BLUESKY_HANDLE")
    user_password = os.getenv("BLUESKY_PASSWORD")
    posts_filter = os.getenv("POSTS_FILTER")

    client = Client()
    try:
        client.login(user_handle, user_password)
    except (RequestException, UnauthorizedError) as err:
        print("Error logging in: %s" % err.response.content.message)
        sys.exit(1)

    posts_by_year = defaultdict(int)
    cursor = None

    while True:
        response = client.get_author_feed(
            actor=user_handle, limit=100, cursor=cursor, filter=posts_filter
        )

        for feed_item in response.feed:
            if feed_item.post.record.created_at:
                year = datetime.fromisoformat(feed_item.post.record.created_at).year
                posts_by_year[year] += 1

        if not response.cursor:
            break
        cursor = response.cursor

    print(f"{user_handle} made this many posts ({posts_filter}) in:\n")

    for year, count in sorted(posts_by_year.items()):
        print(f"{year}{count:>8}")


if __name__ == "__main__":
    main()
