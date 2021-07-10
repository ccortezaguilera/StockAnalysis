#!/bin/bash
# to start the container
docker run --name mycontainer -p 8000:80 -e MODULE_NAME="stockanalysis.main" stockanalysis
