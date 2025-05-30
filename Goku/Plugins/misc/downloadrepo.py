
from pyrogram import Client, filters
import git
import shutil
import os
from Alya import app

@app.on_message(filters.command(["downloadrepo"]))
def download_repo(_, message):
    if len(message.command) != 2:
        message.reply_text("Please provide the GitHub repository URL after the command. Example: /downloadrepo <Repo URL>")
        return

    repo_url = message.command[1]
    zip_path = download_and_zip_repo(repo_url)

    if zip_path:
        with open(zip_path, "rb") as zip_file:
            message.reply_document(zip_file)
        os.remove(zip_path)
    else:
        message.reply_text("Unable to download the specified GitHub repository.")

def download_and_zip_repo(repo_url):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = f"{repo_name}"
    
    try:
        git.Repo.clone_from(repo_url, repo_path)
        shutil.make_archive(repo_path, 'zip', repo_path)
        return f"{repo_path}.zip"
    except git.exc.GitCommandError as e:
        print(f"Git error: {e}")
        return None
    except Exception as e:
        print(f"Error downloading and zipping GitHub repository: {e}")
        return None
    finally:
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
