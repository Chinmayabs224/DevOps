# Lab Question 2: Branching and Merging with Git

## 📝 Problem Statement
**Create a new branch named `update-form`, modify the registration form by adding a new field (Department), merge the branch into `main`, and push the changes to GitHub.**

---

## ✅ Solution Steps

Follow these steps to complete the task.

### Step 1: Create a New Branch
Create a new branch named `update-form` and switch to it. This allows you to work on the new feature without affecting the main codebase.

**Commands:**
```bash
# Create and switch to the new branch
git checkout -b update-form

# Verify you are on the correct branch
git branch
```

### Step 2: Modify the Code
Update the `regestration.html` file to include the new "Department" field.

**Changes:**
1. Open `regestration.html`.
2. Add the "Department" input field in the HTML form.
3. Update the JavaScript to handle validation and submission for the new field.

*Reference Code for Updated Form:*
[updated-form.html](updated-form.html)

### Step 3: Stage and Commit Changes
After modifying the file, add it to the staging area and commit the changes to the `update-form` branch.

**Commands:**
```bash
# Check the status of your changes
git status

# Add the modified file
git add regestration.html

# Commit the changes
git commit -m "feat: Add department field to registration form"
```

### Step 4: Merge Branch into Main
Switch back to the `main` branch and merge the changes from `update-form` into it.

**Commands:**
```bash
# Switch to the main branch
git checkout main

# Merge the update-form branch
git merge update-form
```

### Step 5: Push Changes to GitHub
Push the updated `main` branch to the remote repository.

**Commands:**
```bash
# Push the changes
git push origin main
```
