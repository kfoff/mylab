# rmi
docker rmi discoroveryx/mylab:alpine_noenv
docker image prune

# build
docker build -t discoroveryx/mylab:alpine_noenv .

# run and configure
docker run --rm -it discoroveryx/mylab:alpine_noenv

# push to hub
docker push discoroveryx/mylab:alpine_noenv
