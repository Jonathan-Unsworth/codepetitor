from flask import Blueprint, render_template, url_for, session
from codepetitor.models import db
from flask_socketio import SocketIO, emit
from codepetitor.codepetitor import socketio


blueprint_collaborator = Blueprint (
    'blueprint_collaborator',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

@blueprint_collaborator.route('/')
def collaborator():
    print(session['username'])
    task = db.Task.get(task_id=1)
    return render_template('collaborator/collaborator.html', task_desc=task.task_description, task_name=task.task_name, task_code=task.task_code, username=session['username'])

# @blueprint_collaborator.route('/username/<username>')
# def collaborator(username):
#     task = db.Task.get(task_id=1)
#     return render_template('collaborator/collaborator.html', task_desc=task.task_description, task_name=task.task_name, task_code=task.task_code, username=session['username'])


@socketio.on('my event')
def handle_message():
    print('Success Success Success!!!')


@socketio.on('collab_update')
def handle_collab_update(data):
    emit('update_editor', data, broadcast=True, include_self=False)


@socketio.on('chat_update')
def handle_chat_update(data):
    emit('update_chat', data, broadcast=True)
