# This file is part of party_pa module.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta


class Configuration(metaclass=PoolMeta):
    __name__ = 'party.configuration'

    @classmethod
    def __setup__(cls):
        super(Configuration, cls).__setup__()
        cls.identifier_types.selection += [
            ('pa_ruc', 'Panamenian Tax Identifier - RUC'),
            ('pa_ci', 'Panamenian Personal ID Identifier - CI'),
            ]
