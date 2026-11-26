# GROWL Catalog

A standardized catalog of compact-binary population simulations from the literature. Each entry
records how to obtain a simulation's data, which code produced it, and every physics assumption
behind it, with a pointer to where that assumption is stated in the paper.

Built by the Gravitational Wave Paleontology Lab (GROWL) at UC San Diego, together with the
GROWL Task Force.

## Layout

```
.github/
  workflows/
    git-hooks.yml             runs prek checks on pushes and pull requests
.pre-commit-config.yml        git pre-commit hooks, optimized for prek.
GROWL_TF_individual_data_projects/
  README.md                   how to contribute: start here
  instructions_task_force/    instruction notebooks (one per step) and templates
  individual_project_folders/
    <dataset>/                one folder per dataset, e.g. vanson-2022-nopeaks
      README.md               notes and results for this dataset
      metadata.csv            the dataset's metadata, checked against the paper
```

Dataset names are lowercase, `<first author>-<year>-<short tag>`. Simulation data is never stored
in this repository.

## Contributing

Contributors are members of the GROWL Task Force. They have completed the GW Paleontology
Bootcamp and were then assigned an individual project: a published dataset that they bring into
the catalog. Each contributor has either completed this process or is actively working through it.

GROWL Task Force members: see
[GROWL_TF_individual_data_projects/README.md](GROWL_TF_individual_data_projects/README.md).

Shared analysis code lives in [growl-tools](https://github.com/growl-lab/growl-tools).

## Citing

Citation information will be added with the first Zenodo release.
