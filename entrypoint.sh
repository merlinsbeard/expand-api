#!/bin/bash
exec gunicorn app:app \
    --bind 0.0.0.0:5000 \
    --name expand_api \
    --workers 2 \
    --log-level=info \
    --access-logfile -
"$@"
