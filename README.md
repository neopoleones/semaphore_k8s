### semaphore_k8s

There you can take the k8s manifests for deploying ansible semaphore.

All deploy commands are located in taskfile. Before use change nodeAffinity value in pv.yaml and generate your own Secret manifest using `gen_secret.py`.

After deploying, the Ansible Semaphore will be available at address http://node:30030 
