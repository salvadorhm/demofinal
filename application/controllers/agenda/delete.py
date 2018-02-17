import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_persona, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_persona) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_persona, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_persona) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_persona, **k):
        message = None # Error message
        id_persona = config.check_secure_val(str(id_persona)) # HMAC id_persona validate
        result = config.model.get_agenda(int(id_persona)) # search  id_persona
        result.id_persona = config.make_secure_val(str(result.id_persona)) # apply HMAC for id_persona
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_persona, **k):
        form = config.web.input() # get form data
        form['id_persona'] = config.check_secure_val(str(form['id_persona'])) # HMAC id_persona validate
        result = config.model.delete_agenda(form['id_persona']) # get agenda data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_persona = config.check_secure_val(str(id_persona))  # HMAC user validate
            id_persona = config.check_secure_val(str(id_persona))  # HMAC user validate
            result = config.model.get_agenda(int(id_persona)) # get id_persona data
            result.id_persona = config.make_secure_val(str(result.id_persona)) # apply HMAC to id_persona
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/agenda') # render agenda delete.html 
