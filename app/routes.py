from pathlib import Path

from flask import Blueprint, abort, jsonify, render_template, send_from_directory

main = Blueprint("main", __name__)

RESUME_DIRECTORY = Path(__file__).parent / "static" / "resume"
RESUME_FILENAME = "nikita-kirilenko-resume.pdf"


@main.get("/")
def index():
    return render_template("index.html")


@main.get("/health")
def health():
    return jsonify(status="ok")


@main.get("/resume/<path:filename>")
def download_resume(filename: str):
    if filename != RESUME_FILENAME:
        abort(404)

    return send_from_directory(
        RESUME_DIRECTORY,
        RESUME_FILENAME,
        as_attachment=True,
        download_name="nikita-kirilenko-resume.pdf",
    )
