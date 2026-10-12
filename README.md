# GROWL Catalog

A standardized, public catalog of compact-binary population simulations from the literature. Each entry records how to obtain a simulation's data, which code produced it, and every physics assumption behind it, with a pointer to where that assumption is stated in the paper.

Built by the Gravitational Wave Paleontology Lab (GROWL) at UC San Diego.

## Layout

```
simulations/
  _template/            copy this to start a new entry
  <id>/
    metadata.yaml       machine-readable entry (validated automatically)
    README.md           short human-readable summary
schema/                 JSON Schema every metadata.yaml must satisfy
scripts/                validation and helper scripts
```

## Contributing

Contributors are lab members who have completed the GW Paleontology Bootcamp. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citing

Citation information will be added with the first Zenodo release.
