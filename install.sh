#!/bin/bash

# Update and upgrade system
apt-get update && sudo apt-get upgrade -y

# Install gfortran
apt-get install -y gfortran

# Install required dependencies for R packages
apt-get install -y libstdc++-dev

# Install 'igraph' R package
Rscript -e 'install.packages("igraph", repos="http://cran.rstudio.com/")'

# Install 'vtree' R package
Rscript -e 'install.packages("vtree", repos="http://cran.rstudio.com/")'

# Install 'psych' R package
Rscript -e 'install.packages("psych", repos="http://cran.rstudio.com/")'
