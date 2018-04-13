## Locust on Cloud Foundry 
This is a small locust demo app running on Cloud foundry


### Pre requests
- Python 2.7 or later
- pyquery; `pip3 install pyquery`
- locustio; `brew install locustio`


### How to run locally
run locust --host=[locust documentation url]
`locust --host=https://docs.locust.io/`


### How to run on CF
run `cf push pt-test` and python_buildpack will run locust using the host inside [Procfile](Procfile) 
