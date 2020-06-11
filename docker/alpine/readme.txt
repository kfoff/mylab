# rmi
docker rmi discoroveryx/alpine
docker image prune

# build
docker build -t discoroveryx/alpine .

# run and configure
docker run --rm -it discoroveryx/alpine

# push to hub
docker push discoroveryx/alpine
