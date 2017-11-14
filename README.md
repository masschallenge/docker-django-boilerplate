_MIT License_
_Copyright (c) 2017 MassChallenge, Inc._

# Accelerator Directory Server

<a href="https://codeclimate.com/github/masschallenge/accelerator-directory/maintainability">
  <img src="https://api.codeclimate.com/v1/badges/919b52c7bf78bfc67bb6/maintainability" />
</a>

## Quickstart

1. Install [Docker](https://docs.docker.com/engine/installation/#supported-platforms)
(download the stable channel).

2. Start Docker.


3. Install impact-api and spin up a dev server. 
The accelerator-directory code is currently designed to 
work with an instance of the MassChallenge's impact-api, and relevant 
depenedencies. Make sure to install it and run it by following the steps 
described [here](https://github.com/masschallenge/impact-api/blob/development/QUICK_START.md).

4. Get the source code for accelerator-directory.  
If you already have accelerator-directory checked out, then in a Terminal 
window go to that directory and bring it up to date
with:
```
cd <accelerator-directory>
git checkout development
git pull
```
If you don't have accelerator-directory checked out, but you do have the
impact-api code base checked out, check out the accelerator-directory code
next to the impact-api directory with:
```
cd <impact-api-directory>/..
git clone https://github.com/masschallenge/accelerator-directory.git
cd accelerator-directory
```

5. Configure the docker-compose with a .env file. Do this by copying 
`.env.template` as `.env`, and set configurations for this project. 
Ports set must not be already used on your localhost. The configuration is
valid if running `docker-compose config` prints a valid docker-compose file.

Also, make sure the following are configured manually:
- redis port is configured correctly in the `DJANGO_HIREDIS_CACHE_LOCATION` 
variable in _.dev.env_.
- localhost port is configured correctly in the `proxy_pass` variable in 
_web/nginx/nginx.conf_.
- localhost port is configured correctly in _web/scripts/start-nodaemon.sh_.
- localhost port is configured correctly in _supervisord.conf_.


6. Run tests.  From the accelerator-directory source directory run:
```
make build
make test
```

This will take a while, but all tests should pass.  Specifically the
end of the output should look something like:

```
Ran 102 tests in 14.845s

OK
Destroying test database for alias 'default'...
```

6. Start server

```
make dev
```

Once the process completes (it will take a little while and the last
line should say "BUILD COMPLETE"), visit http://localhost:8001 in a
browser to see the login screen (or the custom port you configured).


7. Go to http://localhost:8001. You should be able to use a simple search
interface, aimed at the local dev impact-api server you created earlier.

## Commands
See [impact-api's readme](https://github.com/masschallenge/impact-api#commands)

## Using Makefile Commands
See [impact-api's readme](https://github.com/masschallenge/impact-api#using-makefile-commands)