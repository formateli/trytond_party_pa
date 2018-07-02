# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Party', 'PartyIdentifier']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'

    party_type = fields.Selection([
            (None, ''),
            ('n', 'Natural'),
            ('e', 'Empresa'),
            ('f', 'Fundacion'),
            ('p', 'Publica'),
            ], 'Type')


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
