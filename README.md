# AG-DevOpsProject
# Adam Grimes - L00183736

# Python DevOps & CI/CD Pipeline Project

This project demonstrates a complete DevOps workflow for a Python application. While the Python code itself is simple (a basic combat calculator and choice processor), the focus of this repository is the robust **Continuous Integration (CI), automated testing, and security infrastructure** built around it.

It is designed to showcase best practices in modern software development, automation, and repository management, aligning with Agile and DevOps principles.

[![Python CI, Tests, and Docs](https://github.com/Adam-Grimes/AG-DevOpsProject/actions/workflows/ci_tests.yml/badge.svg)](https://github.com/Adam-Grimes/AG-DevOpsProject/actions/workflows/ci_tests.yml)

---

## 🚀 Key Features

### 🛠️ Automation & CI/CD
* **Continuous Integration:** A GitHub Actions workflow (`ci_tests.yml`) automatically builds and tests the project on every `push` and `pull_request` to `main`.
* **Continuous Deployment (CD):** The pipeline automatically builds HTML documentation and deploys it to **GitHub Pages**, ensuring documentation is always live and up-to-date.
* **Automated Dependency Management:** **Dependabot** is configured to scan for outdated dependencies and automatically open Pull Requests to update them.

### 🧪 Testing & Quality
* **Automated Unit Testing:** The pipeline runs a full suite of tests using Python's `unittest` framework.
* **Scalable Test Runner:** A custom `run_tests.py` script uses `unittest.TestLoader().discover` to find all files matching `test_*.py`. This ensures new tests are automatically registered without manual intervention.
* **Code Quality Analysis:** The pipeline integrates **Flake8** to enforce PEP 8 style guides and linting standards before any code is merged.

### 🔍 Observability (Logging & Monitoring)
* **Structured Logging:** The application (`combat.py`, `choice_processor.py`) implements Python's `logging` module to generate timestamped, informative logs (`app.log`) for traceability.
* **Automated Health Checks:** The CI pipeline includes a `health_check.py` script that verifies module availability and system stability post-testing.
* **Visual Monitoring:** A live **Workflow Status Badge** provides immediate feedback on pipeline health directly from the README.

### 📚 Documentation
* **Auto-Generated Documentation:** The project uses **pydoc** (Python's built-in documentation generator) to automatically create HTML documentation from code docstrings during the CI process.

---

## 🔁 CI/CD Pipeline Workflow

The pipeline defined in `.github/workflows/ci_tests.yml` executes the following steps on an `ubuntu-latest` runner:

1.  **Checkout Code:** Checks out the repository securely.
2.  **Environment Setup:** Sets up Python 3.10 for a consistent runtime.
3.  **Install Dependencies:** Installs `flake8` and other requirements.
4.  **Linting:** Runs `flake8` to check for syntax errors and style violations.
5.  **Test Suite:** Executes `python run_tests.py` to run all unit tests. The job fails immediately if any test fails.
6.  **Health Check (Monitoring):** Runs `python health_check.py` to verify that the application modules load correctly in the production-like environment.
7.  **Documentation Build:** Uses `pydoc` to generate HTML files for `choice_processor` and `combat`.
8.  **Deploy:** Uploads the generated HTML artifacts to **GitHub Pages**.

---

## 🛡️ Security & Compliance
* **Vulnerability Reporting:** Security policy defined in `SECURITY.md`.
* **Community Standards:** Expected behavior outlined in `CODE_OF_CONDUCT.md`.
* **Licensing:** Open source distribution under the Apache 2.0 `LICENSE`.
