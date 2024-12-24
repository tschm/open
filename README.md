# Experiments with openBB

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

## The problem

Given $N$ random points in an $m$ dimensional space we compute
the center $x$ and the radius $r$ of a ball such that all $N$
points are contained in this ball.

## Makefile

Create the virtual environment defined in requirements.txt using

```bash
make install
```

## Marimo

We use Marimo (instead of Jupyter) to perform our experiments. Start with

```bash
make marimo
```
