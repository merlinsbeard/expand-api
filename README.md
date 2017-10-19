# Usage

Copy `local.env` to `prod.env`

Add the details

## Development

```
   $ pip install -r requirements.txt
   $ apistar run
```

Using Gunicorn

```bash
  $ gunicorn app:app --workers=4 --bind=0.0.0.0:5000
```

open in browser

`http://localhost:8080/docs/`

## Production 

Uses Docker for production



```bash
  $ docker build -t expand_api:latest .
  $ docker run --name expand_api \
  > -p 5000:5000 \
  # Using Environment Keys for configurations
  > -e GW2_KEY=MY-LONG_KEY \
  # Using volume for configurations
  > -v prod.env:./prod.env
  > -d expand_api:latest
```

