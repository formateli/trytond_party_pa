# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval, Not, In

__all__ = ['Party', 'PartyIdentifier']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'

    party_type = fields.Selection([
            (None, ''),
            ('natural', 'Natural'),
            ('privada', 'Empresa Privada'),
            ('fundacion', 'Fundacion'),
            ('publica', 'Empresa Publica'),
            ('gobierno', 'Gobierno'),
        ], 'Type')
    dob = fields.Date('Date of Birth')
    gender = fields.Selection([
            (None, ''),
            ('male', 'Masculino'),
            ('female', 'Femenino'),
        ], 'Gender',
        states={
            'invisible': Not(In(Eval('party_type'), ['natural',])),
        }, depends=['party_type'])
    estado_civil = fields.Selection([
            (None, ''),
            ('casado', 'Casado'),
            ('soltero', 'Soltero'),
            ('divorciado', 'Divorciado'),
            ('Viudo', 'Viudo'),
        ], 'Estado Civil',
        states={
            'invisible': Not(In(Eval('party_type'), ['natural',])),
        }, depends=['party_type'])


class PartyIdentifier:
    __metaclass__ = PoolMeta
    __name__ = 'party.identifier'

    @classmethod
    def __setup__(cls):
        super(PartyIdentifier, cls).__setup__()
        cls.type.selection += [
                ('ruc', 'RUC'),
                ('ci', 'C.I.'),
                ('passport', 'Passport'),
            ]
        cls.type.required = True
