# python-project-template

Low dependency, simple to start template for python3 projects.

[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/lechugaletal/python-project-template/badge)](https://securityscorecards.dev/viewer/?uri=github.com/lechugaletal/python-project-template)

## What's in the bundle?

 * [🗃️] Project directory structure basis for every python3 app:
   * The ``src/config.d`` should contain environment variable config and sensitive data config files.
   * The ``src/models`` shpuld contain any object schema defined for the project.
   * Other project directories considered but maybe less widely used are: ``src/routers`` and ``src/public``. Keep in mind that those can be useful for Flask projects!
 * [🕵️] A ``.gitignore`` file with defaults for python3 tmp files and sensitive data.
 * [📜] The Unilicense as the basis for projects.
 * [⤵️] A ``requirements.txt`` containing project dependencies.
 * [🔧] A ``Makefile`` with a default instruction set.
 * [🛡️] Automated OSSF scorecard vulnerability scanning with GitHub actions.
 * [📄] And last but not least... this README.md


## Maybees...

 * Generate documentation with [MkDocs](https://www.mkdocs.org/). Although it can be useful for most cases, the idea behind this template is to keep python3 dependencies to a minimum.

## About OSSF scorecard

With GitHub actions an automated repo scanning can be configured, currrently this template is configured following OSSF guidelines, using the [following instructions](https://github.com/ossf/scorecard-action#workflow-setup-required). Any repository created from this template will generate a report automatically.

To review the details of the generated report you must first **generate a GitHub token**. 

```bash
docker run -e GITHUB_AUTH_TOKEN=<your_token> gcr.io/openssf/scorecard:latest --show-details --repo=https://github.com/lechugaletal/python-project-template
```
