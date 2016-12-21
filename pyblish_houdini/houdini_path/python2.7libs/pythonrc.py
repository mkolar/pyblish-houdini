try:
    __import__("pyblish_houdini")

except ImportError as e:
    print "pyblish: Could not load integration: %s" % e

else:
    import pyblish.api
    pyblish.api.register_gui("pyblish_qml")
    pyblish.api.register_gui("pyblish_lite")

    import pyblish_houdini
    pyblish_houdini.setup()
