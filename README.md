# DevSecOps Demo



Testing app locally 

```shell
python -m venv venv   # optional but recommended
source venv/bin/activate
pip install -r requirements.txt
```

E.g. Running inside Github Codespace

```shell
(venv) @iamgini ➜ /workspaces/devsecops-demo (main) $python app.py

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.11.133:5000
Press CTRL+C to quit
```

Review the app in Codespaces

- In the top bar, click “Ports” (or find the forwarded ports panel).
- Codespaces automatically detects port 5000.
- Click “Open in Browser” or “Preview in Browser.”

## GitHub Action

Secrets:

- Add QUAY_USERNAME and QUAY_PASSWORD in your repo settings → Secrets → Actions.
- Use your Quay robot account token if possible; easier than your personal password.


## Test it in Kubernetes

```shell
kubectl apply -f deployment.yaml

SHA=$(git rev-parse HEAD)
kubectl set image deployment/flask-demo \
  flask-demo=quay.io/iamgini/flask-devsecops-demo:$SHA
kubectl rollout status deployment/flask-demo

kubectl port-forward svc/flask-demo-service 8080:5000

```

## Change app

For testing app changes

```shell
# blue
echo "v0.0.2" > VERSION.txt


```