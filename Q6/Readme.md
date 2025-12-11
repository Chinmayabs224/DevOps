# Kubernetes Deployment Steps

This guide outlines the steps to deploy a Docker image on Kubernetes using a Deployment YAML file and verify that the pod is running.

## Step 1: Create the Deployment Manifest

The deployment configuration is stored in the file below. Open it to modify the image name or other settings if necessary.

**File Location:** [deployment.yaml](./deployment.yaml)

> **Note:** 
> - If you are using a local image with Minikube, make sure to load it into the cluster: `minikube image load student-portal:v1`.
> - If using a remote registry, ensure `YOUR_DOCKER_REGISTRY` in the `deployment.yaml` file is replaced with your actual Docker Hub username or registry URL.

## Step 2: Apply the Deployment

Use `kubectl` to apply the configuration defined in your YAML file to the Kubernetes cluster.

```bash
kubectl apply -f deployment.yaml
```

## Step 3: Verify the Deployment and Pod Status

### 1. Check Deployment Status
Verify that the deployment was created successfully and the pods are available.

```bash
kubectl get deployments
```

**Expected Output:**
```text
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
student-portal-deploy   1/1     1            1           10s
```

### 2. Check Pod Status
Verify that the specific pods managed by the deployment are running.

```bash
kubectl get pods -l app=student-portal
```

**Expected Output:**
```text
NAME                                     READY   STATUS    RESTARTS   AGE
student-portal-deploy-66b8c6f5f9-abcde   1/1     Running   0          20s
```

### 3. Check Application Logs
To ensure the application inside the container started correctly (e.g., Flask server running), check the logs of the pod.

```bash
kubectl logs <pod-name>
```
*(Replace `<pod-name>` with the actual name from the previous command)*

**Expected Result:** You should see startup logs like `Running on http://0.0.0.0:5000/`.
