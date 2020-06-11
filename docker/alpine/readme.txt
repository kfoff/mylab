# rmi
docker image prune
docker rmi discoroveryx/alpine

# build
docker build -t discoroveryx/alpine .

# run and configure
docker run --rm -it discoroveryx/alpine

# push to hub
docker push discoroveryx/alpine
