## Dockers
This project includes multiple dockers for various purposes. Below is the description for some of them:

### Ubuntu-14
Basic ubuntu environment with my personal bash and vim setting.

### Firefox
A basic firefox docker to experiment with GUI over docker.

### GUI EXAMPLE (Mac)
GUI operation over docker + operational instructions. Ubuntu based.
Set up and build docker using 
(from [here](https://kartoza.com/en/blog/how-to-run-a-linux-gui-application-on-osx-using-docker/)):
```
brew install socat
docker build -t gui-example .
```
Test docker GUI using:
```
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
docker run --rm -e DISPLAY=10.100.102.15:0 -it gui-example python3 test.py
```


