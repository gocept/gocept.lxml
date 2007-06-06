==============================
Interface Definitions For lxml
==============================

This package provides zope interfaces for lxml objects. Far from being
complete but a starting point.

Interfaces
==========

Interfaces are here::    
    
    >>> import gocept.lxml.interfaces

There is an interface for lxml.etree elements::

    >>> import lxml.etree
    >>> xml = lxml.etree.fromstring('<a/>')
    >>> gocept.lxml.interfaces.IElement.providedBy(xml)
    True

And for objectifieds::

    >>> import lxml.objectify
    >>> obj = lxml.objectify.fromstring('<a><str>holla</str></a>')
    >>> gocept.lxml.interfaces.IElement.providedBy(obj)
    True
    >>> gocept.lxml.interfaces.IObjectified.providedBy(obj)
    True
    >>> gocept.lxml.interfaces.IElement.providedBy(obj.str)
    True
    >>> gocept.lxml.interfaces.IObjectified.providedBy(obj.str)
    True
