# actually not a library but rather the real application
python_library(
  name="mini",
  dependencies=[
    '3rdparty/python:Flask',
  ],
  sources=globs("**/*.py", "static/*", "templates/*.html", exclude=[globs("**/*.swp")]),
)

# "production" server using gunicorn
python_binary(
  name="run_server",
  entry_point="webapp.serve:run_server",
  dependencies=[
    '3rdparty/python:gunicorn',
    ':mini',
  ],
  platforms=['current'],
)

python_app(
  name='hello-app',
  binary=':run_server',
  bundles=[
    bundle(fileset=globs('BUILD')),
  ],
)
