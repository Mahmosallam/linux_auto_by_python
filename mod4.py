#!/usr/bin/python
import os
import subprocess
from mod1 import run_cmd

def install_httpd():
    """Install the Apache HTTPD server."""
    print("Installing httpd...")
    run_cmd("yum install -y httpd", capture=False)
    print("httpd installed.")

def start_and_enable_httpd():
    """Start and enable the httpd service."""
    print("Starting and enabling httpd service...")
    run_cmd("systemctl start httpd", capture=False)
    run_cmd("systemctl enable httpd", capture=False)
    print("httpd service started and enabled.")

def create_index_html():
    """Create an index.html with an image and heading centered."""
    html_path = "/var/www/html/index.html"
    image_src = "sallam.jpg"
    
    content = f"""
    <html>
        <head>
            <title>Welcome</title>
            <style>
                body {{
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                img {{
                    width: 400px;
                }}
            </style>
        </head>
        <body>
            <h1>msg from mahmoud sallam</h1>
            <img src="{image_src}" alt="Sallam Image">
        </body>
    </html>
    """
    
    with open(html_path, "w") as f:
        f.write(content.strip())
    
    print("index.html created with centered content and image.")



def copy_image():
    """Copy sallam.jpg to /var/www/html/"""
    src = "/root/sallam.jpg"  
    dest = "/var/www/html/sallam.jpg"
    run_cmd(f"cp {src} {dest}", capture=False)
    print("Image copied to web directory.")







def verify_website():
    """Verify website accessibility via curl."""
    print("Verifying website accessibility...")
    response = run_cmd("curl -s http://intranet.xyz.local")
    if "<h1>this is sallam</h1>" in response:
        print("Website is accessible and content is correct.")
    else:
        print("Website is not accessible or content mismatch.")






def disable_firewalld():
    print("Disabling firewalld...")
    run_cmd("systemctl stop firewalld", capture=False)
    run_cmd("systemctl disable firewalld", capture=False)
    print("firewalld stopped and disabled.")

def disable_selinux():
    print("Disabling SELinux (temporary and permanent)...")
    run_cmd("setenforce 0", capture=False)
    
    # Replace SELINUX=enforcing with SELINUX=disabled in /etc/selinux/config
    with open("/etc/selinux/config", "r") as file:
        config_lines = file.readlines()
    
    with open("/etc/selinux/config", "w") as file:
        for line in config_lines:
            if line.strip().startswith("SELINUX="):
                file.write("SELINUX=disabled\n")
            else:
                file.write(line)
    
    print("SELinux set to permissive now and disabled permanently.")




def main():
    disable_firewalld()
    disable_selinux()
    install_httpd()
    start_and_enable_httpd()
    copy_image()
    create_index_html()
    verify_website()




if __name__ == "__main__":
    main()
