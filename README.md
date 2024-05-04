# FastAPI-Vercel

A Hello World FastAPI app that deployed to Vercel using CI/CD.

Warning! According to [Vercel Python Documentation](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python), Vercel only support Python 3.9, Python 3.6 already deprecated. I recommend to use [conda](https://docs.conda.io/en/latest/miniconda.html) or [mamba](https://mamba.readthedocs.io/en/latest/) in order to set Python version in custom environment.

## API Files Structure

All the API codes (routes, models) are in `server` folder. `main.py` is to run FastAPI with uvicorn.

The API files structure as follows.

```powershell
.
│   .gitignore
│   .vercelignore
│   main.py
│   README.md
│   requirements.txt
│   vercel.json
│
├───.github
│   └───workflows
│           preview.yaml
│           production.yaml
│
├───.vercel
│       project.json
│       README.txt
│
└───server
        api.py
        model.py
        routes.py
        __init__.py
```

## Run in Local

The steps to run this API in local are as follows.

1. Create new environment and install requirements.

   ```bash
   conda create -p .conda_env python=3.9 --file requirements.txt
   ```
2. Activate the environment.

   ```bash
   conda activate ./.conda_env
   ```
3. Run the API.

   ```bash
   python main.py
   ```

## Vercel Deployment

The CI/CD deployment steps are as follows.

1. Install Vercel CLI.

   ```bash
   npm i -g vercel
   ```
2. Login Vercel CLI.

   ```bash
   vercel login
   ```
3. Download this code as zip.
4. Create your new repository and git clone your repo.
5. Extract zip to your new repo folder.
6. Open terminal and link repo to Vercel.

   ```bash
   vercel link
   ```
7. Add GitHub repository secrets for GitHub Actions

   | Name              | Description                                                                                                                                  |
   | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
   | VERCEL_TOKEN      | Vercel account token. You can get it by [following](https://vercel.com/guides/how-do-i-use-a-vercel-api-access-token#creating-an-access-token). |
   | VERCEL_ORG_ID     | Vercel Organization ID. You can get it from `.vercel/project.json`.                                                                        |
   | VERCEL_PROJECT_ID | Vercel Project ID. You can get it from `.vercel/project.json`.                                                                            |
8. Commit repo.
9. Add main branch.

   ```bash
   git branch -M main
   ```
10. Push to GitHub.

    ```bash
    git push -u origin main
    ```
11. GitHub Actions will run immediately.
