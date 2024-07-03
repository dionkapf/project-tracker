from flask import Blueprint, render_template
from src.models import Project, db
 
main = Blueprint('main', __name__)
 
@main.route('/')
def home():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)
 
@main.route('/project/<int:project_id>')
def select_project(project_id):
    project = db.session.get(Project, project_id)
    return render_template('project.html', project=project)