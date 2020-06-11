# rmi
docker rmi discoroveryx/mylab:ubuntu
docker image prune

# build
docker build -t discoroveryx/mylab:ubuntu .

# run and configure
docker run --rm -it discoroveryx/mylab:ubuntu

# push to hub
docker push discoroveryx/mylab:ubuntu
