# Contributing to the GROWL Catalog

You will own one catalog entry (one simulation or paper). A maintainer opens a **parent issue** for your entry with **sub-issues** for each task (data download, parameters, ...). You work through the tasks one pull request at a time.

Questions go to the GW Paleontology Discord, not to GitHub issues.

## One-time setup

```bash
git clone https://github.com/growl-lab/growl-catalog.git
cd growl-catalog
pip install pyyaml jsonschema
```

## Starting your entry

1. Find your parent issue (assigned to you) and note your catalog id, e.g. `smith-2024-bns-delays`.
2. Create a branch and copy the template:
   ```bash
   git switch -c smith-2024-bns-delays/setup
   cp -r simulations/_template simulations/smith-2024-bns-delays
   ```
3. Set `id`, `title`, `contributors`, and the `paper` section in `metadata.yaml`. Commit, push, open a pull request.

## Working on a task

One branch and one pull request per task:

```bash
git switch main && git pull
git switch -c smith-2024-bns-delays/data
# edit simulations/smith-2024-bns-delays/metadata.yaml
python scripts/validate_metadata.py smith-2024-bns-delays
git add simulations/smith-2024-bns-delays
git commit -m "Add data section for smith-2024-bns-delays"
git push -u origin smith-2024-bns-delays/data
```

Then open a pull request, write `Closes #<task issue number>` in the description, and fill in the checklist.

## Rules of thumb

- Only edit files inside your own `simulations/<id>/` folder. Changes to the schema or templates go through a separate issue.
- Every parameter needs `source_in_paper`. If the paper is silent and you used a code default, write that.
- Test download steps yourself before recording them.
- If something is unclear, write it in the README "Open questions" section and keep going. Unclear is useful information.
- The automatic check must pass before a maintainer reviews. Run the validator locally first.

## Review

A maintainer reviews every pull request. Expect comments; addressing them by pushing more commits to the same branch is normal. Once approved, the maintainer merges.
