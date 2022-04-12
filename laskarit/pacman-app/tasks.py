from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/peli.py", pty=True)

@task
def test(ctx):
    ctx.run("python3 src/tests/peli_test.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
