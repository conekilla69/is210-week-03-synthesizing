#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM  = '42'
EMAIL = '{FNAME}, {NTYPE}, (RNUM}'.format(NEWS, FNAME='friend', NTYPE='0', RNUM='1')
 
=
