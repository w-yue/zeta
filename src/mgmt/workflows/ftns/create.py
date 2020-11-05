# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Authors.

# Authors: Phu Tran          <@phudtran>

from common.workflow import *
from operators.ftns_operator import *
from operators.chains_operator import *
from operators.dfts_operator import *

dfts_opr = DftOperator()
chains_opr = ChainOperator()
ftns_opr = FtnOperator()


def ftn_create(task, ftn, name, body, spec):
    logger.info("Creating Ftn {}!".format(name))
    if not ftn:
        ftn = ftns_opr.get_stored_obj(name, spec)
    if not dfts_opr.store.contains_obj(ftn.dft, KIND.dft):
        task.raise_temporary_error(
            "Parent DFT {} not yet created!".format(ftn.dft))
    if not chains_opr.store.contains_obj(ftn.parent_chain, KIND.chain):
        task.raise_temporary_error(
            "Parent Chain {} not yet created!".format(ftn.parent_chain))
    return ftn
