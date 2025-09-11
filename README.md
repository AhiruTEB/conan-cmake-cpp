# {{PROJECT_NAME}}
[![.github/workflows/ci-cd.yml]({{PROJECT_HOMEPAGE_URL}}/actions/workflows/ci-cd.yml/badge.svg)]({{PROJECT_HOMEPAGE_URL}}/actions/workflows/ci-cd.yml)

Repository template for a cross-platform project written in C++ with use of Conan and CMake. This template has also GitHub actions configured for CI/CD with static analysis by clang-tidy and cppcheck. It has also clang-format configuration file for code formatting.

---

## ⚙️ How to Use This Template

This repository is a template. To create your own project from it, you need to run the **Configure Project** workflow. This workflow will replace all the placeholder values in the code and documentation with the values you provide.

### Steps to Configure Your Project

1.  Navigate to the **Actions** tab of your repository on GitHub.
2.  In the left sidebar, you will see a list of workflows. Click on **Configure Project**.
3.  You will see a button that says **Run workflow**. Click on it.
4.  A dropdown menu will appear with several input fields. Fill them out as described below:
    *   **New Project Name**: The name of your new project (e.g., `My Awesome Game`).
    *   **Project Description**: A short description of your project.
    *   **Project Homepage URL**: The URL for your project's homepage.
    *   **CPack Package Contact**: The contact email for your project.
5.  Click the **Run workflow** button.

The workflow will then run and create a new pull request. This pull request will contain all the changes, with the placeholders replaced by your provided values. Review the changes and merge the pull request to finalize the configuration of your project.