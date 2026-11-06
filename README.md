# PetterTech blog

This site is built with Hugo and deployed to [pettertech.com/blog](https://pettertech.com/blog/).

## Local development

Use Hugo Extended v0.123.8 (the version used in deployment) and initialize the PaperMod theme submodule:

```powershell
git submodule update --init --recursive
hugo server
```

To generate the production site locally:

```powershell
hugo --minify --baseURL https://pettertech.com/blog/
```

The generated `public/` directory is ignored by git. Pushing to `main` deploys the site through GitHub Actions.