# Usage

Copy `local.env` to `prod.env`

Add the details

## Development

```
   $ pip install -r requirements.txt
   $ apistar run
```

open in browser

`http://localhost:8080/docs/`

## Production

```bash
$ gunicorn app:app.wsgi --workers=4 --bind=0.0.0.0:5000
```

Open in Browser

`http://localhost:5000/docs`
