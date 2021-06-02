# only if not using docker compose

sudo docker build -t foo/foobar-foo:latest foo/
sudo docker build -t foo/foobar-bar:latest bar/

sudo docker run -d --net host foobar-foo:latest
sudo docker run -d --net host foobar-bar:latest