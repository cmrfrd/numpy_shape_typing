#!/usr/bin/env bash
source $(cd /opt/project/ && poetry env info -p)/bin/activate
exec "$@"
