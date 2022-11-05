import datetime
import config


# creates file name for a screenshot in format «YYYY-MM-DD_HH:mm_<user id>.jpg»
def screenshot_adr():
    t = str(datetime.datetime.now())
    date = t[:10]+'_'+t[11:16]+'_'
    return config.screenshots_dir + date