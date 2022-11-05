import datetime


# creates file name for a screenshot in format «YYYY-MM-DD_HH:mm_<user id>.jpg»
def file_name():
    t = str(datetime.datetime.now())
    name = t[:10]+'_'+t[11:16]+'_'+'<user id>.jpg'
    return name