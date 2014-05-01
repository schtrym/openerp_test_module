from osv import osv
from osv import fields

class test_class(osv.osv):
    _name = 'test'
    _columns = {
            'name': fields.char('Name', size = 30,required= True)
                    }