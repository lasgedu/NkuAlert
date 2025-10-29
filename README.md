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

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone <https://github.com/lasgedu/NkuAlert>
   cd NkuAlert
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Running with Docker

1. **Build the Docker image**
   ```bash
   docker build -t nkualert .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 nkualert
   ```

3. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

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
- Chiedu Paul Unekwe - Create repository and add Members as collaborator
                    - Write initial application code
                    - Implement the core feature

- Vestine Pendo 
                - Configure branch protection rules
                - Create GitHub Projects board (8-10 items)
                - Write README.md with project description
                - Add setup instructions

## Future Enhancements
- User authentication and authorization
- Database migration from JSON to SQLite/PostgreSQL
- SMS/Email notifications
- Mobile app integration
- Image attachments for alerts
- Push notifications



## Project Management (F1 Checklist)

- Project Board: [add board URL]
- Milestone: `M1 - Initial Release (Sprint 1)` (created: [yes/no])
- Labels: feature, devops, bug, enhancement, documentation, priority:high, priority:medium, priority:low ([created: yes/no])
- Branch Protection on `main`: PR required, 1 approval, stale approvals dismissed, status checks, up-to-date before merge, conversations resolved, include admins ([enabled: yes/no])
