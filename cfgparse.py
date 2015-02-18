# -*- coding: utf-8 -*-
class Config(object):
    pass
cfg = Config()
fname = 'cfg.py'
cfg_globals = {'i': 3}
cfg_locals = {}
print 'BEFORE: cfg_globals =', cfg_globals
print 'BEFORE: cfg_locals =', cfg_locals
#execfile(fname, cfg_globals, cfg_locals)
execfile(fname, {}, cfg.__dict__)
print 'AFTER: cfg_globals =', cfg_globals
print 'AFTER: cfg_locals =', cfg_locals
print 'AFTER: cfg.__dict__ =', cfg.__dict__
print 'cfg.msg:', repr(cfg.msg)
print 'cfg.pi:', repr(cfg.pi)
