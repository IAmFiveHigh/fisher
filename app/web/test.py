"""
  created by IAmFiveHigh on 2019-02-12
 """

from . import web


@web.route('/sun')
def sun_image():
    return "<img src='static/images/sun.jpg'>"


