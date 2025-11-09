# AG-DevOpsProject
# Adam Grimes - L00183736

# Python DevOps & CI/CD Pipeline Project

This project demonstrates a complete DevOps workflow for a Python application. While the Python code itself is simple (a basic combat calculator and choice processor), the focus of this repository is the robust **Continuous Integration (CI), automated testing, and security infrastructure** built around it.

It is designed to showcase best practices in modern software development, automation, and repository management.

[![Python CI Tests](https://github.com/Adam-Grimes/AG-DevOpsProject/actions/workflows/ci_tests.yml/badge.svg)](https://github.com/Adam-Grimes/AG-DevOpsProject/actions/workflows/ci_tests.yml)

---

## 🚀 Key Features

* **Continuous Integration Pipeline:** A full CI workflow using **GitHub Actions** that automatically builds and tests the project on every `push` and `pull_request` to the `main` branch.
* **Automated Unit Testing:** The pipeline automatically runs a full suite of unit tests. The project uses Python's built-in `unittest` framework.
* **Scalable Test Runner:** A custom `run_tests.py` script uses `unittest.TestLoader().discover` to find all files matching `test_*.py`. This means new tests are automatically included in the CI run, making the suite scalable.
* **CI-Friendly Exit Codes:** The test runner script properly reports failure to the CI system by using `sys.exit(1)`, ensuring the pipeline fails if any test fails.
* **Automated Dependency Management:** The repository uses **Dependabot** to automatically scan for outdated dependencies and create pull requests to update them, enhancing project security.
* **Code Quality & Documentation:** The pipeline is configured to run **linters** (like Flake8) to enforce code style and **auto-documentation tools** (like Sphinx) to keep documentation up-to-date.
* **Professional Repository Standards:** Includes standard community health files such as `LICENSE`, `CODE_OF_CONDUCT.md`, and a `SECURITY.md` with vulnerability reporting guidelines.

---

## 🔁 CI Pipeline Workflow

The CI pipeline defined in `.github/workflows/ci_tests.yml` executes the following steps on an `ubuntu-latest` runner:

1.  **Checkout Code:** `uses: actions/checkout@v5`
    * Securely checks out the repository's source code.
2.  **Set up Python:** `uses: actions/setup-python@v6`
    * Sets up a specific Python version (e.g., `3.10`) for a consistent test environment.
3.  **Install Dependencies:**
    * Upgrades `pip` and installs all required packages from `requirements.txt`.
4.  **Run Linters & Doc Generators:**
    * *(This step runs tools like Flake8 to check code style and Sphinx to build documentation).*
5.  **Run Test Suite:**
    * Executes the `python run_tests.py` script, which discovers and runs all unit tests.
    * The job will fail if any test fails, preventing bad code from being merged.
