from osv import osv
from osv import fields

class players(osv.osv):
    _name = 'test.players'
    _columns = {
            'player_name': fields.char('Name', size = 30,required= True)
            }
    _order = 'player_name' 
   
    _sql_constraints = [     ('PLAYER_UK', 'unique (player_name)', 'The name of the player must be unique !'),      ]