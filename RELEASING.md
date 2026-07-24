# Making a new release

This describes how to release a new version of `sphinx-ymmsl` to PyPI.

1. Go to the [GitHub page of sphinx-ymmsl](https://github.com/multiscale/sphinx-ymmsl).
2. Check the [open pull requests](https://github.com/multiscale/sphinx-ymmsl/pulls). Merge (or
   postpone) anything that should (or should not) be part of the new release before continuing.
3. In the right sidebar, click **Releases**, then **Draft a new release**.
4. Under **Choose a tag**, create a new tag for the release. Tags follow
   [semantic versioning](https://semver.org/) and are prefixed with `v`, e.g. `v0.3.0`
   (see the existing tags for examples). The version number on PyPI is derived from this tag
   via `setuptools_scm`, so no version needs to be bumped in the code itself.
5. Set the release title to the same value as the tag (e.g. `v0.3.0`).
6. Click **Generate release notes**. This creates a changelog from the merged PRs since the
   last release. Edit the generated text down to what matters to a *user* of the package.
7. Make sure **Set as the latest release** is checked.
8. Click **Save draft** (do not publish yet). The draft is now visible to others on the
   [Releases page](https://github.com/multiscale/sphinx-ymmsl/releases), marked as `Draft`.
9. Ask someone else to review the draft release notes.
10. Once reviewed, click **Publish release**.

Publishing the release pushes the new tag, which triggers the `publish-to-pypi` GitHub Actions
workflow (see [`.github/workflows/publish-to-pypi.yml`](.github/workflows/publish-to-pypi.yml)).
This builds the package and publishes it to PyPI using trusted publishing, there is nothing
else to do manually. You can follow along under the repository's
[Actions tab](https://github.com/multiscale/sphinx-ymmsl/actions) to confirm the publish
succeeded, and check [pypi.org/project/sphinx-ymmsl](https://pypi.org/project/sphinx-ymmsl/) and
`stable` on [Read the Docs](https://sphinx-ymmsl.readthedocs.io/en/stable/) to confirm the new
version is listed and built there before considering the release done.
