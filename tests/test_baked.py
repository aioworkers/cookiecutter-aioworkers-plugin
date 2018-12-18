from pathlib import Path


def test_default(cookies, project_checker):
    result = cookies.bake()
    project_checker(result)

    # check files in project
    path = Path(result.project)
    assert (path / 'README.rst').exists()
