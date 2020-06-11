# rmi
docker rmi discoroveryx/mylab:alpine
docker image prune

# build
docker build -t discoroveryx/mylab:alpine .

# run and configure
docker run --rm -it discoroveryx/mylab:alpine

# push to hub
docker push discoroveryx/mylab:alpine
