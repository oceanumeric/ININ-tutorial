#!/bin/bash

# install r language server
conda install -y conda-forge::r-languageserver

# install r packages
conda install -y conda-forge::r-pacman
conda install -y conda-forge::r-stringr
conda install -y conda-forge::r-data.table
conda install -y conda-forge::r-sparql
conda install -y conda-forge::r-vtree