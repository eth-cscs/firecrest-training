# CI/CD Pipeline with FirecREST

## Goal

Create a CI/CD pipeline that runs tests on Piz Daint via FirecREST.
The repository already contains the code to be tested and the pipeline is mostly configured -- you only need to fill in the parts that submit the job to the supercomputer and process the results.

## Prerequisites

- **Basic Python and Git knowledge**: the task involves straightforward Python; experience with another language is sufficient.
- **CSCS user account**: the pipeline is pre-configured for Piz Daint but requires minimal changes for a different machine.
- **GitHub account**: the CI uses GitHub Actions from your account.
- **Basic CI/CD understanding**: familiarity with continuous integration and deployment concepts is recommended.

## Getting Started

1. **Create an OIDC client**, if you haven't already.

2. **Fork and clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

    Enable the workflows in the **Actions** tab of your forked repository (they are disabled by default).

3. **Inspect the code to be tested** in the `mylib` folder. Add your own tests there.

4. **Configure the CI/CD pipeline:**
    - Open `.github/workflows/ci.yml` and review the steps already configured.
    - Set up the required secrets in your GitHub account (see [GitHub Actions secrets documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)):

        | Secret | Description |
        |--------|-------------|
        | `F7T_CLIENT_ID` | FirecREST client ID |
        | `F7T_CLIENT_SECRET` | FirecREST client secret |
        | `F7T_URL` | FirecREST API URL |
        | `F7T_TOKEN_URL` | OAuth2 token URL |

    - Edit `use-case-CI-pipeline/ci/ci_script.py`: remove the premature exit line and implement the commented sections using PyFirecREST or direct API calls.

5. **Review results:** commit and push your changes, then follow the workflow progress in the **Actions** tab.

6. **[Optional]** Apply this pattern to your own code using another CI platform.

## Additional Resources

- [PyFirecREST documentation](https://pyfirecrest.readthedocs.io)
- [FirecREST v2](https://eth-cscs.github.io/firecrest-v2/)
- [How to set up secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
