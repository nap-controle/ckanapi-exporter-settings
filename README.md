# ckanapi-exporter-settings

A repo to organize exports from transportdata.be and check the data.

To run for transportdata.be:   

`python export.py > export.csv`

To run some basic checks:

`python check.py export.csv export-checked.csv`

## Common actions op API

Get all orgs: [https://www.transportdata.be/api/3/action/organization_list](https://www.transportdata.be/api/3/action/organization_list).  
Get on org: [https://www.transportdata.be/api/3/action/organization_show?id=parking-brussels](https://www.transportdata.be/api/3/action/organization_show?id=parking-brussels). 
