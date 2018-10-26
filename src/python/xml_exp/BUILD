# another pattern for adding in a library dependency
python_requirement_library(
  name='libs',
  requirements=[
    python_requirement('lxml'),
  ],
)

python_library(
  name="xml_exp",
  dependencies=[
    ':libs'
  ],
  sources=globs("**/*.py", exclude=[globs("**/*.swp")]),
)

python_binary(
  name="run_main",
  entry_point="xml_exp:main",
  dependencies=[
    ':xml_exp',
  ],
  platforms=['current'],
)

python_app(
  name='xml-app',
  binary=':run_main',
  bundles=[
    bundle(fileset=globs('BUILD')),
  ],
)
