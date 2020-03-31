#!/bin/bash

DIR=$(dirname $0)

cd $DIR
npm start > server.log 2>&1 &
cd - >/dev/null
