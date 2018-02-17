import web
import config

db = config.db


def get_all_agenda():
    try:
        return db.select('agenda')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_agenda(id_persona):
    try:
        return db.select('agenda', where='id_persona=$id_persona', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_agenda(id_persona):
    try:
        return db.delete('agenda', where='id_persona=$id_persona', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_agenda(nombre,telefono):
    try:
        return db.insert('agenda',nombre=nombre,
telefono=telefono)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_agenda(id_persona,nombre,telefono):
    try:
        return db.update('agenda',id_persona=id_persona,
nombre=nombre,
telefono=telefono,
                  where='id_persona=$id_persona',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
