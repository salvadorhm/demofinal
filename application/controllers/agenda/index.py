import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            elif session_privilege == 1: # guess user
                return self.GET_INDEX() # call GET_INDEX() function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
        result = config.model.get_all_agenda().list() # get agenda table list
        for row in result:
            row.id_persona = config.make_secure_val(str(row.id_persona)) # apply HMAC to id_persona (primary key)
        return config.render.index(result) # render agenda index.html
