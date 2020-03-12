# {APPLICATION}

## Instruction to deploy to OCP 4.3 using tekton pipeline
1. git clone {THIS_GIT_REPO}
2. loging to OCP cluster with default project namespace.
   ```
   sample commads
   ```
3. create Tekton pipeline and resources for this application
   ```
   oc create -f pipeline/tekton/pipeline.yaml
   oc create -f pipeline/tekton/resources.yaml
   ```
   
   **note:** Update the {image.url} in resources.yaml file if you want to deploy the application in your own project
   namespace (e.g. *myproject*).  
   ```
     params:
       - name: url
         value: image-registry.openshift-image-registry.svc:5000/myproject/application:latest
   ```
4. start the pipeline
   ```
   tkn pipeline start build-and-deploy
   ```
5. find your application url 
   ....

## using the OCP / Tekton console.
   ...

Development todo tasks:
- update server_config.py for db driver classpath 
- update resource.yaml for git repo
