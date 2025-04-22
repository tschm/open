# Experiments with openBB

[![CodeFactor](https://www.codefactor.io/repository/github/tschm/open/badge)](https://www.codefactor.io/repository/github/tschm/open)

Install openBB locally with

```bash
make install
```

## Create a local .env file

Set your keys at [OpenBB Hub](https://my.openbb.co/app/platform/credentials)
and get your personal access token from
<https://my.openbb.co/app/platform/pat> to connect with your account.

Create the local .env file and set

```bash
PAT=<COPY of your Personal Access Token>
```

The .env file is listed explicitly in .gitignore.

## Marimo

Start the marimo server with

```bash
make marimo
```

We have a notebook there using the openbb package to extract data.

## Start the openbb REST API

Start with

```bash
make rest
```

Visit the [api docs](https://localhost:8000/docs)
