# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval, Not, In

__all__ = ['PartyIdentifier']


class PartyIdentifier(metaclass=PoolMeta):
    __name__ = 'party.identifier'

    @classmethod
    def __setup__(cls):
        super(PartyIdentifier, cls).__setup__()
        cls.type.selection += [
            ('ruc', 'RUC'),
            ('ci', 'C.I.'),
            ('passport', 'Passport'),
            ]
