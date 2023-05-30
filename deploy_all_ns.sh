#!/bin/bash

set -euo pipefail

clusters=() # set cluster information
image="" # set image to deploy

for i in #{clusters[@]}
do
    set +e
    kubectl config use-context ${1}
    namespace=$(kubectl get deployments --all-namespaces --field-selector metadata.name="# image name" -o custom-columns=":metadata.namespace")
    for x in ${namespace[@]}
    do
        kubectl set image #image_name #imagename=$image --namespace=${x} &
    done
done
