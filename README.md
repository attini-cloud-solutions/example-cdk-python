# Example Attini project with Python CDK

Example project for a CDK project using Attini


## Attini commands
In the below examples we will work with an environment called `dev` and a 
distribution called `example-cdk-python`.


#### Create an Attini environment

```bash
attini environment create dev
```

#### Package

The ``-cb/--container-build ``  flag will do a container build.

The ``-crl/--container-repository-login `` flag will log in to ECR. 

Find the container configuration in attini-setup.yaml. 

```bash
attini deploy run . -e dev -cb -crl
```

#### Deploy

```bash
attini deploy run attini_dist/example-cdk-python.zip -e dev 
```

#### Package and deploy

```bash
attini deploy run . -e dev -cb -crl
```

#### See all your deployments

```bash
attini environment context 
```

#### See all your deployments

```bash
attini deploy history -e dev -n example-cdk-python
```

#### Rollback

```bash
attini deploy rollback -e dev -n example-cdk-python -i {id}
```


## Run tests
```bash
pip install -r requirements-dev.txt
pytest
```
