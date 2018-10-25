python_library(
  name="mini",
  dependencies=[
    '3rdparty/python:Flask',
  ],
  sources=globs("**/*.py"),
)

python_binary(
  name="run_server",
  entry_point="lepkg.serve:run_server",
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
