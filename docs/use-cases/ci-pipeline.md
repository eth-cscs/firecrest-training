# CI/CD Pipeline with FirecREST

## Goal

Create a CI/CD pipeline that runs tests on Daint via FirecREST.
The repository already contains the code to be tested and the pipeline is mostly configured -- you only need to fill in the parts that submit the job to the supercomputer and process the results.

## Prerequisites

- **Basic Python and Git knowledge**: the task involves straightforward Python; experience with another language is sufficient.
- **CSCS user account**: the pipeline is pre-configured for Piz Daint but requires minimal changes for a different machine.
- **GitHub account**: the CI uses GitHub Actions from your account.
- **Basic CI/CD understanding**: familiarity with continuous integration and deployment concepts is recommended.

## Getting Started

1. [Setup your API keys](../setup.md#get-your-api-keys), if you haven't already.

2. Fork and clone the repository

    [Fork the repository into your GitHub account](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) by clicking on the **Fork** button in the top of the browser.

    Then, clone in your local workstation the git repository:

    ```bash
    $ git clone https://github.com/<your-username>/<your-repository>.git
    $ cd <your-repository>
    ```

    Replace `your-username` and `your-repository` with your GitHub username and the name of the repository you forked.

    !!! tip 
        The workflows will be disabled by default in your repository, so go ahead and enable them in the "Actions" tab of your repository.

## Exercise

1. **Inspect the code that will be tested:**
    Take a moment to review the code in the `mylib` folder. This is the code that will be tested in the CI/CD pipeline.

    Right now there is nothing meaningful there, but you should add your own tests.

2. **Configure CI/CD Pipeline:**
    - Open the CI configuration file (`.github/workflows/ci.yml`) and, with the help of the comments, try to understand the different steps that are already configured.
    - Find out the *secrets* and *variables* that are used in the pipeline and try to figure out how to set them up in your account. Follow this official GitHub [document](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) for more help.
    - You will need to make changes in the file `.ci/ci_script.py`.
    Remove the premature exit line (this will make the CI fail) and try to fix the script by following the instructions of the commented sections.

    !!! tip
        You can use PyFirecREST to try to solve the problem or direct requests to the API.

3. **Review Results:**
    Once you've configured the pipeline, commit your changes and push them to your GitHub repository.

    Click on **Actions**, select **CI** and execute the workflow by selecting **Run workflow** in the right of the screen and clicking on **Use workflow from: main** option.

    !!! tip
        If you want the CI is triggered on push to `main` branch, you can uncomment the following lines in the `.github/workflows/ci.yml` file
        ```yml
        #   push:
        #     branches: [ "main" ]
        #   pull_request:
        #     branches: [ "main" ]
        ```

4. **[Optional] Apply this to your own codes:**

    If you are familiar with another CI platform and you have code that you would like to test on an HPC Cluster via FirecREST, we can help you set up the CI.
