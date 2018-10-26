Inspired by [Stephan Erb's talk about pants &
pex](https://de.pycon.org/schedule/talks/python-with-and-without-pants/) at
PyCon DE 2018 I put together an example for bundling a Python web application
into a pex-file using pants.

Links:

- [Stephan's example code](https://github.com/StephanErb/pexample)
- TODO: Video link


# How to run & build

Bundle the app into a pex file: 

```bash
./pants bundle src/python/webapp/:hello-app
```

This creates a pex file in the `dist/` directory which should be runnable
on any linux system with only Python 3.6 installed:

```bash
python3 dist/run_server.pex
```

Just to demonstrate that you can run it without installing dependencies, let's
run it inside a docker container now. (It is ironic to use docker for the demo
because I actually looked into bundling an app with pex because I don't like
the docker-based deployment I have in a project.)

```bash
$ docker run -ti -p 8080:8080 -v `pwd`/dist:/dist python:3.6.7-alpine3.7 python /dist/run_server.pex
[2018-10-26 09:38:56 +0000] [1] [INFO] Starting gunicorn 19.9.0
[2018-10-26 09:38:56 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
[2018-10-26 09:38:56 +0000] [1] [INFO] Using worker: sync
[2018-10-26 09:38:56 +0000] [14] [INFO] Booting worker with pid: 14
[2018-10-26 09:38:56 +0000] [15] [INFO] Booting worker with pid: 15
[2018-10-26 09:38:56 +0000] [16] [INFO] Booting worker with pid: 16
[2018-10-26 09:38:56 +0000] [17] [INFO] Booting worker with pid: 17
[2018-10-26 09:38:56 +0000] [18] [INFO] Booting worker with pid: 18
[2018-10-26 09:38:56 +0000] [19] [INFO] Booting worker with pid: 19
[2018-10-26 09:38:56 +0000] [20] [INFO] Booting worker with pid: 20
[2018-10-26 09:38:56 +0000] [21] [INFO] Booting worker with pid: 21
[2018-10-26 09:38:56 +0000] [22] [INFO] Booting worker with pid: 22
[2018-10-26 09:39:00 +0000] [1] [INFO] Handling signal: winch
```

# Solved Problems
I am not an expert on this, but from what I read and heard, these things
seem to be solved with the pants/pex approach

- Pure-python Libraries
- Libraries with C extensions that have a wheel on PyPI work

# Remaining Problems

- Libraries with dependencies on system libraries (those will need to be
  installed separately on the target system)
- Windows?! If your usecase is distributing a client application, Windows might
  be a target platform.
