# Git and GitHub Tutorial

This tutorial provides a comprehensive guide to using **Git** and **GitHub**, covering everything from basic concepts to advanced techniques. Whether you're a beginner or looking to deepen your understanding, this guide will walk you through version control, collaboration, and best practices with clear explanations, examples, and code snippets.

---

## 🧭 Table of Contents

1. [Introduction](#1-introduction)
2. [Git Basics](#2-git-basics)
3. [Working with Branches](#3-working-with-branches)
4. [Remote Repositories](#4-remote-repositories)
5. [GitHub Essentials](#5-github-essentials)
6. [Collaboration with Git and GitHub](#6-collaboration-with-git-and-github)
7. [Advanced Git](#7-advanced-git)
8. [Working with .gitignore](#8-working-with-gitignore)
9. [GitHub Advanced Features](#9-github-advanced-features)
10. [Best Practices](#10-best-practices)
11. [Troubleshooting & Tips](#11-troubleshooting--tips)
12. [Resources & Further Learning](#12-resources--further-learning)

---

## 1. Introduction

### What is Version Control?
Version control is a system that tracks changes to files, allowing multiple people to collaborate on a project while maintaining a history of changes. It enables you to revert to previous versions, track who made changes, and work on different features simultaneously.

### What is Git?
Git is a distributed version control system designed to handle everything from small to large projects with speed and efficiency. It tracks changes locally on your machine and supports collaboration through remote repositories.

### What is GitHub?
GitHub is a platform for hosting Git repositories, enabling collaboration, code sharing, and project management. It adds features like pull requests, issues, and CI/CD pipelines on top of Git.

### Git vs GitHub
- **Git**: A tool for version control, used locally or with any remote service.
- **GitHub**: A cloud-based service that hosts Git repositories and provides collaboration tools.

| Git       | GitHub           |
|-----------|------------------|
| Local VCS | Cloud platform   |
| CLI Tool  | Web UI & Hosting |
| Offline   | Online features  |


---

## 2. Git Basics

### Installing Git
Download and install Git from [git-scm.com](https://git-scm.com/). Verify installation:
```bash
git --version
```

### Setting up Git
Configure your username and email for commits:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Basic Git Workflow
1. **Initialize a repository**: Create a new Git repository.
   ```bash
   git init
   ```
2. **Clone a repository**: Copy an existing repository from a remote source.
   ```bash
   git clone https://github.com/username/repository.git
   ```
3. **Check status**: View the current state of your repository.
   ```bash
   git status
   ```
4. **Add files**: Stage changes for commit.
   ```bash
   git add filename.txt
   git add .  # Stages all changes
   ```
5. **Commit changes**: Save staged changes with a message.
   ```bash
   git commit -m "Add initial project files"
   ```
6. **View history**: See the commit log.
   ```bash
   git log
   ```
7. **View changes**: Compare changes between commits or working directory.
   ```bash
   git diff
   ```

---

## 3. Working with Branches

### What are Branches?
Branches allow you to work on different features or fixes independently. The default branch is usually `main`.

### Creating and Switching Branches
- Create a branch:
  ```bash
  git branch feature-branch
  ```
- Switch to a branch:
  ```bash
  git checkout feature-branch
  ```
- Create and switch in one command:
  ```bash
  git checkout -b feature-branch
  ```

### Merging Branches
Merge changes from one branch into another:
```bash
git checkout main
git merge feature-branch
```

### Resolving Merge Conflicts
If changes conflict, Git will pause the merge. Open the conflicting files, resolve the conflicts (marked with `<<<<<<<`, `=======`, `>>>>>>>`), then:
```bash
git add resolved-file.txt
git commit
```

---

## 4. Remote Repositories

### Adding a Remote
Link your local repository to a remote on GitHub:
```bash
git remote add origin https://github.com/username/repository.git
```

### Pushing to a Remote
Send local commits to the remote repository:
```bash
git push origin main
```

### Pulling Changes
Retrieve and merge changes from the remote:
```bash
git pull origin main
```

### Fetching Changes
Download changes without merging:
```bash
git fetch origin
```

### Removing a Remote
Remove a remote connection:
```bash
git remote remove origin
```

---

## 5. GitHub Essentials

### Creating a GitHub Account
Sign up at [github.com](https://github.com/) and verify your email.

### Creating a Repository on GitHub
1. Click "New repository" on GitHub.
2. Name it, add a description, and choose public/private.
3. Initialize with a README (optional).

### Connecting Local Repo to GitHub
```bash
git remote add origin https://github.com/username/repository.git
git push -u origin main
```

### Forking Repositories
Fork a repository by clicking "Fork" on GitHub to create your own copy.

### Starring and Watching
- **Star**: Bookmark repositories you like.
- **Watch**: Get notifications for repository updates.

---

## 6. Collaboration with Git and GitHub

### Pull Requests (PRs)
1. Push a branch to GitHub.
2. Create a PR on GitHub to propose changes.
3. Team members review and comment.
4. Merge the PR into the main branch.

### Issues and Bug Tracking
Use GitHub Issues to report bugs or request features. Assign labels, milestones, or assignees.

### Labels, Milestones, and Projects
- **Labels**: Categorize issues (e.g., "bug", "enhancement").
- **Milestones**: Group issues for specific releases.
- **Projects**: Organize tasks using Kanban boards.

---

## 7. Advanced Git

### Reverting Changes
- Undo a commit and keep changes:
  ```bash
  git reset HEAD~1
  ```
- Create a new commit to undo a previous one:
  ```bash
  git revert <commit-hash>
  ```

### Amending Commits
Modify the last commit:
```bash
git commit --amend
```

### Rebasing
Reapply commits on top of another base:
```bash
git rebase main
```

### Cherry-picking
Apply a specific commit to another branch:
```bash
git cherry-pick <commit-hash>
```

### Stashing Changes
Temporarily save uncommitted changes:
```bash
git stash
git stash pop
```

### Tagging Releases
Mark a specific commit (e.g., for a release):
```bash
git tag v1.0.0
git push origin v1.0.0
```

### Inspecting and Cleaning Up
Clean untracked files:
```bash
git clean -f
```

---

## 8. Working with .gitignore

### Purpose of .gitignore
A `.gitignore` file specifies which files or directories Git should ignore (e.g., temporary files, sensitive data).

### Creating and Editing .gitignore
Example `.gitignore`:
```
node_modules/
dist/
.env
*.log
```

---

## 9. GitHub Advanced Features

### GitHub Actions
Automate workflows (e.g., CI/CD). Example workflow file (`.github/workflows/ci.yml`):
```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: npm test
```

### GitHub Pages
Host static websites directly from a repository. Enable in repository settings.

### GitHub Discussions
Engage with the community through forum-like discussions.

### GitHub Wiki
Document your project with a built-in wiki.

### Security and Dependabot
Enable Dependabot to monitor and update dependencies for security vulnerabilities.

---

## 10. Best Practices

### Commit Message Conventions
Write clear, concise messages:
- Use present tense: "Add feature" not "Added feature".
- Example: `Add user authentication endpoint`

### Branching Strategies
- **Git Flow**: Use `main`, `develop`, and feature branches.
- **GitHub Flow**: Use `main` and short-lived feature branches.

### Code Reviews
Review PRs for quality, functionality, and style.

### Keeping Repositories Clean
Regularly prune old branches and archive stale repositories.

---

## 11. Troubleshooting & Tips

### Resolving Merge Conflicts
Manually edit conflicting files, then mark as resolved:
```bash
git add resolved-file.txt
git commit
```

### Undoing Mistakes
Recover a deleted branch:
```bash
git branch feature-branch <commit-hash>
```

### Managing SSH Keys
Generate and add an SSH key:
```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
cat ~/.ssh/id_rsa.pub  # Add to GitHub
```

---

## 12. Resources & Further Learning

- **Official Documentation**: 

    * [Git - Official Docs](https://git-scm.com/doc)
    * [GitHub Docs](https://docs.github.com/)

- Cheat Sheet

    * [Git Cheat Sheet PDF](https://education.github.com/git-cheat-sheet-education.pdf)

- **Community**: 

    * [GitHub Community](https://github.community/)
    * [Stack Overflow](https://stackoverflow.com/)

- **Books**: 

    * [Pro Git Book](https://git-scm.com/book/en/v2) by Scott Chacon and Ben Straub

- **Courses**: 

    * [GitHub Learning Lab](https://lab.github.com/)
    * [Coursera](https://www.coursera.org/)

---

Happy coding! 🚀
**Start your version-controlled journey today.**
If you found this helpful, ⭐ the repo and share!

Next Topic: - [Mathematics for AI](../lectures/templates/Mathematics_for_AI.html)

Need More Help: [Ask Your Questions](https://github.com/purus15987/LearnCV.ai/discussions/categories/q-a)
