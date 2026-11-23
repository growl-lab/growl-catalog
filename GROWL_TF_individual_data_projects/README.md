# GROWL Task Force: individual data projects

Each GROWL Task Force member works on **one published population-synthesis dataset**. Every
dataset has **one folder** here. If several people work on the same dataset, they share that
folder and split the deliverables between them. You share your work by opening a
**pull request (PR)**; a GROWL mentor reviews it and merges it into the repository.

## Stay in touch: hands-on sessions and Discord

**Please use the hands-on sessions!** They are the best place to:

- **check in on the results you found**, even small or half-finished ones;
- **show examples**: a plot, a strange column in the data file, a table you filled in;
- **discuss the science** of your paper and your dataset with the rest of the task force.

Don't wait until a step is "done" to show it. Intermediate results are exactly what we want to see,
and nobody has looked at most of these datasets this way before, so what you find is new.

**Post on Discord** (your dataset channel, or the shared "individual projects" channel):

- **any questions**, about the data, the paper, the physics, git, anything. If you're stuck for
  more than a short while, ask. Someone else probably has the same question.
- **cool updates**: plots, surprises, things that match (or don't match) the paper. Everyone
  would love to see them.

GitHub is for submitting your work; Discord and the hands-on sessions are for talking about it.
Please don't use GitHub issues for questions.

```
GROWL_TF_individual_data_projects/
├── README.md                          <- this file
├── instructions_task_force/           <- instruction notebooks, one per step (read only, don't edit)
│   └── step1_download_and_investigate_data.ipynb
└── individual_project_folders/
    └── <dataset>/                     <- one folder per DATASET, e.g. broekgaarden-2022-dcorates
        ├── README.md                  <- shared notes: the main file of the project
        ├── step1_<YourName>.ipynb     <- each person's own copy of the instructions
        ├── download_instructions.md   <- deliverable of step 1 (Task C)
        ├── metadata.csv               <- deliverable of step 1 (Task E)
        └── figures/                   <- optional: small PNGs you refer to in README.md
```

## Dataset names

The folder name is the **dataset name** used everywhere in GROWL (folders on the data server,
this repository, the catalog). It is all lowercase:

```
<first author>-<4-digit year>-<short tag>        e.g. vanson-2022-nopeaks, riley-2021-che
```

Only letters, digits and hyphens. For a new dataset you **propose** the name (and the submodel
folder names) in your checklist issue, and a mentor **confirms** it before you create any folders.

## Working together on one dataset

- Each deliverable has **one owner**: the checklist issue for your dataset says who does what.
  Only edit files you own, so you don't overwrite each other's work (or get merge conflicts).
- Everyone writes in the shared `README.md`. Start your entries with your name and the date, e.g.
  `### 2026-11-20 (Joseph)`.
- Everyone keeps their own notebook, `step1_<YourName>.ipynb`.

---

## The three rules

1. **Only change files inside your dataset's folder.** If you think something outside it should
   change (an instruction notebook, this README), ask on Discord.
2. **Never upload data.** No `.h5` / `.hdf5` files, no `.zip` / `.tar.gz` archives, no large
   tables. The data stays on your own machine (later: the GROWL server); your notebook points at
   it through the `PATH` dictionary from Task B. An automatic check rejects data files and any file
   larger than 10 MB.
3. **Every change goes through a pull request.** Nobody pushes directly to `main`. That is not
   because we don't trust you: it gives a mentor a chance to see your work and comment on it.

---

## What goes in your folder

| File | What it is | When |
|---|---|---|
| `README.md` | **Shared notes.** This is the main file of the project. Write down what you did, what you found, what was unclear, and questions for the team. Keep adding to it, with your name and the date on each entry (`### 2026-11-20 (Joseph)`). | Always |
| `step1_<YourName>.ipynb` | Your copy of the instruction notebook, with the tasks filled in. | Step 1 |
| `download_instructions.md` | The exact recipe to download the data (Task C): links, the commands you typed, difficulties. Someone else must be able to follow it literally. Written in Markdown, so commands go in code blocks and the difficulties in a table. | Step 1 |
| `metadata.csv` | The metadata table (Task E), **checked by a person against the paper**. See below. | Step 1 |
| `figures/*.png` | Small plots you want to show in your `README.md`. | Optional |

More deliverables will be added as the next steps are released.

### `metadata.csv`

> 🚧 **Draft.** The columns will change soon: we are aligning this file with the GROWL metadata
> table that Julia is building (an older version is at
> [julia-haynes.github.io/Popsynth-Metadata-LLM-Table](https://julia-haynes.github.io/Popsynth-Metadata-LLM-Table/);
> ping Julia on Discord for the current interactive version). Your folder will then get a
> `metadata.csv` with the values already filled in by an AI model, for you to check.

Until then, start from
[`instructions_task_force/metadata_template.csv`](instructions_task_force/metadata_template.csv):
one row per parameter (and per submodel, if the value differs between submodels). The columns
that matter most:

| Column | What to write |
|---|---|
| `source_in_paper` | **Where** the value is stated: section, table, equation or figure. No source, no value. |
| `status` | `llm` (not checked yet), `verified` (checked, correct) or `corrected` (checked, was wrong) |
| `verified_by` | Your name |

**Notebooks:** before committing, make sure your notebook isn't huge (a few MB at most). If it has
many large plots, clear those outputs (*Edit → Clear Outputs of All Cells* in Jupyter, or for one cell)
and save the plots you want to keep as PNGs in `figures/`.

---

## How to submit your work

You have write access to this repository, so you can make a **branch**, push it, and open a pull
request. Choose whichever route you're comfortable with.

### Route A: in the browser (no git needed)

1. Go to your folder on GitHub:
   `https://github.com/growl-lab/growl-catalog/tree/main/GROWL_TF_individual_data_projects/individual_project_folders/<dataset>/`
2. **To upload files:** click **Add file → Upload files**, drag your files in.
   **To edit your README:** open `README.md`, click the pencil icon.
3. At the bottom, choose **"Create a new branch for this commit and start a pull request"**. Give
   the branch a name like `Joseph/step1-download`, then click **Propose changes**.
4. On the next page, write a short description and click **Create pull request**.

### Route B: on the command line

One-time setup:

```bash
git clone https://github.com/growl-lab/growl-catalog.git
cd growl-catalog
```

Each time you want to submit something:

```bash
git switch main
git pull                                      # get everyone else's latest work
git switch -c <YourName>/<what>               # e.g. Joseph/step1-download
# ... work in your folder ...
git add GROWL_TF_individual_data_projects/individual_project_folders/<dataset>
git status                                    # check: only your folder, no data files
git commit -m "<dataset>: <what you did>"
git push -u origin <YourName>/<what>
```

Then open the link that `git push` prints (or go to the repository page and click **Compare & pull
request**), write a short description, and click **Create pull request**.

### After you open the pull request

- The automatic checks run (you'll see a green ✓ or a red ✗). If one fails, the details tell you
  why; usually it is a file that is too large or a data file.
- A GROWL mentor reviews it. They may approve it straight away or leave comments.
- To respond to comments, **keep working on the same branch** and push again (or, in the browser,
  edit the file on that branch). The pull request updates automatically.
- Once approved, a mentor merges it. Then start your next piece of work from a fresh `main`
  (`git switch main && git pull`).

**Small and often beats big and rare.** Open a pull request after each task or two; don't wait
until the whole step is done. We'd love to see intermediate results.

---

## Need help?

- Git or GitHub problems: ask on Discord, and paste the error message.
- Stuck on a task, or found something odd in the data: write it in your `README.md` and ask on
  Discord. "This isn't in the file" or "the paper doesn't say" is a useful result.
