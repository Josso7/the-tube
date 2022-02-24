from flask import Blueprint, request
from flask_login import login_required
from app.models import User, Video, Comment, db
from datetime import datetime, date

video_routes = Blueprint('videos', __name__)

@video_routes.route('/', methods=['POST'])
@login_required
def post_video():
    url = request.json
    video = Video(
        user_id = url['userId'],
        video_url = url['videoUrl'],
        title = url['title'],
        description = url['description'],
        created_at_date = date.today(),
        created_at_time = datetime.utcnow(),
        views = 12
    )
    db.session.add(video)
    db.session.commit()
    return {1:1}

@video_routes.route('/', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    return {'videos' : [video.to_dict() for video in videos]}

@video_routes.route('/<int:video_id>/video-comments', methods=['POST'])
@login_required
def post_comment(video_id):
    data = request.json
    comment = Comment(
        user_id = data['userId'],
        video_id = data['videoId'],
        content = data['comment'],
        created_at_date = date.today(),
        created_at_time = datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return{'comment': comment.to_dict()}

@video_routes.route('/<int:video_id>/video-comments', methods=['GET'])
def get_comments(video_id):
    comments = db.session.query(Comment).filter(video_id == Comment.video_id).order_by(Comment.id).all()
    return {'comments': [comment.to_dict() for comment in comments]}

@video_routes.route('/<int:video_id>/video-comments/<int:comment_id>', methods=['PUT'])
@login_required
def edit_comment(video_id, comment_id):
    data = request.json

    currentComment = Comment.query.get(comment_id)

    if (currentComment):
        currentComment.content = data['comment']
        db.session.commit()
        return {'comment' : currentComment.to_dict()}

    return {'didnt work'}

@video_routes.route('/<int:video_id>/video-comments/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(video_id, comment_id):
    comment = Comment.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return 'Delete successful'
