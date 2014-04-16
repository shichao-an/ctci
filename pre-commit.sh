#!/bin/bash


find . -mindepth 2 -path ./.git -prune -o -type f -executable -exec rm {} \;
