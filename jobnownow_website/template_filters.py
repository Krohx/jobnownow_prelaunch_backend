"""
jobnownow_website.template_filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions defined in this document using the `@jinja2.contextfilter`
decorator can be called from a Jinja2 template document.

The first parameter is a "contextfilter()".

See documentation at:
        http://jinja.pocoo.org/docs/dev/api/#jinja2.contextfilter

:author: Krohx Technologies (krohxinc@gmail.com)
:copyright: (c) 2016 by Krohx Technologies
:license: see LICENSE for details.
"""

# library imports
import jinja2


# compute the number of days between today
# and specified date throug 'date' parameter
@jinja2.contextfilter
def get_num_days_left(context, date):
    
    import datetime
    
    return (date.date() - datetime.date.today()).days


# get the current year
@jinja2.contextfilter
def get_current_year(context, num):
    
    import datetime
    
    return datetime.datetime.utcnow().year


# get the current year
@jinja2.contextfilter
def get_date(context, dt=None):

    import datetime

    try:
        date = dt.date()
        return date
    except Exception, e:
        raise e
        return ''
    

# get time from date
#@jinja2.contextfilter
def get_time(date=None, milli=False):
    
    import datetime

    if date:
        
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            
            time = date.time
            
            if milli:
                return time().strftime("%H.%M.%S.%f")

            return time().strftime("%H.%M.%S")

        except Exception, e:
            raise e
            return ''

    else:
        return ''


# debug-print the passed value
@jinja2.contextfilter
def dbg_print(context, val=''):

    print 'DEBUG_JINJA_PRINT:\t %r' % val


# mark message as 'Read'
@jinja2.contextfilter
def msg_status_change(context, msg):

    from . import db_ops
    param_dict = {}
    param_dict['msg_id'] = msg.msg_id
    
    # mark all user's notifications as read, i.e change 'notif_status'
    db_ops.update_row(db_ops.Message, param_dict, dict(msg_status='Read'))


# custom filter for text-truncate
# 
# Important!
# Remember to pass the result of this function to
# the Jinja2 Template "safe()" function, to escape
# special HTML character "&nbsp"
@jinja2.contextfilter
def truncate_text(context, text, size):
    
    ellipsis = " ..."
    space = "&nbsp"
    
    if len(text)<size:
        spaces = space * ((size-4) - len(text))
        return text + ellipsis + spaces

    else:
        return text[:size-4] + ellipsis

