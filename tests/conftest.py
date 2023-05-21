import py
import pytest
import sh
from pytest_cookies.plugin import Cookies


@pytest.fixture(scope="session")
def cookies(request, _cookiecutter_config_file):
    # Customize directory to bake projects
    template_dir = request.config.option.template
    p = py.path.local("tests/projects")
    if p.exists():
        p.remove()
    output_factory = py.path.local("tests").mkdir("projects").mkdir

    return Cookies(template_dir, output_factory, _cookiecutter_config_file)


@pytest.fixture
def project_checker():
    def check(result):
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project.isdir()

        # Check project with ruff
        try:
            sh.ruff(str(result.project))
        except sh.ErrorReturnCode as e:
            print(e)  # noqa
            pytest.fail(e)

    return check
