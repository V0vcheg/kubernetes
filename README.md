VLADIMIR KREMNEV - Projet Mircoservices

- Quelques commandes pour tout ajouter à kubernetes

docker build -t user-service:latest .\User-Service\
docker build -t product-service:latest .\Product-Service\
docker build -t order-service:latest .\Order-Service\

kubectl apply -f .\api-key-secret.yaml

kubectl apply -f .\Product-Service\product-deployment.yaml
kubectl apply -f .\Product-Service\product-service.yaml
kubectl apply -f .\Product-Service\product-hpa.yaml

kubectl apply -f .\Order-Service\order-deployment.yaml
kubectl apply -f .\Order-Service\order-service.yaml
kubectl apply -f .\Order-Service\order-hpa.yaml

kubectl apply -f .\User-Service\user-deployment.yaml
kubectl apply -f .\User-Service\user-service.yaml
kubectl apply -f .\User-Service\user-hpa.yaml

- Pour les logs :
  kubectl logs -f <pad> -c "pad_prefix"-log-sidecar
  ex. kubectl logs -f user-deployment-84dc5f8fd4-48rvm user-log-sidecar
