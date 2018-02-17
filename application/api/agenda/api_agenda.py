import web
import config
import json


class Api_agenda:
    def get(self, id_persona):
        try:
            # http://0.0.0.0:8080/api_agenda?user_hash=12345&action=get
            if id_persona is None:
                result = config.model.get_all_agenda()
                agenda_json = []
                for row in result:
                    tmp = dict(row)
                    agenda_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(agenda_json)
            else:
                # http://0.0.0.0:8080/api_agenda?user_hash=12345&action=get&id_persona=1
                result = config.model.get_agenda(int(id_persona))
                agenda_json = []
                agenda_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(agenda_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            agenda_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(agenda_json)

# http://0.0.0.0:8080/api_agenda?user_hash=12345&action=put&id_persona=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,telefono):
        try:
            config.model.insert_agenda(nombre,telefono)
            agenda_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(agenda_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_agenda?user_hash=12345&action=delete&id_persona=1
    def delete(self, id_persona):
        try:
            config.model.delete_agenda(id_persona)
            agenda_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(agenda_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_agenda?user_hash=12345&action=update&id_persona=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_persona, nombre,telefono):
        try:
            config.model.edit_agenda(id_persona,nombre,telefono)
            agenda_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(agenda_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            agenda_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(agenda_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_persona=None,
            nombre=None,
            telefono=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_persona=user_data.id_persona
            nombre=user_data.nombre
            telefono=user_data.telefono
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_persona)
                elif action == 'put':
                    return self.put(nombre,telefono)
                elif action == 'delete':
                    return self.delete(id_persona)
                elif action == 'update':
                    return self.update(id_persona, nombre,telefono)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
