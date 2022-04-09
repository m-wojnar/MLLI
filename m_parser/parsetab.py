
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSEright=MULASSIGNDIVASSIGNADDASSIGNSUBASSIGNnonassoc><GELEEQNEleftDOTADDDOTSUB+-leftDOTMULDOTDIV*/rightUMINUSleft\'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GE ID IF INTNUM LE MULASSIGN NE ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructions\n               | instructions : instructions instruction\n                    | instruction instruction : \'{\' instructions \'}\' instruction : RETURN \';\'\n                   | RETURN expr \';\'\n                   | BREAK \';\'\n                   | CONTINUE \';\' instruction : PRINT expressions \';\' instruction : var \'=\' expr \';\'\n                   | var ADDASSIGN expr \';\'\n                   | var SUBASSIGN expr \';\'\n                   | var MULASSIGN expr \';\'\n                   | var DIVASSIGN expr \';\' instruction : WHILE \'(\' condition \')\' instruction instruction : FOR ID \'=\' range instruction\n                   | FOR \'(\' ID \'=\' range \')\' instruction instruction : IF \'(\' condition \')\' instruction %prec IFX\n                   | IF \'(\' condition \')\' instruction ELSE instruction condition : expr EQ expr\n                 | expr NE expr\n                 | expr GE expr\n                 | expr LE expr\n                 | expr \'>\' expr\n                 | expr \'<\' expr var : ID expr : ID \'[\' range \']\' var : ID \'[\' range \']\' var : ID \'[\' expr \']\'\n           | ID \'[\' expr \',\' expr \']\' expr : ID \'[\' expr \']\'\n            | ID \'[\' expr \',\' expr \']\' expr : \'-\' expr %prec UMINUS expr : expr \'+\' expr\n            | expr \'-\' expr\n            | expr \'*\' expr\n            | expr \'/\' expr\n            | expr DOTADD expr\n            | expr DOTSUB expr\n            | expr DOTMUL expr\n            | expr DOTDIV expr expr : \'(\' expr \')\' expr : expr "\'" expr : EYE \'(\' expr \')\'\n            | ZEROS \'(\' expr \')\'\n            | ONES \'(\' expr \')\' expr : FLOATNUM expr : INTNUM expr : STRING expr : ID expr : \'[\' expressions \']\' expr : \'[\' range \']\' expressions : expressions \',\' expr\n                   | expr range : expr \':\' expr '
    
