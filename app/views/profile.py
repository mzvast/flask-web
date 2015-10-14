from flask import Blueprint, render_template,g

profile = Blueprint('profile', __name__)

@profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    # query = User.query.filter_by(url_slug=values.pop('user_url_slug'))
    # g.profile_owner = query.first_or_404()
    g.profile_owner = values.pop('user_url_slug')

@profile.route('/')
def timeline():
    # Do some stuff
    return '%s profile/timeline.html '%(g.profile_owner)

@profile.route('/photos')
def photos():
    # Do some stuff
    return 'profile/photos.html'

@profile.route('/about')
def about():
    # Do some stuff
    return 'profile/about.html'