from pywebio.session import run_js


def update():
    run_js('window.location.reload()')
