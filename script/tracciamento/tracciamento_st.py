#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: tracciamento_st.py
# Author: Tesser Paolo
# Date: aaaa-mm-dd
# Desc: this script starts when make command it's start to generate Spefica Tecnica document.
# It takes value from componenti-requisiti.tex file and generate viceversa table.
#
# Mail: p.tesser921@gmail.com
# Modify
# Version   Date        Author          Description
# =======================================================================
# 
# -----------------------------------------------------------------------
#
# -----------------------------------------------------------------------
#
#
__author__ = 'ptesser'
from requisiti_fonti import RequisitiFonti

if __name__ == '__main__':

    print "*** Start: generazione file contenente lista requisiti tracciati con i componenti " \
          "presi da componenti-requisiti.text"

    r = RequisitiFonti()
    r.open_doc_req()
    r.open_doc_componenti()
    r.take_req()
    r.take_req_comp()
    r.write_list_req_for_comp()

    print "*** End: generazione file contenente lista requisiti tracciati con i componenti " \
          "presi da componenti-requisiti.text"
