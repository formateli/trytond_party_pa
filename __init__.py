# This file is part of party_pa module.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import configuration


def register():
    Pool.register(
        configuration.Configuration,
        module='party_pa', type_='model')
