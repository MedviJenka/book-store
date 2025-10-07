from backend.utils.logs import Logfire


log = Logfire('smoke-test')


def test() -> None:
    assert 1 + 1 == 2, log.fire.error('error')
