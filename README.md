![](https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg)
# TMDB CLI FOR DATAIKU ![](https://img.shields.io/badge/python-%3E%3D3.7-green) ![](https://img.shields.io/badge/status-beta-orange)

This is my private repo for Dataiku coding assignment

## The aim

This project is a first version of a CLI for The Movie Database Project (more infos here: https://www.themoviedb.org).
Today, there's only one Cli command implemented called "withcast"
This command retrieves all movies where all actors passed in parameters played togethers.

## Installation

We recommand to install a virtual environment in order to have a clean install.
Clone the repo, and do the following: 
```
cd tmdbcli
python3 -m venv venv
source venv/bin/activate
pip install . 
```
### Development Mode

As you may probably want add your own cli command, you can install the package in a development mode :

```
pip install -e .[extras]
```
## Quickstart

```
export API_KEY
tmdbcli withcast
```
## Architecture

The basic architecture of the project aims to be modulable and scalable easily.

