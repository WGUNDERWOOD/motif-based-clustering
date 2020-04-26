#!/usr/bin/env bash

# check running in right directory
if [ ${PWD##*/} != "motif-based-clustering" ]
then
  echo "wrong directory!"
  exit
fi

# base directory
basedir=$PWD

# python
echo "Python"
cd $basedir/python/
pytest --profile-svg

cd $basedir/python/doc/
make html latex

# R
echo "R"
cd $basedir/R/
Rscript build_R.R