from app.src.repositories.factory_repository import FactoryRepository, RepositoryName


def test_get_list():
    factory = FactoryRepository()

    example = factory.get_repository(RepositoryName.EXAMPLE_REPOSITORY.value)
    example.get_list()

    assert True