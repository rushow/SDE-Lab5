!For reproduce the project, follow this instruction:
This project runs in Azure Function V4: which General Available for Python 3.9-3.8, my PC using 3.8.10
The full document here: https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python
Just have to read environment configuration:
- Core Tools: Download Core Tools v4: https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash%2Ckeda#install-the-azure-functions-core-tools
- In visual code, install Azure Function Extensions https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions, also Python Extension https://marketplace.visualstudio.com/items?itemName=ms-python.python if you don't have
- https://docs.python.org/3/library/venv.html
On the root folder /AzureFunctions/ -> create .venv environment folder (command python -m venv .venv) in order to use
Select interprecter there .venv environment
Press F5 to run
- If it required Azure Web Job Storage to run, just install this: https://go.microsoft.com/fwlink/?linkid=717179&clcid=0x409

!For testing api without install above environments: Get the docker from here: docker pull zhenyuan0502/azurefunctionimage:1.0
Public repository here https://hub.docker.com/repository/docker/zhenyuan0502/azurefunctionimage
Then run: docker run -p 8080:80 -it zhenyuan0502/azurefunctionimage:1.0
Simple test to make sure it works
- Command: docker pull zhenyuan0502/azurefunctionimage:1.0
- Command: docker run -p 8080:80 -it zhenyuan0502/azurefunctionimage:1.0
- Postman: http://localhost:8080/api/Reddit/search-reddit?trends=stress


When it run successfully will be likely below text
###########
Found Python version 3.8.10 (py).

Azure Functions Core Tools
Core Tools Version:       4.0.3971 Commit hash: d0775d487c93ebd49e9c1166d5c3c01f3c76eaaf  (64-bit)
Function Runtime Version: 4.0.1.16815


Functions:

        Linkedin: [GET,POST] http://localhost:7071/api/Linkedin

        Reddit: [GET,POST] http://localhost:7071/api/Reddit

        Twitter: [GET,POST] http://localhost:7071/api/Twitter


!Development note:
docker pull zhenyuan0502/azurefunctionsimage:1.0
docker build -t zhenyuan0502/azurefunctionimage:1.0 .
docker push zhenyuan0502/azurefunctionimage:1.0
docker run -p 8080:80 -it zhenyuan0502/azurefunctionimage:1.0
