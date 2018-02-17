import web

db_host = 'l6slz5o3eduzatkw.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'yhxafgboydvcojjh'
db_user = 'yh5ub3hhrtpx05tz'
db_pw = ' aiyl2x6v8rlh73le'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )