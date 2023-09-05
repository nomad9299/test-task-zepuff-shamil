# test-task-zepuff-shamil
test-task-zepuff-shamil

1) cd into root folder, and run "minikube start"
2) open one more tab in terminal and run "minikube tunnel" to be able to open rabbitmq, required a password from me
3) run "kubectl expose deployment rabbitmq --type=LoadBalancer --port=15672" to run rabbitmq itself
4) you can use "kubectl describe service" to see output
5) "kubectl get pods" to see that is service is working or not,should be in READY 1/1
6) then you can check by typing in browser localhost:15672 to enter the rabbitmq 
