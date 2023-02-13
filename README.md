# Cobra Test

Proof of concept with CobraPY
- https://cobrapy.readthedocs.io/en/latest/
- https://github.com/opencobra/cobrapy/blob/devel/INSTALL.rst

## Docker
Build a container to manage dependencies and simplify the running process

### create dockerfile
A preconfigured dockerfile is provided. Here's a rundown of what we're doing in the Dockerfile.

- We're going to build a base python image. May consider changing this to a Conda Image in the future depending on future requirements
> FROM python:latest

- Add our working files to the container image
> ADD . .

- Install the dependencies in requirements.txt
> RUN pip install --no-cache-dir -r requirements.txt

- Our entry point should be the main.py script. Arguments will be passed to this file.
- Think of main.py as a "controller". It will dictate which functions / scripts to run based on the parameters you pass it.
> ENTRYPOINT ["python","src/main.py"]

### build image
This builds the docker image. The image is a ready-to-use template that's built from the "recipe" in the "Dockerfile"
> docker build . --tag cobra
- This docker image should be rebuilt whenever scripts or required packages change.

### run image
Once you have a working image, every time you need to run a cobra based script, run this image
> docker run -rm cobra commandName [arg1 [arg2 [arg3]]]

# Current Command List
- Check Python Version
> docker run -rm cobra

- Check Cobra Version
> docker run -rm cobra cobra_version