# from app.src.repositories.factory_repository import (
#     FactoryRepository,
#     RepositoryName
# )
import sys
[sys.path.append(i) for i in ['.', '..']]

from app.src.repositories.factory_repository import FactoryRepository, RepositoryName

factory = FactoryRepository()

example = factory.get_repository(RepositoryName.EXAMPLE_REPOSITORY.value)
example.get_list()