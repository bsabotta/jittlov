#!/bin/bash

cd [filePath]

source $"[filePath]/[apiName]_venv/bin/activate"

export FLASK_APP=[apiName]
export FLASK_ENV="development"

flask run -h [apiBroadcastIp] -p [apiBroadcastPort]

