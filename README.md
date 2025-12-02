# NkuAlert

**Timely local alerts for weather, health, and civic updates**

## Project Description

### Problem Statement
In many Rwandan communities — especially rural or semi‑urban areas — people rely on word of mouth, radio, or delayed SMS for critical information like heavy rain warnings, disease outbreaks, power outages, or community meetings. There is often no centralized, low‑tech, or accessible system to broadcast and retrieve verified local alerts quickly. This leads to missed warnings, poor preparedness, and reduced civic engagement.

NkuAlert solves this by providing a lightweight, web-accessible platform where trusted local admins can post alerts, and community members can view the latest updates.

### Target Users
- **Community members**: Residents who need timely, trustworthy local information
- **Local admins**: Teachers, health workers, ward councillors, or cooperative leaders who disseminate alerts

### Core Features
1. **View Latest Alerts** - Users see the 10 most recent alerts, each labeled with category (Weather, Health, Civic, Emergency), timestamp, and short message
2. **Post New Alert (Admin-Only Simulation)** - Simple form allows mock "admin" input: category, message, and location
3. **Filter Alerts by Category** - Users can click Weather, Health, Civic, Emergency to see only relevant alerts
4. **Responsive, Low-Bandwidth UI** - Lightweight HTML/CSS that loads fast on 2G networks and basic devices
5. **Alert Expiry Indicator** - Alerts older than 72 hours are marked "Past"

### Technology Stack
- **Backend**: Python with Flask (minimal, easy to containerize)
- **Frontend**: Plain HTML, CSS, and minimal JavaScript (no heavy frameworks)
- **Data Storage**: JSON file (for F1; scalable to SQLite later)
- **Deployment**: Docker container, deployable to cloud (e.g., Render, AWS ECS, or Fly.io)
  
### Pipeline Architecture Diagram
(CI)
----------------------
Pull Request Created
        │
        ▼
   Checkout Code
        │
        ▼
     Run Linter
        │
        ▼
     Run Tests
        │
        ▼
  Build Docker Image
        │
        ▼
  Scan Image (Trivy)
        │
        ▼
  Scan IaC (tfsec)
        │
   ┌────┴─────┐
   │          │
Pass → Allow Merge
Fail → Block Merge
--------------------

### Pipeline Architecture Diagram
(Cd)
----------------------
Merge to Main
        │
        ▼
    Run CI Checks
        │
        ▼
    Build Docker Image
        │
        ▼
Push to Container Registry (ECR/ACR)
        │
        ▼
  Run Ansible Playbook
        │
        ▼
 Application Updated
        │
        ▼
 Live on Public URL
--------------------
## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)
- Terraform v1.x
- Ansible 2.9+
- Git
- An AWS or Azure account with permissions for networking, VMs, and a managed database
### Installation

1. Clone the repository
   ```bash
   git clone <https://github.com/lasgedu/NkuAlert>
   cd NkuAlert
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Provision infrastructure (Terraform)

```powershell
cd terraform
terraform init
terraform apply -auto-approve
```

4. Configure GitHub Secrets
- CLOUD credentials (AWS/ Azure)
- `SSH_PRIVATE_KEY` — private key used by Ansible to connect via bastion
- Registry credentials 



3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   Open your browser and navigate to `https://nkualert-app-lb.uaenorth.cloudapp.azure.com`

### Running with Docker

1. **Build the Docker image**
   ```bash
   docker build -t nkualert.
   ```

### Running with Docker Compose

Docker Compose lets you build and run everything with one command while persisting alert data.

1. **Start the stack (builds if needed)**
   ```bash
   docker compose up --build
   ```
   
   To run in the background (detached mode):
   ```bash
   docker compose up -d --build
   ```

2. **Open the app**
   Visit `http://20.174.99.204/` in your browser.

3. **Environment variables**
   - `FLASK_SECRET_KEY` controls Flask session encryption (override in production).
   - `ALERTS_FILE` points to the alerts JSON file (defaults to `/data/alerts.json`).

4. **Persisted data**
   Alerts are stored in the named volume `alerts_data`, so they survive container restarts.

5. **Stop the services**
   ```bash
   docker compose down
   ```

6. **Clean up volumes (removes saved alerts)**
   ```bash
   docker compose down -v
   ```

## Usage

### Viewing Alerts
- Visit the homepage to see all alerts sorted by most recent
- Use the filter buttons (All, Weather, Health, Civic, Emergency) to view specific categories
- Alerts older than 72 hours are marked with a "Past" badge

### Posting New Alerts (Admin)
1. Click the "+ Post New Alert (Admin)" button
2. Fill in the form:
   - Select a category
   - Enter the alert message
   - Specify the location
3. Click "Post Alert" to submit

### Editing or Deleting Alerts (Admin)
- To edit: Click "Edit" on an alert card, update fields, then click "Update Alert".
- To delete: Click "Delete" on an alert card to remove it.

### Language Selection
- Use the language links at the top to switch between English and Kinyarwanda.
- Your selection is remembered in your browser session.

## Team Members

- Chiedu Paul Unekwe (GitHub: @lasgedu)
  - Repository initialization and collaborator access
  - Initial Flask app and core feature implementation
  - Templates and API endpoints
  - PR reviews and merges

- Vestine Pendo (GitHub: @vpendo)
  - Branch protection rules configuration
  - GitHub Projects board (8–10 items) and labeling
  - README authoring and setup instructions
  - UI styling, language toggle, and admin edit/delete UX
  - Dockerfile creation and optimization (non-root user, security hardening, Python 3.11.9)
  - docker-compose.yml configuration (container orchestration, volumes, networking)
  - .dockerignore file creation

- Bosco Ishimwe (GitHub: @[username])
  - Branch protection rules: Require CI checks to pass before merging to main
  - Pull request integration and code review process
  - Team collaboration facilitation: Multiple team member contributions
  - Code reviews on pull requests
  - Project board maintenance and continued use

## Progress Report

As a team, one of our main challenges during this phase was Docker installation and setup. It became a problem on some of our machines due to version incompatibilities and environment configuration issues. Building the Docker image and ensuring it ran correctly across different systems required extra troubleshooting. We also encountered difficulties setting up GitHub Actions for Continuous Integration (CI), especially in configuring the workflow files and ensuring the automated builds passed all tests without errors.

Through this experience, we learned how Docker helps create a consistent environment for running applications regardless of the host machine. We also gained valuable insights into CI and how it automates the build, test, and validation process, improving efficiency and reducing manual errors. This helped us better understand the importance of DevOps practices in modern software development.

Compared to F1, the NkuAlert project has evolved significantly. We introduced Docker containerization, implemented a CI workflow using GitHub Actions, and improved our documentation and project structure. These enhancements have made the project more reliable, scalable, and easier to collaborate on as a team.
