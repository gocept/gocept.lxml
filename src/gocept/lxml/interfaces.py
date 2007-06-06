# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import lxml.objectify

import zope.interface


class IElement(zope.interface.Interface):
    """An lxml.etree.ElementBase object."""

    # XXX add methods and attributes


class IObjectified(zope.interface.Interface):
    """An objectified element."""
