# Contributing to Tickmark

Thank you for helping. Questions and ideas go to
[GitHub Discussions](https://github.com/tickmark-app/tickmark/discussions);
issues are for bugs and planned work.

## Set up

You need [uv](https://docs.astral.sh/uv/). It installs the right Python version
and all tools.

```sh
git clone https://github.com/tickmark-app/tickmark
cd tickmark
uv sync
uv run pre-commit install
uv run tickmark
```

## Before you open a pull request

```sh
uv run pre-commit run --all-files   # format, lint, types, layer rules
uv run pytest --cov                 # tests
```

- One topic per pull request, ideally under 400 changed lines.
- Write commit messages as [Conventional Commits](https://www.conventionalcommits.org/):
  `feat: add spacing mode`, `fix: keep vertical ruler readable at 200 %`.
- Add tests for new behaviour; a bug fix starts with a test that shows the bug.
- Put user-visible text through `self.tr()` so it can be translated.
- Say in the pull request what you tested and on which systems.

The rules in [CLAUDE.md](CLAUDE.md) apply to every contributor, human or not.

## Sign your work (DCO)

Tickmark uses the [Developer Certificate of Origin](https://developercertificate.org/).
By adding a `Signed-off-by` line you confirm that you have the right to submit
the change under the project's licence:

```sh
git commit -s -m "fix: ..."
```

Use your GitHub noreply address if you do not want your email in the history.

## AI-assisted contributions

They are welcome. Mark them in the pull request, and make sure you understand
and have tested every line you submit. You are responsible for it, not the tool.

## Translations

Translations will be handled through Weblate once the pipeline is in place.
Until then, open an issue if you would like to translate Tickmark.
