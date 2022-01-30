docker build ./wave --tag wghilliard/waved:latest --platform linux/amd64 -f ./wave/Dockerfile.waved

docker build ./wave --tag wghilliard/ner-wave-app:latest --platform linux/amd64 -f ./wave/Dockerfile.ner-wave-app

docker build ./ner --tag wghilliard/ner:latest --platform linux/amd64 -f ./ner/Dockerfile