_lr_action_items = {'$end':([0,1,2,3,14,16,28,29,42,43,62,94,95,96,97,98,120,127,130,136,137,],[-2,0,-1,-4,-3,-6,-8,-9,-5,-7,-10,-11,-12,-13,-14,-15,-16,-17,-19,-18,-20,]),'{':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[4,4,-4,4,-3,4,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,4,4,4,-28,-32,-56,-45,-46,-47,-16,-17,-19,4,4,-33,-18,-20,]),'RETURN':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[5,5,-4,5,-3,5,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,5,5,5,-28,-32,-56,-45,-46,-47,-16,-17,-19,5,5,-33,-18,-20,]),'BREAK':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[6,6,-4,6,-3,6,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,6,6,6,-28,-32,-56,-45,-46,-47,-16,-17,-19,6,6,-33,-18,-20,]),'CONTINUE':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[7,7,-4,7,-3,7,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,7,7,7,-28,-32,-56,-45,-46,-47,-16,-17,-19,7,7,-33,-18,-20,]),'PRINT':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[8,8,-4,8,-3,8,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,8,8,8,-28,-32,-56,-45,-46,-47,-16,-17,-19,8,8,-33,-18,-20,]),'WHILE':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[10,10,-4,10,-3,10,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,10,10,10,-28,-32,-56,-45,-46,-47,-16,-17,-19,10,10,-33,-18,-20,]),'FOR':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[11,11,-4,11,-3,11,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,11,11,11,-28,-32,-56,-45,-46,-47,-16,-17,-19,11,11,-33,-18,-20,]),'IF':([0,2,3,4,14,15,16,18,25,26,27,28,29,42,43,52,57,62,76,77,78,79,80,81,82,83,86,87,89,94,95,96,97,98,99,106,112,113,114,116,117,118,119,120,127,130,132,134,135,136,137,],[13,13,-4,13,-3,13,-6,-51,-48,-49,-50,-8,-9,-5,-7,-44,-34,-10,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-11,-12,-13,-14,-15,13,13,13,-28,-32,-56,-45,-46,-47,-16,-17,-19,13,13,-33,-18,-20,]),'ID':([0,2,3,4,5,8,11,14,15,16,18,19,20,21,25,26,27,28,29,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,59,60,61,62,63,71,76,77,78,79,80,81,82,83,86,87,88,89,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,114,115,116,117,118,119,120,127,130,132,134,135,136,137,],[12,12,-4,12,18,18,38,-3,12,-6,-51,18,18,18,-48,-49,-50,-8,-9,18,18,18,18,18,18,72,18,18,-5,-7,18,18,18,18,18,18,18,18,-44,18,-34,18,18,18,-10,18,18,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,18,-43,-11,-12,-13,-14,-15,12,18,18,18,18,18,18,12,18,18,12,-28,-32,18,-56,-45,-46,-47,-16,-17,-19,12,12,-33,-18,-20,]),'}':([3,14,15,16,28,29,42,43,62,94,95,96,97,98,120,127,130,136,137,],[-4,-3,42,-6,-8,-9,-5,-7,-10,-11,-12,-13,-14,-15,-16,-17,-19,-18,-20,]),';':([5,6,7,17,18,25,26,27,30,31,52,57,64,65,66,67,68,76,77,78,79,80,81,82,83,86,87,89,93,113,114,117,118,119,135,],[16,28,29,43,-51,-48,-49,-50,62,-55,-44,-34,94,95,96,97,98,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-54,-28,-32,-45,-46,-47,-33,]),'-':([5,8,17,18,19,20,21,25,26,27,31,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,52,53,56,57,58,59,60,61,63,64,65,66,67,68,70,71,74,76,77,78,79,80,81,82,83,85,86,87,88,89,90,91,92,93,100,101,102,103,104,105,107,108,111,113,114,115,116,117,118,119,121,122,123,124,125,126,129,131,135,],[20,20,45,-51,20,20,20,-48,-49,-50,45,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-44,20,45,-34,45,20,20,20,20,45,45,45,45,45,45,20,45,-35,-36,-37,-38,-39,-40,-41,-42,45,-52,-53,20,-43,45,45,45,45,20,20,20,20,20,20,45,20,20,-28,-32,20,45,-45,-46,-47,45,45,45,45,45,45,45,45,-33,]),'(':([5,8,10,11,13,19,20,21,22,23,24,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[21,21,37,39,41,21,21,21,59,60,61,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'EYE':([5,8,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'ZEROS':([5,8,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'ONES':([5,8,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'FLOATNUM':([5,8,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'INTNUM':([5,8,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'STRING':([5,8,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'[':([5,8,12,18,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[19,19,40,53,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'=':([9,12,38,72,109,110,133,],[32,-27,71,108,-29,-30,-31,]),'ADDASSIGN':([9,12,109,110,133,],[33,-27,-29,-30,-31,]),'SUBASSIGN':([9,12,109,110,133,],[34,-27,-29,-30,-31,]),'MULASSIGN':([9,12,109,110,133,],[35,-27,-29,-30,-31,]),'DIVASSIGN':([9,12,109,110,133,],[36,-27,-29,-30,-31,]),'ELSE':([16,28,29,42,43,62,94,95,96,97,98,120,127,130,136,137,],[-6,-8,-9,-5,-7,-10,-11,-12,-13,-14,-15,-16,-17,134,-18,-20,]),'+':([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[44,-51,-48,-49,-50,44,-44,44,-34,44,44,44,44,44,44,44,44,-35,-36,-37,-38,-39,-40,-41,-42,44,-52,-53,-43,44,44,44,44,44,-28,-32,44,-45,-46,-47,44,44,44,44,44,44,44,44,-33,]),'*':([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[46,-51,-48,-49,-50,46,-44,46,-34,46,46,46,46,46,46,46,46,46,46,-37,-38,46,46,-41,-42,46,-52,-53,-43,46,46,46,46,46,-28,-32,46,-45,-46,-47,46,46,46,46,46,46,46,46,-33,]),'/':([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[47,-51,-48,-49,-50,47,-44,47,-34,47,47,47,47,47,47,47,47,47,47,-37,-38,47,47,-41,-42,47,-52,-53,-43,47,47,47,47,47,-28,-32,47,-45,-46,-47,47,47,47,47,47,47,47,47,-33,]),'DOTADD':([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[48,-51,-48,-49,-50,48,-44,48,-34,48,48,48,48,48,48,48,48,-35,-36,-37,-38,-39,-40,-41,-42,48,-52,-53,-43,48,48,48,48,48,-28,-32,48,-45,-46,-47,48,48,48,48,48,48,48,48,-33,]),'DOTSUB':([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[49,-51,-48,-49,-50,49,-44,49,-34,49,49,49,49,49,49,49,49,-35,-36,-37,-38,-39,-40,-41,-42,49,-52,-53,-43,49,49,49,49,49,-28,-32,49,-45,-46,-47,49,49,49,49,49,49,49,49,-33,]),'DOTMUL':([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[50,-51,-48,-49,-50,50,-44,50,-34,50,50,50,50,50,50,50,50,50,50,-37,-38,50,50,-41,-42,50,-52,-53,-43,50,50,50,50,50,-28,-32,50,-45,-46,-47,50,50,50,50,50,50,50,50,-33,]),'DOTDIV':([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[51,-51,-48,-49,-50,51,-44,51,-34,51,51,51,51,51,51,51,51,51,51,-37,-38,51,51,-41,-42,51,-52,-53,-43,51,51,51,51,51,-28,-32,51,-45,-46,-47,51,51,51,51,51,51,51,51,-33,]),"'":([17,18,25,26,27,31,52,56,57,58,64,65,66,67,68,70,74,76,77,78,79,80,81,82,83,85,86,87,89,90,91,92,93,107,113,114,116,117,118,119,121,122,123,124,125,126,129,131,135,],[52,-51,-48,-49,-50,52,-44,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-52,-53,-43,52,52,52,52,52,-28,-32,52,-45,-46,-47,52,52,52,52,52,52,52,52,-33,]),',':([18,25,26,27,30,31,52,54,56,57,74,76,77,78,79,80,81,82,83,85,86,87,89,93,113,114,117,118,119,135,],[-51,-48,-49,-50,63,-55,-44,63,-55,-34,111,-35,-36,-37,-38,-39,-40,-41,-42,115,-52,-53,-43,-54,-28,-32,-45,-46,-47,-33,]),':':([18,25,26,27,52,56,57,74,76,77,78,79,80,81,82,83,85,86,87,89,107,113,114,117,118,119,135,],[-51,-48,-49,-50,-44,88,-34,88,-35,-36,-37,-38,-39,-40,-41,-42,88,-52,-53,-43,88,-28,-32,-45,-46,-47,-33,]),']':([18,25,26,27,52,54,55,56,57,73,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,113,114,116,117,118,119,129,131,135,],[-51,-48,-49,-50,-44,86,87,-55,-34,109,110,-35,-36,-37,-38,-39,-40,-41,-42,113,114,-52,-53,-43,-54,-28,-32,-56,-45,-46,-47,133,135,-33,]),')':([18,25,26,27,52,57,58,69,75,76,77,78,79,80,81,82,83,86,87,89,90,91,92,113,114,116,117,118,119,121,122,123,124,125,126,128,135,],[-51,-48,-49,-50,-44,-34,89,99,112,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,117,118,119,-28,-32,-56,-45,-46,-47,-21,-22,-23,-24,-25,-26,132,-33,]),'EQ':([18,25,26,27,52,57,70,76,77,78,79,80,81,82,83,86,87,89,113,114,117,118,119,135,],[-51,-48,-49,-50,-44,-34,100,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-28,-32,-45,-46,-47,-33,]),'NE':([18,25,26,27,52,57,70,76,77,78,79,80,81,82,83,86,87,89,113,114,117,118,119,135,],[-51,-48,-49,-50,-44,-34,101,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-28,-32,-45,-46,-47,-33,]),'GE':([18,25,26,27,52,57,70,76,77,78,79,80,81,82,83,86,87,89,113,114,117,118,119,135,],[-51,-48,-49,-50,-44,-34,102,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-28,-32,-45,-46,-47,-33,]),'LE':([18,25,26,27,52,57,70,76,77,78,79,80,81,82,83,86,87,89,113,114,117,118,119,135,],[-51,-48,-49,-50,-44,-34,103,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-28,-32,-45,-46,-47,-33,]),'>':([18,25,26,27,52,57,70,76,77,78,79,80,81,82,83,86,87,89,113,114,117,118,119,135,],[-51,-48,-49,-50,-44,-34,104,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-28,-32,-45,-46,-47,-33,]),'<':([18,25,26,27,52,57,70,76,77,78,79,80,81,82,83,86,87,89,113,114,117,118,119,135,],[-51,-48,-49,-50,-44,-34,105,-35,-36,-37,-38,-39,-40,-41,-42,-52,-53,-43,-28,-32,-45,-46,-47,-33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions':([0,4,],[2,15,]),'instruction':([0,2,4,15,99,106,112,132,134,],[3,14,3,14,120,127,130,136,137,]),'var':([0,2,4,15,99,106,112,132,134,],[9,9,9,9,9,9,9,9,9,]),'expr':([5,8,19,20,21,32,33,34,35,36,37,40,41,44,45,46,47,48,49,50,51,53,59,60,61,63,71,88,100,101,102,103,104,105,108,111,115,],[17,31,56,57,58,64,65,66,67,68,70,74,70,76,77,78,79,80,81,82,83,85,90,91,92,93,107,116,121,122,123,124,125,126,107,129,131,]),'expressions':([8,19,],[30,54,]),'range':([19,40,53,71,108,],[55,73,84,106,128,]),'condition':([37,41,],[69,75,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','parser.py',40),
  ('program -> <empty>','program',0,'p_program','parser.py',41),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','parser.py',48),
  ('instructions -> instruction','instructions',1,'p_instructions','parser.py',49),
  ('instruction -> { instructions }','instruction',3,'p_instructions_block','parser.py',60),
  ('instruction -> RETURN ;','instruction',2,'p_control_statements','parser.py',66),
  ('instruction -> RETURN expr ;','instruction',3,'p_control_statements','parser.py',67),
  ('instruction -> BREAK ;','instruction',2,'p_control_statements','parser.py',68),
  ('instruction -> CONTINUE ;','instruction',2,'p_control_statements','parser.py',69),
  ('instruction -> PRINT expressions ;','instruction',3,'p_print','parser.py',83),
  ('instruction -> var = expr ;','instruction',4,'p_assign','parser.py',89),
  ('instruction -> var ADDASSIGN expr ;','instruction',4,'p_assign','parser.py',90),
  ('instruction -> var SUBASSIGN expr ;','instruction',4,'p_assign','parser.py',91),
  ('instruction -> var MULASSIGN expr ;','instruction',4,'p_assign','parser.py',92),
  ('instruction -> var DIVASSIGN expr ;','instruction',4,'p_assign','parser.py',93),
  ('instruction -> WHILE ( condition ) instruction','instruction',5,'p_while_statement','parser.py',109),
  ('instruction -> FOR ID = range instruction','instruction',5,'p_for_statement','parser.py',115),
  ('instruction -> FOR ( ID = range ) instruction','instruction',7,'p_for_statement','parser.py',116),
  ('instruction -> IF ( condition ) instruction','instruction',5,'p_if_statement','parser.py',126),
  ('instruction -> IF ( condition ) instruction ELSE instruction','instruction',7,'p_if_statement','parser.py',127),
  ('condition -> expr EQ expr','condition',3,'p_condition','parser.py',137),
  ('condition -> expr NE expr','condition',3,'p_condition','parser.py',138),
  ('condition -> expr GE expr','condition',3,'p_condition','parser.py',139),
  ('condition -> expr LE expr','condition',3,'p_condition','parser.py',140),
  ('condition -> expr > expr','condition',3,'p_condition','parser.py',141),
  ('condition -> expr < expr','condition',3,'p_condition','parser.py',142),
  ('var -> ID','var',1,'p_id_var','parser.py',160),
  ('expr -> ID [ range ]','expr',4,'p_vector_range_expr','parser.py',166),
  ('var -> ID [ range ]','var',4,'p_vector_range_var','parser.py',172),
  ('var -> ID [ expr ]','var',4,'p_vector_el_var','parser.py',178),
  ('var -> ID [ expr , expr ]','var',6,'p_vector_el_var','parser.py',179),
  ('expr -> ID [ expr ]','expr',4,'p_vector_el_expr','parser.py',184),
  ('expr -> ID [ expr , expr ]','expr',6,'p_vector_el_expr','parser.py',185),
  ('expr -> - expr','expr',2,'p_unary_minus_expression','parser.py',200),
  ('expr -> expr + expr','expr',3,'p_binary_expression','parser.py',206),
  ('expr -> expr - expr','expr',3,'p_binary_expression','parser.py',207),
  ('expr -> expr * expr','expr',3,'p_binary_expression','parser.py',208),
  ('expr -> expr / expr','expr',3,'p_binary_expression','parser.py',209),
  ('expr -> expr DOTADD expr','expr',3,'p_binary_expression','parser.py',210),
  ('expr -> expr DOTSUB expr','expr',3,'p_binary_expression','parser.py',211),
  ('expr -> expr DOTMUL expr','expr',3,'p_binary_expression','parser.py',212),
  ('expr -> expr DOTDIV expr','expr',3,'p_binary_expression','parser.py',213),
  ('expr -> ( expr )','expr',3,'p_brackets_expression','parser.py',235),
  ("expr -> expr '",'expr',2,'p_transpose_expression','parser.py',241),
  ('expr -> EYE ( expr )','expr',4,'p_function_expression','parser.py',247),
  ('expr -> ZEROS ( expr )','expr',4,'p_function_expression','parser.py',248),
  ('expr -> ONES ( expr )','expr',4,'p_function_expression','parser.py',249),
  ('expr -> FLOATNUM','expr',1,'p_float_expr','parser.py',261),
  ('expr -> INTNUM','expr',1,'p_int_expr','parser.py',267),
  ('expr -> STRING','expr',1,'p_string_expr','parser.py',273),
  ('expr -> ID','expr',1,'p_id_expr','parser.py',279),
  ('expr -> [ expressions ]','expr',3,'p_vector_expr','parser.py',285),
  ('expr -> [ range ]','expr',3,'p_range_vector_expr','parser.py',291),
  ('expressions -> expressions , expr','expressions',3,'p_expressions','parser.py',297),
  ('expressions -> expr','expressions',1,'p_expressions','parser.py',298),
  ('range -> expr : expr','range',3,'p_range','parser.py',309),
]
