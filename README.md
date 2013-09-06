Ororo-pp
========

Ororo is a very small Python script that merges a JSON based
CloudFormation template, with optional Jinja2 templating, some general
configuration settings (in yaml) and a yaml file of what becomes your
CloudFormation templates mapping section.

    ./bin/ororo --config-file ./config.yaml --template-file ./templates/webapp.json --mapping-file ./mappings/dev-eu.yaml

We currently have a number of CloudFormation templates defined that are each used multiple times, in dev, staging and production across multiple regions

We currently use the general config file to declare common settings such as which instance types we use, the number of AZs to build the application in and similar. These are the big, general settings.

The mapping files are broken down per region / environment combination. We set the subnets, AMIs etc. in these.
