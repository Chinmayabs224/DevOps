# Jenkins Freestyle Job: Auto Pull from GitHub & Trigger on Push

This guide outlines the steps to configure a Jenkins Freestyle Job that automatically pulls changes from GitHub when a push occurs, specifically tracking changes to `Q2/updated-form.html`.

## Prerequisites
- Jenkins is installed and running.
- A GitHub repository is set up with the project files (specifically `Q2/updated-form.html`).
- Jenkins has network access to the GitHub repository.

---

### A. Install Jenkins Plugins
Ensure the following plugins are installed in Jenkins (**Manage Jenkins** → **Plugins** → **Available plugins**):
1. **Git plugin**
2. **GitHub plugin** (GitHub Integration / GitHub Hook)
3. **GitHub Branch Source** (optional, but recommended)

---

### B. Create Jenkins Job

1. **Create New Item**:
   - Go to **Jenkins UI** → **New Item**.
   - Enter item name: `updated-form-build`.
   - Select **Freestyle project**.
   - Click **OK**.

2. **Source Code Management (Git)**:
   - Scroll to **Source Code Management** and select **Git**.
   - **Repository URL**: Enter your GitHub repository URL (e.g., `https://github.com/YOUR_USERNAME/devops-repo.git`).
   - **Credentials**: Add your GitHub credentials (username/password or SSH key) if the repo is private.
   - **Branch Specifier**: `*/main` (or `*/master` depending on your default branch).

3. **Build Triggers**:
   - Check **GitHub hook trigger for GITScm polling**.
   - *(Note: This enables Jenkins to listen for the "Push" webhooks from GitHub).*

4. **Build Steps**:
   - Scroll to **Build** section → **Add build step** → **Execute shell**.
   - Enter the following script to verify the build and display the file content:
     ```bash
     echo "Building updated-form project..."
     ls -la Q2/
     echo "Contents of Q2/updated-form.html (first 20 lines):"
     sed -n '1,20p' Q2/updated-form.html
     ```
   - Click **Save**.

---

### C. Configure GitHub Webhook

1. Go to your **GitHub Repository** settings.
2. Navigate to **Webhooks** → **Add webhook**.
3. **Payload URL**: `http://<YOUR_JENKINS_IP_OR_DNS>:8080/github-webhook/`
   - *Ensure you include the trailing slash `/`*.
4. **Content type**: Select `application/json`.
5. **Which events would you like to trigger this webhook?**: Select **Just the push event**.
6. Click **Add webhook**.

---

### D. Verification: Make a Change and Push

Perform these steps in your local terminal (Git Bash or VS Code terminal) to trigger the build.

1. **Checkout a new branch**:
   ```bash
   git checkout -b update-title
   ```

2. **Modify the HTML file**:
   Use `sed` to update the title in `Q2/updated-form.html` (or edit manually):
   ```bash
   # Update the title tag in the HTML file
   sed -i 's/Event Registration Form - Updated/Event Registration Form - CI Triggered/' Q2/updated-form.html
   ```

3. **Stage and Commit**:
   ```bash
   git add Q2/updated-form.html
   git commit -m "Update page title to test Jenkins trigger"
   ```

4. **Push to GitHub**:
   ```bash
   git push -u origin update-title
   ```

5. **Merge to Main**:
   ```bash
   git checkout main
   git merge update-title
   git push origin main
   ```

---

### E. Expected Results

1. **GitHub Side**:
   - In **Settings** → **Webhooks**, checking the "Recent Deliveries" should show a green checkmark (Status 200) for the push event.

2. **Jenkins Side**:
   - The job `updated-form-build` should automatically start running shortly after the push.
   - Click on the build number (e.g., **#1**) → **Console Output**.
   - You should see output similar to:
     ```text
     Building updated-form project...
     total ...
     Contents of Q2/updated-form.html (first 20 lines):
     <!DOCTYPE html>
     <html lang="en">
     <head>
     ...
     <title>Event Registration Form - CI Triggered</title>
     ...
     Finished: SUCCESS
     ```
