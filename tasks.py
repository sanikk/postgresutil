from invoke import task


@task
def start(c):
    c.run('python sql_filler/main.py')
