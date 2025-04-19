
# Automating Linux Server Setup with Python

## Overview

This project is a fully automated **Linux server setup** script suite written in **Python** and tested on **Red Hat Linux 8**. It covers everything from networking to user management, directory permissions, and Apache web hosting — all through modular, reusable Python code with no manual steps required.

## Goal

To automate the internal deployment of a functional web server using Python scripts, replacing manual system administration tasks with safe and consistent automation.

---

## Project Structure

The project is divided into four main modules:

### `mod1.py` – System Configuration

**Features:**

- Detect active network interface using `nmcli`
- Configure static IP, DNS, and gateway
- Set system hostname
- Update `/etc/hosts`

**Challenges:**

- Handling inconsistent `nmcli` output
- Safe shell execution with `subprocess`
- Parsing command output for edge cases
- Ensuring line endings are `Unix (LF)` using `set ff=unix`
- Correct usage of shebang: `#!/usr/bin/python3`

---

### `mod2.py` – User Management

**Features:**

- Create system users
- Set passwords securely via `chpasswd`
- Add admin users to `sudo` group

**Challenges:**

- Secure password piping using `echo` + `chpasswd`
- Reusable `run_cmd()` function for commands
- `try-except` handling for user existence checks
- Avoiding duplicate users gracefully

---

### `mod3.py` – Directory Setup & Permissions

**Features:**

- Create required web directories
- Assign ownership using `chown`
- Set permissions (755)

**Challenges:**

- Mapping usernames to UID/GID using `os`, `pwd`, and `grp`
- Handling existing directories without breaking structure
- Catching exceptions from `os.chown` when users don’t exist yet

---

### `mod4.py` – Apache Installation & Deployment

**Features:**

- Install and start Apache (`httpd`)
- Generate `index.html` homepage
- Verify deployment using `curl`
- Disable `firewalld` and SELinux (temporary and permanent)

**Challenges:**

- Editing `/etc/selinux/config` safely with file I/O
- Generating HTML with Python
- Validating deployment programmatically with `curl`

---


---

#### **🔹 Key Features**  
| Feature | Description |  
|---------|-------------|  
| **Hostname & IP Automation** | Sets `intranet.xyz.local` and configures static networking via `nmcli`. |  
| **Multi-User Setup** | Creates `admin1` (sudo), `developer1`, and `viewer1` with passwords. |  
| **Apache Deployment** | Installs HTTPD, deploys a custom `index.html` with a centered image (`sallam.jpg`). |  
| **Permission Management** | Assigns `755` permissions and ownership to `/var/www/` directories. |  
| **Security Tweaks** | Disables `firewalld` and `SELinux` for development ease (⚠️ not for production). |  

#### **🔹 How It Works**  
1. **Execution Flow**:  
   - `main.py` calls modules in sequence:  
     ```python
     mod1.configure_system()  # Network/hostname  
     mod2.main()             # User creation  
     mod3.set_permissions()  # Directory setup  
     mod4.main()             # Apache + webpage  
     ```  
2. **Modules**:  
   - **`mod1.py`**: Uses `nmcli` to detect interfaces, set IPs, and update `/etc/hosts`.  
   - **`mod2.py`**: Creates users with `useradd`, sets passwords via `chpasswd`.  
   - **`mod3.py`**: Configures `/var/www/` ownership for `developer1`/`admin1`.  
   - **`mod4.py`**: Installs Apache, centers the image in HTML, and disables security modules.  

#### **🔹 Use Cases**  
- **Internal company portals** (e.g., HR docs, team dashboards).  
- **Educational labs** (quickly deploy web servers for students).  
- **DevOps practice** (Python + Linux automation).  

#### **🔹 Limitations**  
- **Hardcoded values**: Passwords (`1234`), hostname, and image path need manual updates.  
- **Security**: Disabling `firewalld`/`SELinux` is **not production-safe**.  
- **OS Compatibility**: Designed for RHEL/CentOS (uses `yum` and `nmcli`).  

#### **🔹 Future Improvements**  
- Add **user input prompts** for hostname/passwords.  
- Support **Ubuntu/Debian** (replace `yum` with `apt`).  
- Integrate **Ansible** for idempotent deployments.  

---



