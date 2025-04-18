# Bluesky posts counter

A simple Python script that counts how many posts an account made per year.

## Setup

Either use `uv` to install dependencies:

```shell
uv sync
```

Or install them using pip:

```shell
pip install atproto dotenv
```

Copy the `.env.dist` file to `.env`.

Put your Bluesky handle and password into `.env`.

Optionally change the value of `POSTS_FILTER` in `.env`.

## Running it

Run the script:

```shell
uv run main.py
```

Or, if you're in a virtualenv:

```shell
./main.py
```

It should display something like:

```
philgyford.bsky.social made this many posts (posts_with_replies) in:

2023      11
2024      46
2025      55
```
