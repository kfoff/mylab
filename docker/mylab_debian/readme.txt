# rmi
docker rmi discoroveryx/mylab:debian
docker image prune

# build
docker build -t discoroveryx/mylab:debian .

# run and configure
docker run --rm -it discoroveryx/mylab:debian

# push to hub
docker push discoroveryx/mylab:debian
