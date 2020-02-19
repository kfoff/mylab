# build
docker build -t discoroveryx/debian .

# run and configure
docker run --rm -it discoroveryx/debian

# push to hub
docker push discoroveryx/debian
