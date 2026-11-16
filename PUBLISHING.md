# Publishing to your GitHub account

The GitHub-ready source files are already in this directory. No application build, Node.js, or Python package installation is needed.

**Intended repository:** `aditti30-prog/payments-pm-handbook`

## Option A — Upload through GitHub's website

1. Sign into the GitHub account `aditti30-prog`.
2. Create a **new public repository** named `payments-pm-handbook` at https://github.com/new .
3. Create it **without** GitHub's generated README, license, or `.gitignore`, because this package already has those files.
4. Open the empty repository and follow GitHub's **uploading an existing file** flow. Upload the contents of this directory (preserving its folder structure), or use the command-line method below.
5. Verify the Markdown chapter links render, and inspect the Mermaid diagrams on GitHub.

## Option B — Publish from a terminal

Once the empty repository exists, run these commands from the **extracted `payments-pm-handbook` folder**:

```bash
git init
git branch -M main
git add .
git commit -m "Draft textbook release: Payments PM Handbook v0.2"
git remote add origin https://github.com/aditti30-prog/payments-pm-handbook.git
git push -u origin main
```

You must have GitHub authentication configured on your computer. Avoid putting personal access tokens in command history or repository files.

## Verify before publishing

```bash
python3 scripts/verify_case.py
python3 scripts/check_internal_links.py
```

**License note:** Original handbook material is presently designated CC BY 4.0 in `LICENSE.md`. Review that choice before making the repository public if you would prefer a different content license.

## Next improvement after v0.2

Invite payments specialists to review the 3DS, tokenization, disputes and reconciliation deep dives. Part V is still planned and not written. This draft does not claim outside peer review, complete jurisdiction coverage, or any security certification.
