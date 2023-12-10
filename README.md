# k8s-dl-workflow
Running training and inference on kubernetes clusters

To build and push the container images

`docker build --platform linux/amd64 -t train-image -f Dockerfile-train .`
`docker tag train-image lvb243/cml:train-image`
`docker push lvb243/cml:train-image`

`docker build --platform linux/amd64 -t inference-image -f Dockerfile-inference .`
`docker tag inference-image lvb243/cml:inference-image`
`docker push lvb243/cml:inference-image`

After creating the cluster, to deploy the training and then inference apps from the gke cluster shell:
`kubectl create -f pvc.yaml`
`kubectl create -f train.yaml`
`kubectl create -f service.yaml`
`kubectl create -f inference.yaml`