from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import main
from .forms import PostForm, CommentForm, UpdateProfile
from ..models import Post, Comment, User, Upvote, Downvote